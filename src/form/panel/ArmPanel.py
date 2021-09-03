# -*- coding: utf-8 -*-
#
import wx
import wx.lib.newevent

from form.panel.BasePanel import BasePanel
from form.parts.FloatSliderCtrl import FloatSliderCtrl
from form.parts.SizingFileSet import SizingFileSet
from module.MMath import MRect, MVector3D, MVector4D, MQuaternion, MMatrix4x4 # noqa
from utils import MFormUtils, MFileUtils # noqa
from utils.MLogger import MLogger # noqa

logger = MLogger(__name__)


class ArmPanel(BasePanel):
    
    def __init__(self, frame: wx.Frame, parent: wx.Notebook, tab_idx: int):
        super().__init__(frame, parent, tab_idx)

        # 剛体リスト
        self.avoidance_set_dict = {}
        # 剛体用ダイアログ
        self.avoidance_dialog = AvoidanceDialog(self.frame)

        avoidance_tooltip = "避免指定字符串名称的骨骼跟随刚体与手腕/指尖接触。\n从选择按钮中，选择要在转换目标模型中避免的骨骼跟随刚体。\n" \
                            + "“避免头部接触”会自动计算以头部为中心的球形刚体。"
        alignment_tooltip = "调整手腕位置，使转换目标模型的手腕位置与创建源模型的手腕位置几乎相同。"

        # Bulk用接触回避データ
        self.bulk_avoidance_set_dict = {}

        # 同じグループなので、とりあえず宣言だけしておく
        self.arm_process_flg_avoidance = wx.CheckBox(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize)
        self.arm_process_flg_avoidance.SetToolTip(avoidance_tooltip)
        self.arm_process_flg_avoidance.Bind(wx.EVT_CHECKBOX, self.set_output_vmd_path)
        self.arm_process_flg_alignment = wx.CheckBox(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize)
        self.arm_process_flg_alignment.SetToolTip(alignment_tooltip)
        self.arm_process_flg_alignment.Bind(wx.EVT_CHECKBOX, self.set_output_vmd_path)

        self.description_txt = wx.StaticText(self, wx.ID_ANY, "您可以根据转换目标模型调整手臂。\n您可以同时执行“避免接触”和“对齐”。（按照避免接触→对齐的顺序执行）" + \
                                             "\n手臂的动作可能与原始动作不同。 两者都需要一些时间。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sizer.Add(self.description_txt, 0, wx.ALL, 5)

        self.static_line01 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.sizer.Add(self.static_line01, 0, wx.EXPAND | wx.ALL, 5)

        # 剛体接触回避 ----------------
        self.avoidance_title_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 剛体接触回避タイトルラジオ
        self.avoidance_title_txt = wx.StaticText(self, wx.ID_ANY, u"接触回避", wx.DefaultPosition, wx.DefaultSize, 0)
        self.avoidance_title_txt.SetToolTip(avoidance_tooltip)
        self.avoidance_title_txt.Wrap(-1)
        self.avoidance_title_txt.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.avoidance_title_txt.Bind(wx.EVT_LEFT_DOWN, self.on_check_arm_process_avoidance)

        self.avoidance_title_sizer.Add(self.arm_process_flg_avoidance, 0, wx.ALL, 5)
        self.avoidance_title_sizer.Add(self.avoidance_title_txt, 0, wx.ALL, 5)
        self.sizer.Add(self.avoidance_title_sizer, 0, wx.ALL, 5)

        # 剛体接触回避説明文
        self.avoidance_description_txt = wx.StaticText(self, wx.ID_ANY, avoidance_tooltip, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sizer.Add(self.avoidance_description_txt, 0, wx.ALL, 5)

        self.avoidance_target_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 剛体名指定
        self.avoidance_target_txt_ctrl = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, (450, 80), wx.HSCROLL | wx.VSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
        self.avoidance_target_txt_ctrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.avoidance_target_txt_ctrl.Bind(wx.EVT_TEXT, self.on_check_arm_process_avoidance)
        self.avoidance_target_sizer.Add(self.avoidance_target_txt_ctrl, 1, wx.EXPAND | wx.ALL, 5)

        self.avoidance_target_btn_ctrl = wx.Button(self, wx.ID_ANY, u"刚体选择", wx.DefaultPosition, wx.DefaultSize, 0)
        self.avoidance_target_btn_ctrl.SetToolTip(u"您可以选择目标模型中的骨骼跟随刚体")
        self.avoidance_target_btn_ctrl.Bind(wx.EVT_BUTTON, self.on_click_avoidance_target)
        self.avoidance_target_sizer.Add(self.avoidance_target_btn_ctrl, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.sizer.Add(self.avoidance_target_sizer, 0, wx.ALL, 0)

        self.static_line03 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.sizer.Add(self.static_line03, 0, wx.EXPAND | wx.ALL, 5)

        # 手首位置合わせ --------------------
        self.alignment_title_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 手首位置合わせタイトルラジオ
        self.alignment_title_txt = wx.StaticText(self, wx.ID_ANY, u"对齐位置", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_title_txt.SetToolTip("根据转换目标模型的手腕位置调整双手并拢或接触地板的动作。\n" + \
                                            "通过调整每个距离，您可以调整对齐范围。")
        self.alignment_title_txt.Wrap(-1)
        self.alignment_title_txt.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.alignment_title_txt.Bind(wx.EVT_LEFT_DOWN, self.on_check_arm_process_alignment)

        self.alignment_title_sizer.Add(self.arm_process_flg_alignment, 0, wx.ALL, 5)
        self.alignment_title_sizer.Add(self.alignment_title_txt, 0, wx.ALL, 5)
        self.sizer.Add(self.alignment_title_sizer, 0, wx.ALL, 5)

        # 手首位置合わせ説明文
        self.alignment_description_txt = wx.StaticText(self, wx.ID_ANY, alignment_tooltip, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sizer.Add(self.alignment_description_txt, 0, wx.ALL, 5)

        # オプションサイザー
        self.alignment_option_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 指位置合わせ
        self.arm_alignment_finger_flg_ctrl = wx.CheckBox(self, wx.ID_ANY, u"手指位置对齐", wx.DefaultPosition, wx.DefaultSize, 0)
        self.arm_alignment_finger_flg_ctrl.SetToolTip(u"如果您检查一下，您可以根据手指距离，如手指TAT动作调整腕部位置。" \
                                                      + "在复数人数动作off的情况下变得更漂亮。")
        self.arm_alignment_finger_flg_ctrl.Bind(wx.EVT_CHECKBOX, self.on_check_arm_process_alignment)
        self.alignment_option_sizer.Add(self.arm_alignment_finger_flg_ctrl, 0, wx.ALL, 5)

        # 床位置合わせ
        self.arm_alignment_floor_flg_ctrl = wx.CheckBox(self, wx.ID_ANY, u"与地板对齐", wx.DefaultPosition, wx.DefaultSize, 0)
        self.arm_alignment_floor_flg_ctrl.SetToolTip(u"如果您检查它，如果手腕下沉并漂浮在地板上，您可以调整手腕的位置到原始模型。\nセンター的位置也一起调整。")
        self.arm_alignment_floor_flg_ctrl.Bind(wx.EVT_CHECKBOX, self.on_check_arm_process_alignment)
        self.alignment_option_sizer.Add(self.arm_alignment_floor_flg_ctrl, 0, wx.ALL, 5)

        self.sizer.Add(self.alignment_option_sizer, 0, wx.ALL, 5)

        # 手首位置スライダー
        self.alignment_distance_wrist_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.alignment_distance_wrist_txt = wx.StaticText(self, wx.ID_ANY, u"手腕之间的距离　  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_wrist_txt.SetToolTip(u"如果手腕功能，请指定如何执行手腕对齐。\n值越小，手腕越小地接近手腕对齐。\n距离单位是原始模型的手掌的大小。" \
                                                     + "\n在尺寸期间，手腕之间的距离出现在“消息”字段中，因此请参阅它。\n如果将滑块设置为最大值，则始终执行手腕对齐。（对双手剑有用）")
        self.alignment_distance_wrist_txt.Wrap(-1)
        self.alignment_distance_wrist_sizer.Add(self.alignment_distance_wrist_txt, 0, wx.ALL, 5)

        self.alignment_distance_wrist_label = wx.StaticText(self, wx.ID_ANY, u"（1.7）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_wrist_label.SetToolTip(u"当前指定的手腕之间的距离。 如果原始模型的原始模型在此范围内，则对齐手腕。")
        self.alignment_distance_wrist_label.Wrap(-1)
        self.alignment_distance_wrist_sizer.Add(self.alignment_distance_wrist_label, 0, wx.ALL, 5)

        self.alignment_distance_wrist_slider = FloatSliderCtrl(self, wx.ID_ANY, 1.7, 0, 10, 0.1, self.alignment_distance_wrist_label, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.alignment_distance_wrist_slider.Bind(wx.EVT_SCROLL_CHANGED, self.on_check_arm_process_alignment)
        self.alignment_distance_wrist_sizer.Add(self.alignment_distance_wrist_slider, 1, wx.ALL | wx.EXPAND, 5)

        self.sizer.Add(self.alignment_distance_wrist_sizer, 0, wx.ALL | wx.EXPAND, 5)

        # 指位置スライダー
        self.alignment_distance_finger_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.alignment_distance_finger_txt = wx.StaticText(self, wx.ID_ANY, u"手指的距离　　  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_finger_txt.SetToolTip(u"接近多少手指，指定是否执行手指对齐。\n值越小，仅当手指接近时的手指对齐。\n距离单位是原始模型的手掌的大小。\n" \
                                                      + "\n在尺寸期间，手指之间的距离出现在“消息”字段中，因此请参阅它。\n将滑块设置为最大值时，总是进行手指对准。")
        self.alignment_distance_finger_txt.Wrap(-1)
        self.alignment_distance_finger_sizer.Add(self.alignment_distance_finger_txt, 0, wx.ALL, 5)

        self.alignment_distance_finger_label = wx.StaticText(self, wx.ID_ANY, u"（1.4）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_finger_label.SetToolTip(u"这是当前指定手指之间的距离。原模型的两个手指位置在该范围内时，进行手指间的定位。")
        self.alignment_distance_finger_label.Wrap(-1)
        self.alignment_distance_finger_sizer.Add(self.alignment_distance_finger_label, 0, wx.ALL, 5)

        self.alignment_distance_finger_slider = FloatSliderCtrl(self, wx.ID_ANY, 1.4, 0, 10, 0.1, self.alignment_distance_finger_label, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.alignment_distance_finger_slider.Bind(wx.EVT_SCROLL_CHANGED, self.on_check_arm_process_alignment)
        self.alignment_distance_finger_sizer.Add(self.alignment_distance_finger_slider, 1, wx.ALL | wx.EXPAND, 5)

        self.sizer.Add(self.alignment_distance_finger_sizer, 0, wx.ALL | wx.EXPAND, 5)

        # 手首と床との位置スライダー
        self.alignment_distance_floor_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.alignment_distance_floor_txt = wx.StaticText(self, wx.ID_ANY, u"腕部和地板的距离    ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_floor_txt.SetToolTip(u"如果腕部和地板接近，请指定是否与手腕和地板进行对齐。\n值越小，手腕和地板接近时的对准越多。\n距离单位是原始模型的手掌的大小。" \
                                                     + "\n在进行循环时，手腕和地板之间的距离会出现在信息栏中，请参考。\n将滑块设置为最大时，我们将始终对齐手腕和地板。")
        self.alignment_distance_floor_txt.Wrap(-1)
        self.alignment_distance_floor_sizer.Add(self.alignment_distance_floor_txt, 0, wx.ALL, 5)

        self.alignment_distance_floor_label = wx.StaticText(self, wx.ID_ANY, u"（1.2）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.alignment_distance_floor_label.SetToolTip(u"它是当前指定的手腕和地板之间的距离。 如果原始模型和地板之间的距离在此范围内，与手腕和地板对齐。")
        self.alignment_distance_floor_label.Wrap(-1)
        self.alignment_distance_floor_sizer.Add(self.alignment_distance_floor_label, 0, wx.ALL, 5)

        self.alignment_distance_floor_slider = FloatSliderCtrl(self, wx.ID_ANY, 1.2, 0, 10, 0.1, self.alignment_distance_floor_label, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.alignment_distance_floor_slider.Bind(wx.EVT_SCROLL_CHANGED, self.on_check_arm_process_alignment)
        self.alignment_distance_floor_sizer.Add(self.alignment_distance_floor_slider, 1, wx.ALL | wx.EXPAND, 5)

        self.sizer.Add(self.alignment_distance_floor_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.static_line04 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.sizer.Add(self.static_line04, 0, wx.EXPAND | wx.ALL, 5)

        # 腕チェックスキップ --------------------
        self.arm_check_skip_sizer = wx.BoxSizer(wx.VERTICAL)

        self.arm_check_skip_flg_ctrl = wx.CheckBox(self, wx.ID_ANY, u"跳过手臂～手腕的可调节检查", wx.DefaultPosition, wx.DefaultSize, 0)
        self.arm_check_skip_flg_ctrl.SetToolTip(u"跳过可循环检查（有手臂IK时不可），务必进行处理。")
        self.arm_check_skip_sizer.Add(self.arm_check_skip_flg_ctrl, 0, wx.ALL, 5)

        self.arm_check_skip_description = wx.StaticText(self, wx.ID_ANY, u"跳过手臂可旋转检查（有手臂IK时不可），务必进行手臂关系处理。\n" \
                                                        + "※循环结果可能会变奇怪，但不属于BUG。", \
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.arm_check_skip_description.Wrap(-1)
        self.arm_check_skip_sizer.Add(self.arm_check_skip_description, 0, wx.ALL, 5)
        self.sizer.Add(self.arm_check_skip_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.fit()
    
    def get_avoidance_target(self):
        if len(self.bulk_avoidance_set_dict.keys()) > 0:
            # Bulk用データがある場合、優先返還
            return self.bulk_avoidance_set_dict
        
        target = {}
        if self.arm_process_flg_avoidance.GetValue() == 0:
            return target
        
        # 選択された剛体リストを入力欄に設定(ハッシュが同じ場合のみ)
        if 1 in self.avoidance_set_dict and self.avoidance_set_dict[1].rep_choices:
            if self.avoidance_set_dict[1].equal_hashdigest(self.frame.file_panel_ctrl.file_set):
                target[0] = [self.avoidance_set_dict[1].rep_avoidance_names[n] for n in self.avoidance_set_dict[1].rep_choices.GetSelections()]
            else:
                logger.warning("【No.%s】设置回避接触后，文件集发生了变更，解除了接触回避", 1, decoration=MLogger.DECORATION_BOX)

        for set_no in list(self.avoidance_set_dict.keys())[1:]:
            if set_no in self.avoidance_set_dict and self.avoidance_set_dict[set_no].rep_choices:
                if len(self.frame.multi_panel_ctrl.file_set_list) >= set_no - 1 and self.avoidance_set_dict[set_no].equal_hashdigest(self.frame.multi_panel_ctrl.file_set_list[set_no - 2]):
                    target[set_no - 1] = [self.avoidance_set_dict[set_no].rep_avoidance_names[n] for n in self.avoidance_set_dict[set_no].rep_choices.GetSelections()]
                else:
                    logger.warning("【No.%s】设置回避接触后，文件集发生了变更，解除了接触回避", set_no, decoration=MLogger.DECORATION_BOX)

        return target
    
    def on_click_avoidance_target(self, event: wx.Event):
        if self.avoidance_dialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed their mind

        # 一旦クリア
        self.avoidance_target_txt_ctrl.SetValue("")

        # 選択された剛体リストを入力欄に設定
        for set_no, set_data in self.avoidance_set_dict.items():
            # 選択肢ごとの表示文言
            if set_data.rep_choices:
                selections = [set_data.rep_choices.GetString(n) for n in set_data.rep_choices.GetSelections()]
                self.avoidance_target_txt_ctrl.WriteText("【No.{0}】{1}\n".format(set_no, ', '.join(selections)))

        self.arm_process_flg_avoidance.SetValue(1)
        self.avoidance_dialog.Hide()

    def initialize(self, event: wx.Event):

        if 1 in self.avoidance_set_dict:
            # ファイルタブ用接触回避のファイルセットがある場合
            if self.frame.file_panel_ctrl.file_set.is_loaded():
                # 既にある場合、ハッシュチェック
                if self.avoidance_set_dict[1].equal_hashdigest(self.frame.file_panel_ctrl.file_set):
                    # 同じである場合、スルー
                    pass
                else:
                    # 違う場合、ファイルセット読み直し
                    self.add_set(1, self.frame.file_panel_ctrl.file_set, replace=True)
            else:
                # ファイルタブが読み込み失敗している場合、読み直し（クリア）
                self.add_set(1, self.frame.file_panel_ctrl.file_set, replace=True)
        else:
            # 空から作る場合、ファイルタブのファイルセット参照
            self.add_set(1, self.frame.file_panel_ctrl.file_set, replace=False)
        
        # multiはあるだけ調べる
        for multi_file_set_idx, multi_file_set in enumerate(self.frame.multi_panel_ctrl.file_set_list):
            set_no = multi_file_set_idx + 2
            if set_no in self.avoidance_set_dict:
                # 複数タブ用接触回避のファイルセットがある場合
                if multi_file_set.is_loaded():
                    # 既にある場合、ハッシュチェック
                    if self.avoidance_set_dict[set_no].equal_hashdigest(multi_file_set):
                        # 同じである場合、スルー
                        pass
                    else:
                        # 違う場合、ファイルセット読み直し
                        self.add_set(set_no, multi_file_set, replace=True)
                    
                        # 複数件ある場合、手首間の距離デフォルト値変更
                        self.alignment_distance_wrist_slider.SetValue(2.5)
                        self.alignment_distance_wrist_label.SetLabel("（2.5）")
                else:
                    # 複数タブが読み込み失敗している場合、読み直し（クリア）
                    self.add_set(set_no, multi_file_set, replace=True)

                    # 複数件ある場合、手首間の距離デフォルト値変更
                    self.alignment_distance_wrist_slider.SetValue(2.5)
                    self.alignment_distance_wrist_label.SetLabel("（2.5）")
            else:
                # 空から作る場合、複数タブのファイルセット参照
                self.add_set(set_no, multi_file_set, replace=False)
            
                # 複数件ある場合、手首間の距離デフォルト値変更
                self.alignment_distance_wrist_slider.SetValue(2.5)
                self.alignment_distance_wrist_label.SetLabel("（2.5）")

        # 腕系不可モデル名リスト
        disable_arm_model_names = []

        if self.frame.file_panel_ctrl.file_set.is_loaded():
            if not self.frame.file_panel_ctrl.file_set.org_model_file_ctrl.data.can_arm_sizing:
                # 腕不可の場合、リスト追加
                disable_arm_model_names.append("【No.1】创建模型: {0}".format(self.frame.file_panel_ctrl.file_set.org_model_file_ctrl.data.name))

            if not self.frame.file_panel_ctrl.file_set.rep_model_file_ctrl.data.can_arm_sizing:
                # 腕不可の場合、リスト追加
                disable_arm_model_names.append("【No.1】目标模型: {0}".format(self.frame.file_panel_ctrl.file_set.rep_model_file_ctrl.data.name))

        for multi_file_set_idx, multi_file_set in enumerate(self.frame.multi_panel_ctrl.file_set_list):
            set_no = multi_file_set_idx + 2
            if multi_file_set.is_loaded():
                if not multi_file_set.org_model_file_ctrl.data.can_arm_sizing:
                    # 腕不可の場合、リスト追加
                    disable_arm_model_names.append("【No.{0}】创建模型: {1}".format(set_no, multi_file_set.org_model_file_ctrl.data.name))

                if not multi_file_set.rep_model_file_ctrl.data.can_arm_sizing:
                    # 腕不可の場合、リスト追加
                    disable_arm_model_names.append("【No.{0}】目标模型: {1}".format(set_no, multi_file_set.rep_model_file_ctrl.data.name))
            
        if len(disable_arm_model_names) > 0:
            # 腕不可モデルがいる場合、ダイアログ表示
            with wx.MessageDialog(self, "以下模型中含有类似“腕IK”的字符串，因此该文件集的腕部处理\n（手臂站姿校正、扭转分散、接触回避、位置对准）就会跳过。\n" \
                                  + "将手臂检查跳过FLG设为ON时，强制执行手臂系统处理。\n※但是，即使结果很奇怪也不属于BUG。\n" \
                                  + "需要将手臂检查跳过FLG设为ON吗？ \n\n{0}".format('\n'.join(disable_arm_model_names)), style=wx.YES_NO | wx.ICON_WARNING) as dialog:
                if dialog.ShowModal() == wx.ID_NO:
                    # 腕系チェックスキップOFF
                    self.arm_check_skip_flg_ctrl.SetValue(0)
                else:
                    # 腕系チェックスキップON
                    self.arm_check_skip_flg_ctrl.SetValue(1)
                
        event.Skip()

    def add_set(self, set_idx: int, file_set: SizingFileSet, replace: bool):
        new_avoidance_set = AvoidanceSet(self.frame, self, self.avoidance_dialog.scrolled_window, set_idx, file_set)
        if replace:
            # 置き換え
            self.avoidance_dialog.set_list_sizer.Hide(self.avoidance_set_dict[set_idx].set_sizer, recursive=True)
            self.avoidance_dialog.set_list_sizer.Replace(self.avoidance_set_dict[set_idx].set_sizer, new_avoidance_set.set_sizer, recursive=True)

            # 置き換えの場合、剛体リストクリア
            self.avoidance_target_txt_ctrl.SetValue("")
        else:
            # 新規追加
            self.avoidance_dialog.set_list_sizer.Add(new_avoidance_set.set_sizer, 0, wx.EXPAND | wx.ALL, 5)
        self.avoidance_set_dict[set_idx] = new_avoidance_set

        # スクロールバーの表示のためにサイズ調整
        self.avoidance_dialog.set_list_sizer.Layout()
        self.avoidance_dialog.set_list_sizer.FitInside(self.avoidance_dialog.scrolled_window)

    # VMD出力ファイルパス生成
    def set_output_vmd_path(self, event, is_force=False):
        # 念のため出力ファイルパス自動生成（空の場合設定）
        self.frame.file_panel_ctrl.file_set.set_output_vmd_path(event)

        # multiのも出力ファイルパス自動生成（空の場合設定）
        for file_set in self.frame.multi_panel_ctrl.file_set_list:
            file_set.set_output_vmd_path(event)
    
    # 処理対象：接触回避ON
    def on_check_arm_process_avoidance(self, event: wx.Event):
        # ラジオボタンかチェックボックスイベントがTrueの場合、切り替え
        if isinstance(event.GetEventObject(), wx.StaticText):
            if self.arm_process_flg_avoidance.GetValue() == 0:
                self.arm_process_flg_avoidance.SetValue(1)
            else:
                self.arm_process_flg_avoidance.SetValue(0)

        # パス再生成
        self.set_output_vmd_path(event)
        
        event.Skip()

    # 処理対象：手首位置合わせON
    def on_check_arm_process_alignment(self, event: wx.Event):
        # ラジオボタンかチェックボックスイベントがTrueの場合、切り替え
        if isinstance(event.GetEventObject(), wx.StaticText):
            if self.arm_process_flg_alignment.GetValue() == 0:
                self.arm_process_flg_alignment.SetValue(1)
            else:
                self.arm_process_flg_alignment.SetValue(0)
        else:
            if self.arm_alignment_finger_flg_ctrl.GetValue() == 1 or self.arm_alignment_floor_flg_ctrl.GetValue() == 1:
                self.arm_process_flg_alignment.SetValue(1)

        if self.arm_alignment_finger_flg_ctrl.GetValue() and len(self.frame.multi_panel_ctrl.file_set_list) > 0:
            self.frame.on_popup_finger_warning(event)

        # パス再生成
        self.set_output_vmd_path(event)

        event.Skip()


class AvoidanceSet():

    def __init__(self, frame: wx.Frame, panel: wx.Panel, window: wx.Window, set_idx: int, file_set: SizingFileSet):
        self.frame = frame
        self.panel = panel
        self.window = window
        self.set_idx = set_idx
        self.file_set = file_set
        self.rep_model_digest = 0 if not file_set.rep_model_file_ctrl.data else file_set.rep_model_file_ctrl.data.digest
        self.rep_avoidances = ["头接触回避 (頭)"]   # 選択肢文言
        self.rep_avoidance_names = ["头接触回避"]   # 選択肢文言に紐付く剛体名
        self.rep_choices = None

        self.set_sizer = wx.StaticBoxSizer(wx.StaticBox(self.window, wx.ID_ANY, "【No.{0}】".format(set_idx)), orient=wx.VERTICAL)

        if file_set.is_loaded():
            self.model_name_txt = wx.StaticText(self.window, wx.ID_ANY, file_set.rep_model_file_ctrl.data.name[:15], wx.DefaultPosition, wx.DefaultSize, 0)
            self.model_name_txt.Wrap(-1)
            self.set_sizer.Add(self.model_name_txt, 0, wx.ALL, 5)

            for rigidbody_name, rigidbody in file_set.rep_model_file_ctrl.data.rigidbodies.items():
                # 処理対象剛体：有効なボーン追従剛体
                if rigidbody.isModeStatic() and rigidbody.bone_index in file_set.rep_model_file_ctrl.data.bone_indexes:
                    self.rep_avoidances.append("{0} ({1})".format(rigidbody.name, file_set.rep_model_file_ctrl.data.bone_indexes[rigidbody.bone_index]))
                    self.rep_avoidance_names.append(rigidbody.name)

            # 選択コントロール
            self.rep_choices = wx.ListBox(self.window, id=wx.ID_ANY, choices=self.rep_avoidances, style=wx.LB_MULTIPLE | wx.LB_NEEDED_SB, size=(-1, 220))
            # 頭接触回避はデフォルトで選択
            self.rep_choices.SetSelection(0)
            self.set_sizer.Add(self.rep_choices, 0, wx.ALL, 5)

            # 一括用コピーボタン
            self.copy_btn_ctrl = wx.Button(self.window, wx.ID_ANY, u"统一CSV复制", wx.DefaultPosition, wx.DefaultSize, 0)
            self.copy_btn_ctrl.SetToolTip(u"将避免接触的数据以统一CSV的形式复制到剪贴板")
            self.copy_btn_ctrl.Bind(wx.EVT_BUTTON, self.on_copy)
            self.set_sizer.Add(self.copy_btn_ctrl, 0, wx.ALL, 5)
        else:
            self.no_data_txt = wx.StaticText(self.window, wx.ID_ANY, u"无数据", wx.DefaultPosition, wx.DefaultSize, 0)
            self.no_data_txt.Wrap(-1)
            self.set_sizer.Add(self.no_data_txt, 0, wx.ALL, 5)

    def on_copy(self, event: wx.Event):
        # 一括CSV用モーフテキスト生成
        avoidance_txt_list = []
        for idx in self.rep_choices.GetSelections():
            avoidance_txt_list.append(f"{self.rep_avoidance_names[idx]}")
        # 文末セミコロン
        avoidance_txt_list.append("")

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(";".join(avoidance_txt_list)))
            wx.TheClipboard.Close()

        with wx.TextEntryDialog(self.frame, u"输出批量处理避免接触用的CSV数据。\n" \
                                + "显示对话框后，以下避免接触的数据已复制到剪贴板。\n" \
                                + "如果无法复制，请选择框中的字符串并粘贴到CSV上。", caption=u"统一CSV用接触回避数据",
                                value=";".join(avoidance_txt_list), style=wx.TextEntryDialogStyle, pos=wx.DefaultPosition) as dialog:
            dialog.ShowModal()

    # 現在のファイルセットのハッシュと同じであるかチェック
    def equal_hashdigest(self, now_file_set: SizingFileSet):
        return self.rep_model_digest == now_file_set.rep_model_file_ctrl.data.digest


class AvoidanceDialog(wx.Dialog):

    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, title="选择避免接触的刚体", pos=(-1, -1), size=(800, 500), style=wx.DEFAULT_DIALOG_STYLE, name="AvoidanceDialog")

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # 説明文
        self.description_txt = wx.StaticText(self, wx.ID_ANY, u"可以从变换目标模型中选择想要避免手的机械追从刚体。\n" \
                                             + u"“头接触回避”是自动计算头的大小的刚体。如果结果不好，请取消选择。\n" \
                                             + u"如果是追随者刚体的话没有限制，但是如果选择太多的刚体的话，手哪里都不能避免，可能会出现意想不到的结果。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sizer.Add(self.description_txt, 0, wx.ALL, 5)

        # ボタン
        self.btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ok_btn = wx.Button(self, wx.ID_OK, "确定")
        self.btn_sizer.Add(self.ok_btn, 0, wx.ALL, 5)

        self.calcel_btn = wx.Button(self, wx.ID_CANCEL, "取消")
        self.btn_sizer.Add(self.calcel_btn, 0, wx.ALL, 5)
        self.sizer.Add(self.btn_sizer, 0, wx.ALL, 5)

        self.static_line01 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.sizer.Add(self.static_line01, 0, wx.EXPAND | wx.ALL, 5)

        self.scrolled_window = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, \
                                                 wx.FULL_REPAINT_ON_RESIZE | wx.HSCROLL | wx.ALWAYS_SHOW_SB)
        self.scrolled_window.SetScrollRate(5, 5)

        # 接触回避用剛体セット用基本Sizer
        self.set_list_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # スクロールバーの表示のためにサイズ調整
        self.scrolled_window.SetSizer(self.set_list_sizer)
        self.scrolled_window.Layout()
        self.sizer.Add(self.scrolled_window, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(self.sizer)
        self.sizer.Layout()
        
        # 画面中央に表示
        self.CentreOnScreen()
        
        # 最初は隠しておく
        self.Hide()

