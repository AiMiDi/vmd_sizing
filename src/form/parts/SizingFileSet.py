# -*- coding: utf-8 -*-
#
import os
import wx
import wx.lib.newevent

from form.parts.BaseFilePickerCtrl import BaseFilePickerCtrl
from form.parts.HistoryFilePickerCtrl import HistoryFilePickerCtrl
from module.MMath import MRect, MVector3D, MVector4D, MQuaternion, MMatrix4x4 # noqa
from utils import MFormUtils, MFileUtils # noqa
from utils.MLogger import MLogger # noqa

logger = MLogger(__name__)


class SizingFileSet():

    def __init__(self, frame: wx.Frame, panel: wx.Panel, file_hitories: dict, set_no):
        self.file_hitories = file_hitories
        self.frame = frame
        self.panel = panel
        self.set_no = set_no
        self.STANCE_DETAIL_CHOICES = ["センターXZ校正", "上半身补正", "下半身补正", "足ＩＫ校正", "つま先校正", "つま先ＩＫ校正", "肩校正", "センターY校正"]
        self.selected_stance_details = [0, 1, 2, 4, 5, 6, 7]

        if self.set_no == 1:
            # ファイルパネルのはそのまま追加
            self.set_sizer = wx.BoxSizer(wx.VERTICAL)
        else:
            self.set_sizer = wx.StaticBoxSizer(wx.StaticBox(self.panel, wx.ID_ANY, "【No.{0}】".format(set_no)), orient=wx.VERTICAL)

        able_aster_toottip = "文件名使用星号（*）的话，可以一次校准多个数据。" if self.set_no == 1 else "不能批量指定。"
        # VMD/VPDファイルコントロール
        self.motion_vmd_file_ctrl = HistoryFilePickerCtrl(frame, panel, u"调整对象动作VMD/VPD", u"打开调整对象动作VMD/VPD文件", ("vmd", "vpd"), wx.FLP_DEFAULT_STYLE, \
                                                          u"请指定想要调整的动作的VMD/VPD路径。\n可通过拖拽指定、打开按钮指定、从历史记录中选择。\n{0}".format(able_aster_toottip), \
                                                          file_model_spacer=46, title_parts_ctrl=None, title_parts2_ctrl=None, file_histories_key="vmd", is_change_output=True, \
                                                          is_aster=True, is_save=False, set_no=set_no)
        self.set_sizer.Add(self.motion_vmd_file_ctrl.sizer, 1, wx.EXPAND, 0)

        # 作成元のスタンス詳細再現FLG
        detail_stance_flg_ctrl = wx.CheckBox(panel, wx.ID_ANY, u"姿势追加修正", wx.DefaultPosition, wx.DefaultSize, 0)
        detail_stance_flg_ctrl.SetToolTip(u"如果勾选的话，可以追加细微的姿势补偿。\n请按一下校正内容的详细内容旁边的「＊」按钮。")
        detail_stance_flg_ctrl.Bind(wx.EVT_CHECKBOX, self.set_output_vmd_path)

        # スタンス補正
        detail_btn_ctrl = wx.Button(panel, wx.ID_ANY, u"＊", wx.DefaultPosition, (20, 20), 0)
        detail_btn_ctrl.SetToolTip("可以确认姿势追加修正的详细内容，以及进行取舍选择。")
        detail_btn_ctrl.Bind(wx.EVT_BUTTON, self.select_detail)

        # 作成元PMXファイルコントロール
        self.org_model_file_ctrl = HistoryFilePickerCtrl(frame, panel, u"动作制作原模型PMX", u"打开动作制作原模型PMX文件", ("pmx"), wx.FLP_DEFAULT_STYLE, \
                                                         u"请指定用于创建动作的模型的PMX路径。\n精度虽然下降，但也可以用类似尺寸、骨架结构的模型来代替。\n可通过拖拽指定、打开按钮指定、从历史记录中选择。", \
                                                         file_model_spacer=1, title_parts_ctrl=detail_stance_flg_ctrl, title_parts2_ctrl=detail_btn_ctrl, \
                                                         file_histories_key="org_pmx", is_change_output=False, is_aster=False, is_save=False, set_no=set_no)
        self.set_sizer.Add(self.org_model_file_ctrl.sizer, 1, wx.EXPAND, 0)

        # 分散旋转骨追加FLG
        twist_flg_ctrl = wx.CheckBox(panel, wx.ID_ANY, u"分散旋转骨", wx.DefaultPosition, wx.DefaultSize, 0)
        twist_flg_ctrl.SetToolTip(u"如果勾选的话，可以追加胳膊扭转等分散处理。\n需要时间。")
        twist_flg_ctrl.Bind(wx.EVT_CHECKBOX, self.set_output_vmd_path)

        # 変換先PMXファイルコントロール
        self.rep_model_file_ctrl = HistoryFilePickerCtrl(frame, panel, u"动作变换目标模型PMX", u"打开动作变换目标模型PMX文件", ("pmx"), wx.FLP_DEFAULT_STYLE, \
                                                         u"请指定想要实际读入动作的模型的PMX路径。\n可通过拖拽指定、打开按钮指定、从历史记录中选择。", \
                                                         file_model_spacer=18, title_parts_ctrl=twist_flg_ctrl, title_parts2_ctrl=None, file_histories_key="rep_pmx", \
                                                         is_change_output=True, is_aster=False, is_save=False, set_no=set_no)
        self.set_sizer.Add(self.rep_model_file_ctrl.sizer, 1, wx.EXPAND, 0)

        # 出力先VMDファイルコントロール
        self.output_vmd_file_ctrl = BaseFilePickerCtrl(frame, panel, u"导出VMD", u"打开输出VMD文件", ("vmd"), wx.FLP_OVERWRITE_PROMPT | wx.FLP_SAVE | wx.FLP_USE_TEXTCTRL, \
                                                       u"请指定调整结果的VMD输出路径。\根据源VMD文件和转换目标PMX的文件名自动生成，也可以变更为任意路径。", \
                                                       is_aster=False, is_save=True, set_no=set_no)
        self.set_sizer.Add(self.output_vmd_file_ctrl.sizer, 1, wx.EXPAND, 0)

    def get_selected_stance_details(self):
        # 選択されたINDEXの名称を返す
        return [self.STANCE_DETAIL_CHOICES[n] for n in self.selected_stance_details]

    def select_detail(self, event: wx.Event):

        with wx.MultiChoiceDialog(self.panel, "站姿追加修正中，只实施有检查的修正", caption="站姿追加修正选择", \
                                  choices=self.STANCE_DETAIL_CHOICES, style=wx.CHOICEDLG_STYLE) as choiceDialog:

            choiceDialog.SetSelections(self.selected_stance_details)

            if choiceDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            
            self.selected_stance_details = choiceDialog.GetSelections()

            if len(self.selected_stance_details) == 0:
                self.org_model_file_ctrl.title_parts_ctrl.SetValue(0)
            else:
                self.org_model_file_ctrl.title_parts_ctrl.SetValue(1)

    def save(self):
        self.motion_vmd_file_ctrl.save()
        self.org_model_file_ctrl.save()
        self.rep_model_file_ctrl.save()

    # フォーム無効化
    def disable(self):
        self.motion_vmd_file_ctrl.disable()
        self.org_model_file_ctrl.disable()
        self.rep_model_file_ctrl.disable()
        self.output_vmd_file_ctrl.disable()

    # フォーム無効化
    def enable(self):
        self.motion_vmd_file_ctrl.enable()
        self.org_model_file_ctrl.enable()
        self.rep_model_file_ctrl.enable()
        self.output_vmd_file_ctrl.enable()

    # ファイル読み込み前のチェック
    def is_valid(self):
        result = True
        if self.set_no == 1:
            # 1番目は必ず調べる
            result = self.motion_vmd_file_ctrl.is_valid() and result
            result = self.org_model_file_ctrl.is_valid() and result
            result = self.rep_model_file_ctrl.is_valid() and result
            result = self.output_vmd_file_ctrl.is_valid() and result
        else:
            # 2番目以降は、ファイルが揃ってたら調べる
            if self.motion_vmd_file_ctrl.is_set_path() or self.org_model_file_ctrl.is_set_path() or \
               self.rep_model_file_ctrl.is_set_path() or self.output_vmd_file_ctrl.is_set_path():
                result = self.motion_vmd_file_ctrl.is_valid() and result
                result = self.org_model_file_ctrl.is_valid() and result
                result = self.rep_model_file_ctrl.is_valid() and result
                result = self.output_vmd_file_ctrl.is_valid() and result

        return result

    # 入力後の入力可否チェック
    def is_loaded_valid(self):
        if self.set_no == 0:
            # CSVとかのファイルは番号出力なし
            display_set_no = ""
        else:
            display_set_no = "{0}番目の".format(self.set_no)
        
        # 両方のPMXが読めて、モーションも読み込めた場合、キーチェック
        not_org_bones = []
        not_org_morphs = []
        not_rep_bones = []
        not_rep_morphs = []
        mismatch_bones = []

        motion = self.motion_vmd_file_ctrl.data
        org_pmx = self.org_model_file_ctrl.data
        rep_pmx = self.rep_model_file_ctrl.data

        if not motion or not org_pmx or not rep_pmx:
            # どれか読めてなければそのまま終了
            return True

        if motion.motion_cnt == 0:
            logger.warning("%s骨骼或表情动作数据中没有关键帧。", display_set_no, decoration=MLogger.DECORATION_BOX)
            return True

        result = True
        is_warning = False

        # ボーン
        for k in motion.bones.keys():
            bone_fnos = motion.get_bone_fnos(k)
            for fno in bone_fnos:
                if motion.bones[k][fno].position != MVector3D() or motion.bones[k][fno].rotation != MQuaternion():
                    # キーが存在しており、かつ初期値ではない値が入っている場合、警告対象

                    if k not in org_pmx.bones:
                        not_org_bones.append(k)

                    if k not in rep_pmx.bones:
                        not_rep_bones.append(k)
                    
                    if k in org_pmx.bones and k in rep_pmx.bones:
                        mismatch_types = []
                        # 両方にボーンがある場合、フラグが同じであるかチェック
                        if org_pmx.bones[k].getRotatable() != rep_pmx.bones[k].getRotatable():
                            mismatch_types.append("性能:旋转")
                        if org_pmx.bones[k].getTranslatable() != rep_pmx.bones[k].getTranslatable():
                            mismatch_types.append("性能:移动")
                        if org_pmx.bones[k].getIkFlag() != rep_pmx.bones[k].getIkFlag():
                            mismatch_types.append("性能:IK")
                        if org_pmx.bones[k].getVisibleFlag() != rep_pmx.bones[k].getVisibleFlag():
                            mismatch_types.append("性能:表示")
                        if org_pmx.bones[k].getManipulatable() != rep_pmx.bones[k].getManipulatable():
                            mismatch_types.append("性能:操作")
                        if org_pmx.bones[k].display != rep_pmx.bones[k].display:
                            mismatch_types.append("表示枠")

                        if len(mismatch_types) > 0:
                            mismatch_bones.append(f"{k} 　【差异】{', '.join(mismatch_types)}）")
                    
                    # 1件あればOK
                    break

        for k in motion.morphs.keys():
            morph_fnos = motion.get_morph_fnos(k)
            for fno in morph_fnos:
                if motion.morphs[k][fno].ratio != 0:
                    # キーが存在しており、かつ初期値ではない値が入っている場合、警告対象

                    if k not in org_pmx.morphs:
                        not_org_morphs.append(k)

                    if k not in rep_pmx.morphs:
                        not_rep_morphs.append(k)
                    
                    # 1件あればOK
                    break

        if len(not_org_bones) > 0 or len(not_org_morphs) > 0:
            logger.warning("%s%s中，缺少动作中使用的骨骼和表情。\n模型: %s\n缺少骨骼: %s\n缺少表情: %s", \
                           display_set_no, self.org_model_file_ctrl.title, org_pmx.name, ",".join(not_org_bones), ",".join(not_org_morphs), decoration=MLogger.DECORATION_BOX)
            is_warning = True

        if len(not_rep_bones) > 0 or len(not_rep_morphs) > 0:
            logger.warning("%s%s中，缺少动作中使用的骨骼和表情。\n模型: %s\n缺少骨骼: %s\n缺少表情: %s", \
                           display_set_no, self.rep_model_file_ctrl.title, rep_pmx.name, ",".join(not_rep_bones), ",".join(not_rep_morphs), decoration=MLogger.DECORATION_BOX)
            is_warning = True

        if len(mismatch_bones) > 0:
            logger.warning("%s%s中，动作中使用的骨骼的性能等不同。\n模型: %s\n不同的骨骼:\n　%s", \
                           display_set_no, self.rep_model_file_ctrl.title, rep_pmx.name, "\n　".join(mismatch_bones), decoration=MLogger.DECORATION_BOX)
            is_warning = True

        if not is_warning:
            logger.info("在动作中被使用的骨骼和表情都有。", decoration=MLogger.DECORATION_BOX, title="完成")

        return result

    def is_loaded(self):
        result = True
        if self.is_valid():
            result = self.motion_vmd_file_ctrl.data and result
            result = self.org_model_file_ctrl.data and result
            result = self.rep_model_file_ctrl.data and result
        else:
            result = False
        
        return result

    def load(self):
        result = True
        try:
            result = self.motion_vmd_file_ctrl.load() and result
            result = self.org_model_file_ctrl.load() and result
            result = self.rep_model_file_ctrl.load() and result
        except Exception:
            result = False
        
        return result

    # VMD出力ファイルパス生成
    def set_output_vmd_path(self, event, is_force=False):
        output_vmd_path = MFileUtils.get_output_vmd_path(
            self.motion_vmd_file_ctrl.file_ctrl.GetPath(),
            self.rep_model_file_ctrl.file_ctrl.GetPath(),
            self.org_model_file_ctrl.title_parts_ctrl.GetValue(),
            self.rep_model_file_ctrl.title_parts_ctrl.GetValue(),
            self.frame.arm_panel_ctrl.arm_process_flg_avoidance.GetValue(),
            self.frame.arm_panel_ctrl.arm_process_flg_alignment.GetValue(),
            (self.set_no in self.frame.morph_panel_ctrl.morph_set_dict and self.frame.morph_panel_ctrl.morph_set_dict[self.set_no].is_set_morph()) \
            or (self.set_no in self.frame.morph_panel_ctrl.bulk_morph_set_dict and len(self.frame.morph_panel_ctrl.bulk_morph_set_dict[self.set_no]) > 0),
            self.output_vmd_file_ctrl.file_ctrl.GetPath(), is_force)

        self.output_vmd_file_ctrl.file_ctrl.SetPath(output_vmd_path)

        if len(output_vmd_path) >= 255 and os.name == "nt":
            logger.error("预定生成的文件路径超过了Windows的限制。\n预定生成路径: {0}".format(output_vmd_path), decoration=MLogger.DECORATION_BOX)

