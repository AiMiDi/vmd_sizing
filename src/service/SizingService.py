# -*- coding: utf-8 -*-
#

import logging
import os
from pathlib import Path

from mmd.PmxData import PmxModel
from mmd.VmdWriter import VmdWriter
from mmd.VmdReader import VmdReader
from module.MOptions import MOptions, MOptionsDataSet
from service.parts.MoveService import MoveService
from service.parts.StanceService import StanceService
from service.parts.ArmAlignmentService import ArmAlignmentService
from service.parts.ArmAvoidanceService import ArmAvoidanceService
from service.parts.MorphService import MorphService
from service.parts.CameraService import CameraService
from utils import MServiceUtils
from utils.MException import SizingException, MKilledException
from utils.MLogger import MLogger # noqa

logger = MLogger(__name__)


class SizingService():
    def __init__(self, options: MOptions):
        self.options = options

    def execute(self):
        logging.basicConfig(level=self.options.logging_level, format="%(message)s [%(module_name)s]")

        try:
            service_data_txt = "VMD尺寸处理执行\n------------------------\nexe版本: {version_name}\n".format(version_name=self.options.version_name)

            for data_set_idx, data_set in enumerate(self.options.data_set_list):
                service_data_txt = "{service_data_txt}\n【No.{no}】 --------- \n".format(service_data_txt=service_data_txt, no=(data_set_idx+1)) # noqa
                service_data_txt = "{service_data_txt}　　动作: {motion}\n".format(service_data_txt=service_data_txt,
                                        motion=os.path.basename(data_set.motion.path)) # noqa
                service_data_txt = "{service_data_txt}　　创建模型: {trace_model} ({model_name})\n".format(service_data_txt=service_data_txt,
                                        trace_model=os.path.basename(data_set.org_model.path), model_name=data_set.org_model.name) # noqa
                service_data_txt = "{service_data_txt}　　目标模型: {replace_model} ({model_name})\n".format(service_data_txt=service_data_txt,
                                        replace_model=os.path.basename(data_set.rep_model.path), model_name=data_set.rep_model.name) # noqa
                if data_set.camera_org_model:
                    service_data_txt = "{service_data_txt}　　相机原型: {trace_model} ({model_name})\n".format(service_data_txt=service_data_txt,
                                            trace_model=os.path.basename(data_set.camera_org_model.path), model_name=data_set.camera_org_model.name) # noqa
                    service_data_txt = "{service_data_txt}　　Y偏移: {camera_offset_y}\n".format(service_data_txt=service_data_txt,
                                            camera_offset_y=data_set.camera_offset_y) # noqa
                service_data_txt = "{service_data_txt}　　有无站姿追加修正: {detail_stance_flg}\n".format(service_data_txt=service_data_txt,
                                        detail_stance_flg=data_set.detail_stance_flg) # noqa
                if data_set.detail_stance_flg:
                    # スタンス追加補正がある場合、そのリストを表示
                    service_data_txt = "{service_data_txt}　　　　{detail_stance_flg}\n".format(service_data_txt=service_data_txt,
                                            detail_stance_flg=", ".join(data_set.selected_stance_details)) # noqa
                    
                service_data_txt = "{service_data_txt}　　有无分散旋转骨: {twist_flg}\n".format(service_data_txt=service_data_txt,
                                        twist_flg=data_set.twist_flg) # noqa

                morph_list = []
                for (org_morph_name, rep_morph_name, morph_ratio) in data_set.morph_list:
                    morph_list.append(f"{org_morph_name} → {rep_morph_name} ({morph_ratio})")
                morph_txt = ", ".join(morph_list)
                service_data_txt = "{service_data_txt}　　表情替换: {morph_txt}\n".format(service_data_txt=service_data_txt,
                                        morph_txt=morph_txt) # noqa

                if data_set_idx in self.options.arm_options.avoidance_target_list:
                    service_data_txt = "{service_data_txt}　　对象刚性名称: {avoidance_target}\n".format(service_data_txt=service_data_txt,
                                            avoidance_target=", ".join(self.options.arm_options.avoidance_target_list[data_set_idx])) # noqa

            service_data_txt = "{service_data_txt}\n--------- \n".format(service_data_txt=service_data_txt) # noqa

            if self.options.arm_options.avoidance:
                service_data_txt = "{service_data_txt}避免刚体接触: {avoidance}\n".format(service_data_txt=service_data_txt,
                                        avoidance=self.options.arm_options.avoidance) # noqa

            if self.options.arm_options.alignment:
                service_data_txt = "{service_data_txt}手腕对准位置: {alignment} ({distance})\n".format(service_data_txt=service_data_txt,
                                        alignment=self.options.arm_options.alignment, distance=self.options.arm_options.alignment_distance_wrist) # noqa
                service_data_txt = "{service_data_txt}手指位置对齐: {alignment} ({distance})\n".format(service_data_txt=service_data_txt,
                                        alignment=self.options.arm_options.alignment_finger_flg, distance=self.options.arm_options.alignment_distance_finger) # noqa
                service_data_txt = "{service_data_txt}地板对齐: {alignment} ({distance})\n".format(service_data_txt=service_data_txt,
                                        alignment=self.options.arm_options.alignment_floor_flg, distance=self.options.arm_options.alignment_distance_floor) # noqa
            
            if self.options.arm_options.arm_check_skip_flg:
                service_data_txt = "{service_data_txt}跳过手臂检查: {arm_check_skip}\n".format(service_data_txt=service_data_txt,
                                        arm_check_skip=self.options.arm_options.arm_check_skip_flg) # noqa

            if self.options.camera_motion:
                service_data_txt = "{service_data_txt}摄相机: {camera}({camera_length})\n".format(service_data_txt=service_data_txt,
                                        camera=os.path.basename(self.options.camera_motion.path), camera_length=self.options.camera_length) # noqa
                service_data_txt = "{service_data_txt}　　距离限制: {camera_length}{camera_length_umlimit}\n".format(service_data_txt=service_data_txt,
                                        camera_length=self.options.camera_length, camera_length_umlimit=("" if self.options.camera_length < 5 else "(无限制)")) # noqa

            service_data_txt = "{service_data_txt}------------------------".format(service_data_txt=service_data_txt) # noqa

            if self.options.total_process_ctrl:
                self.options.total_process_ctrl.write(str(self.options.total_process))
                self.options.now_process_ctrl.write("0")
                self.options.now_process_ctrl.write(str(self.options.now_process))

            logger.info(service_data_txt, decoration=MLogger.DECORATION_BOX)

            if self.options.is_sizing_camera_only is True:
                # カメラサイジングのみ実行する場合、出力結果VMDを読み込む
                for data_set_idx, data_set in enumerate(self.options.data_set_list):
                    reader = VmdReader(data_set.output_vmd_path)
                    data_set.motion = reader.read_data()
            else:
                for data_set_idx, data_set in enumerate(self.options.data_set_list):
                    # 足IKのXYZの比率
                    data_set.original_xz_ratio, data_set.original_y_ratio, data_set.original_heads_tall_ratio = MServiceUtils.calc_leg_ik_ratio(data_set)
                
                # 足IKの比率再計算
                self.options.calc_leg_ratio()

                # 移動補正
                if not MoveService(self.options).execute():
                    return False

                # スタンス補正
                if not StanceService(self.options).execute():
                    return False

                # 剛体接触回避
                if self.options.arm_options.avoidance:
                    if not ArmAvoidanceService(self.options).execute():
                        return False

                # 手首位置合わせ
                if self.options.arm_options.alignment:
                    if not ArmAlignmentService(self.options).execute():
                        return False

            # カメラ補正
            if self.options.camera_motion:
                if not CameraService(self.options).execute():
                    return False

            if self.options.is_sizing_camera_only is False:
                # モーフ置換
                if not MorphService(self.options).execute():
                    return False
                
                for data_set_idx, data_set in enumerate(self.options.data_set_list):
                    # 実行後、出力ファイル存在チェック
                    try:
                        # 出力
                        VmdWriter(data_set).write()

                        Path(data_set.output_vmd_path).resolve(True)

                        logger.info("【No.%s】 导出完成: %s", (data_set_idx + 1), os.path.basename(
                            data_set.output_vmd_path), decoration=MLogger.DECORATION_BOX, title="サイジング成功")
                    except FileNotFoundError as fe:
                        logger.error("【No.%s】输出VMD文件好像没有正常导出。\n请检查路径。%s\n\n%s", (data_set_idx + 1),
                                     data_set.output_vmd_path, fe, decoration=MLogger.DECORATION_BOX)
                
            if self.options.camera_motion:
                try:
                    camera_model = PmxModel()
                    camera_model.name = "カメラ・照明"
                    data_set = MOptionsDataSet(self.options.camera_motion, None, camera_model, self.options.camera_output_vmd_path, 0, 0, [], None, 0, [])
                    # 出力
                    VmdWriter(data_set).write()

                    Path(data_set.output_vmd_path).resolve(True)

                    logger.info("摄像机导出完成: %s", os.path.basename(data_set.output_vmd_path), decoration=MLogger.DECORATION_BOX, title="计算成功")
                except FileNotFoundError as fe:
                    logger.error("摄相机输出VMD文件好像没有正常导出。\n请确认路径。%s\n\n%s", self.options.camera_output_vmd_path, fe, decoration=MLogger.DECORATION_BOX)

            if int(self.options.total_process) != int(self.options.now_process):
                logger.warning("部分处理跳过。\n单击画面左下角的进度数，则以灰色显示跳过的处理。", decoration=MLogger.DECORATION_BOX)

            return True
        except MKilledException:
            return False
        except SizingException as se:
            logger.error("无法处理尺寸调整数据结束。\n\n%s", se, decoration=MLogger.DECORATION_BOX)
            return False
        except Exception as e:
            logger.critical("处理以意外错误结束。", e, decoration=MLogger.DECORATION_BOX)
            return False
        finally:
            logging.shutdown()
