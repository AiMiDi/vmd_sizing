# -*- coding: utf-8 -*-
#
import os
import wx

from form.panel.BasePanel import BasePanel
from form.parts.SizingFileSet import SizingFileSet
from form.parts.BaseFilePickerCtrl import BaseFilePickerCtrl
from form.parts.HistoryFilePickerCtrl import HistoryFilePickerCtrl
from form.parts.FloatSliderCtrl import FloatSliderCtrl
from utils import MFileUtils
from utils.MLogger import MLogger # noqa

logger = MLogger(__name__)


class CameraPanel(BasePanel):
        
    def __init__(self, frame: wx.Frame, parent: wx.Notebook, tab_idx: int):
        super().__init__(frame, parent, tab_idx)

        self.header_panel = CameraHeaderPanel(self.frame, self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.header_sizer = wx.BoxSizer(wx.VERTICAL)

        self.description_txt = wx.StaticText(self.header_panel, wx.ID_ANY, u"您可以同时调整选定的相机动作的尺寸。\n" \
                                             + "全长偏移Y可以指定调整相机中显示的转换目标机型的全长的偏移值。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.header_sizer.Add(self.description_txt, 0, wx.ALL, 5)

        self.static_line01 = wx.StaticLine(self.header_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.header_sizer.Add(self.static_line01, 0, wx.EXPAND | wx.ALL, 5)

        camera_only_flg_spacer_ctrl = wx.StaticText(self.header_panel, wx.ID_ANY, u"　　　　　　　　　　　　　　　　　　　　　", wx.DefaultPosition, wx.DefaultSize, 0)

        # カメラサイジングのみ実行
        self.camera_only_flg_ctrl = wx.CheckBox(self.header_panel, wx.ID_ANY, u"カメラサイジングのみ実行", wx.DefaultPosition, wx.DefaultSize, 0)
        self.camera_only_flg_ctrl.SetToolTip(u"ボーンサイジング済みファイルを出力ファイルに指定した上でチェックを入れると、\nそのサイジング済みVMDを元にカメラサイジングを実行します。")
        self.camera_only_flg_ctrl.Bind(wx.EVT_CHECKBOX, self.set_output_vmd_path)

        # カメラVMDファイルコントロール
        self.camera_vmd_file_ctrl = HistoryFilePickerCtrl(self.frame, self.header_panel, u"相机动作VMD", u"打开相机动作VMD文件", ("vmd"), wx.FLP_DEFAULT_STYLE, \
                                                          u"请指定想要调整的相机动作的VMD路径。\n可通过拖拽指定、打开按钮指定、从历史记录中选择。", \
                                                          file_model_spacer=0, title_parts_ctrl=camera_only_flg_spacer_ctrl, title_parts2_ctrl=self.camera_only_flg_ctrl, file_histories_key="camera_vmd", \
                                                          is_change_output=True, is_aster=False, is_save=False, set_no=1)
        self.header_sizer.Add(self.camera_vmd_file_ctrl.sizer, 1, wx.EXPAND, 0)

        # 出力先VMDファイルコントロール
        self.output_camera_vmd_file_ctrl = BaseFilePickerCtrl(frame, self.header_panel, u"输出相机VMD", u"打开输出相机VMD文件", ("vmd"), wx.FLP_OVERWRITE_PROMPT | wx.FLP_SAVE | wx.FLP_USE_TEXTCTRL, \
                                                              u"请指定调整结果的相机VMD输出路径。\n根据相机VMD文件名自动生成，也可以变更为任意路径。", \
                                                              is_aster=False, is_save=True, set_no=1)
        self.header_sizer.Add(self.output_camera_vmd_file_ctrl.sizer, 1, wx.EXPAND, 0)

        # カメラ距離調整スライダー
        self.camera_length_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.camera_length_txt = wx.StaticText(self.header_panel, wx.ID_ANY, u"距离可动范围", wx.DefaultPosition, wx.DefaultSize, 0)
        self.camera_length_txt.SetToolTip(u"根据舞台的大小等，想要限制照相机的距离调整范围的情况下\n" \
                                          + "可以限定照相机的距离可动范围。\n" \
                                          + "也可以手动调整可动范围。")
        self.camera_length_txt.Wrap(-1)
        self.camera_length_sizer.Add(self.camera_length_txt, 0, wx.ALL, 5)

        self.camera_length_type_ctrl = wx.Choice(self.header_panel, id=wx.ID_ANY, choices=["距离限制强", "距离限制弱", "无距离限制"])
        self.camera_length_type_ctrl.SetSelection(2)
        self.camera_length_type_ctrl.Bind(wx.EVT_CHOICE, self.on_camera_length_type)
        self.camera_length_type_ctrl.SetToolTip(u"「距离限制强」　…　小舞台用。严格限制距离可动范围。\n" \
                                                + "「距离限制弱」　…　中等程度的舞台用。多少限制距离可动范围。\n" \
                                                + "「无距离限制」　…　将距离可动范围设为无限制，最大限度调整为与原机型相同的放映情况。")
        self.camera_length_sizer.Add(self.camera_length_type_ctrl, 0, wx.ALL, 5)

        self.camera_length_label = wx.StaticText(self.header_panel, wx.ID_ANY, u"（5）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.camera_length_label.SetToolTip(u"这是当前指定的相机距离的可动范围。")
        self.camera_length_label.Wrap(-1)
        self.camera_length_sizer.Add(self.camera_length_label, 0, wx.ALL, 5)

        self.camera_length_slider = FloatSliderCtrl(self.header_panel, wx.ID_ANY, 5, 1, 5, 0.01, self.camera_length_label, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.camera_length_slider.Bind(wx.EVT_SCROLL_CHANGED, self.set_output_vmd_path)
        self.camera_length_sizer.Add(self.camera_length_slider, 1, wx.ALL | wx.EXPAND, 5)

        self.header_sizer.Add(self.camera_length_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.header_panel.SetSizer(self.header_sizer)
        self.header_panel.Layout()
        self.sizer.Add(self.header_panel, 0, wx.EXPAND | wx.ALL, 5)

        # カメラセット(key: ファイルセット番号, value: カメラセット)
        self.camera_set_dict = {}
        # Bulk用カメラセット
        self.bulk_camera_set_dict = {}
        # カメラセット用基本Sizer
        self.set_list_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.scrolled_window = CameraScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, \
                                                    wx.FULL_REPAINT_ON_RESIZE | wx.VSCROLL | wx.ALWAYS_SHOW_SB)
        self.scrolled_window.SetScrollRate(5, 5)

        # スクロールバーの表示のためにサイズ調整
        self.scrolled_window.SetSizer(self.set_list_sizer)
        self.scrolled_window.Layout()
        self.sizer.Add(self.scrolled_window, 1, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 5)
        self.sizer.Layout()
        self.fit()

    def on_camera_length_type(self, event):
        if self.camera_length_type_ctrl.GetSelection() == 0:
            self.camera_length_slider.SetValue(1.05)
        elif self.camera_length_type_ctrl.GetSelection() == 1:
            self.camera_length_slider.SetValue(1.3)
        else:
            self.camera_length_slider.SetValue(5)
        
        self.set_output_vmd_path(event)

    def set_output_vmd_path(self, event, is_force=False):
        # カメラ出力パスを強制的に変更する
        self.header_panel.set_output_vmd_path(event, True)
    
    # カメラタブ初期化処理
    def initialize(self, event: wx.Event):
        self.bulk_camera_set_dict = {}
        
        if 1 not in self.camera_set_dict:
            # 空から作る場合、ファイルタブのファイルセット参照
            self.add_set(1, self.frame.file_panel_ctrl.file_set)
        else:
            # ある場合、モデル名だけ入替
            self.camera_set_dict[1].model_name_txt.SetLabel("{0} → {1}".format(\
                                                            self.frame.file_panel_ctrl.file_set.org_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1], \
                                                            self.frame.file_panel_ctrl.file_set.rep_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1]))
        
        # multiはあるだけ調べる
        for multi_file_set_idx, multi_file_set in enumerate(self.frame.multi_panel_ctrl.file_set_list):
            set_no = multi_file_set_idx + 2
            if set_no not in self.camera_set_dict:
                # 空から作る場合、複数タブのファイルセット参照
                self.add_set(set_no, multi_file_set)
            else:
                # ある場合、モデル名だけ入替
                self.camera_set_dict[set_no].model_name_txt.SetLabel("{0} → {1}".format(\
                                                                     multi_file_set.org_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1], \
                                                                     multi_file_set.rep_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1]))

    def add_set(self, set_idx: int, file_set: SizingFileSet):
        new_camera_set = CameraSet(self.frame, self, self.scrolled_window, set_idx, file_set)
        self.set_list_sizer.Add(new_camera_set.set_sizer, 0, wx.EXPAND | wx.ALL, 5)
        self.camera_set_dict[set_idx] = new_camera_set
        
        # スクロールバーの表示のためにサイズ調整
        self.set_list_sizer.Layout()
        self.set_list_sizer.FitInside(self.scrolled_window)

    # フォーム無効化
    def disable(self):
        self.file_set.disable()

    # フォーム無効化
    def enable(self):
        self.file_set.enable()

    def save(self):
        self.camera_vmd_file_ctrl.save()


class CameraScrolledWindow(wx.ScrolledWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    # 複数モーション用カメラの場合、出力パスは変わらないのでスルー
    def set_output_vmd_path(self, event: wx.Event, is_force=False):
        pass


class CameraHeaderPanel(wx.Panel):

    def __init__(self, frame, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, name=name)

        self.parent = parent
        self.frame = frame

    # ファイル変更時の処理
    def on_change_file(self, event: wx.Event):
        self.set_output_vmd_path(event)
    
    def set_output_vmd_path(self, event, is_force=False):
        output_camera_vmd_path = MFileUtils.get_output_camera_vmd_path(
            self.parent.camera_vmd_file_ctrl.file_ctrl.GetPath(),
            self.frame.file_panel_ctrl.file_set.rep_model_file_ctrl.file_ctrl.GetPath(),
            self.parent.output_camera_vmd_file_ctrl.file_ctrl.GetPath(),
            self.parent.camera_length_slider.GetValue(), is_force)

        self.parent.output_camera_vmd_file_ctrl.file_ctrl.SetPath(output_camera_vmd_path)

        if len(output_camera_vmd_path) >= 255 and os.name == "nt":
            logger.error("预定生成的文件路径超过了Windows的限制。\n预定生成路径: {0}".format(output_camera_vmd_path), decoration=MLogger.DECORATION_BOX)
        

class CameraSet():

    def __init__(self, frame: wx.Frame, panel: wx.Panel, window: wx.Window, set_idx: int, file_set: SizingFileSet):
        self.frame = frame
        self.panel = panel
        self.window = window
        self.set_idx = set_idx
        self.file_set = file_set

        self.set_sizer = wx.StaticBoxSizer(wx.StaticBox(self.window, wx.ID_ANY, "【No.{0}】".format(set_idx)), orient=wx.VERTICAL)

        self.model_name_txt = wx.StaticText(self.window, wx.ID_ANY, \
                                            "{0} → {1}".format(file_set.org_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1], \
                                                               file_set.rep_model_file_ctrl.file_model_ctrl.txt_ctrl.GetValue()[1:-1]), wx.DefaultPosition, wx.DefaultSize, 0)
        self.model_name_txt.Wrap(-1)
        self.set_sizer.Add(self.model_name_txt, 0, wx.ALL, 5)

        # カメラPMXファイルコントロール
        self.camera_model_file_ctrl = HistoryFilePickerCtrl(frame, window, u"相机原型PMX", u"打开相机原型PMX文件", ("pmx"), wx.FLP_DEFAULT_STYLE, \
                                                            u"请指定相机制作所用模型的PMX路径。\n未指定时，使用动作制作原模型PMX。" \
                                                            + "\n精度虽然下降，但也可以用类似尺寸、骨架结构的模型来代替。\n可通过拖拽指定、打开按钮指定、从历史记录中选择。", \
                                                            file_model_spacer=20, title_parts_ctrl=None, title_parts2_ctrl=None, file_histories_key="camera_pmx", \
                                                            is_change_output=True, is_aster=False, is_save=False, set_no=set_idx)
        self.set_sizer.Add(self.camera_model_file_ctrl.sizer, 1, wx.EXPAND, 0)

        self.offset_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.camera_offset_y_txt = wx.StaticText(self.window, wx.ID_ANY, u"全长Y偏移", wx.DefaultPosition, wx.DefaultSize, 0)
        self.camera_offset_y_txt.Wrap(-1)
        self.offset_sizer.Add(self.camera_offset_y_txt, 0, wx.ALL, 5)

        # オフセットYコントロール
        self.camera_offset_y_ctrl = wx.SpinCtrlDouble(self.window, id=wx.ID_ANY, size=wx.Size(100, -1), value="0.0", min=-1000, max=1000, initial=0.0, inc=0.1)
        self.camera_offset_y_ctrl.SetToolTip(u"您可以指定调整相机中的目标型号的全长的偏移值。\n" \
                                             + "发饰等“想要排除在头顶以上的对象”时，请指定负值。\n" \
                                             + "如果想包含在头顶以上的对象，请指定正值。")
        self.camera_offset_y_ctrl.Bind(wx.EVT_MOUSEWHEEL, lambda event: self.frame.on_wheel_spin_ctrl(event, 0.2))
        self.offset_sizer.Add(self.camera_offset_y_ctrl, 0, wx.ALL, 5)

        self.set_sizer.Add(self.offset_sizer, 0, wx.ALL, 0)


