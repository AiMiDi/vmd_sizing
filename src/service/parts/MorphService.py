# -*- coding: utf-8 -*-
#
import os
import copy

from mmd.VmdData import VmdMorphFrame
from module.MMath import MRect, MVector3D, MVector4D, MQuaternion, MMatrix4x4 # noqa
from module.MOptions import MOptions, MOptionsDataSet
from utils import MServiceUtils, MBezierUtils # noqa
from utils.MLogger import MLogger # noqa
from utils.MException import SizingException, MKilledException


logger = MLogger(__name__)


class MorphService():
    def __init__(self, options: MOptions):
        self.options = options

    def execute(self):
        for data_set_idx, data_set in enumerate(self.options.data_set_list):
            if data_set.motion.morph_cnt <= 0 or len(data_set.morph_list) == 0:
                # モーフデータが無い場合、或いは置換データが無い場合、処理スキップ
                continue

            logger.info("表情替换　【No.%s】", (data_set_idx + 1), decoration=MLogger.DECORATION_LINE)

            self.replace_morph(data_set_idx, data_set)

            if self.options.now_process_ctrl:
                self.options.now_process += 1
                self.options.now_process_ctrl.write(str(self.options.now_process))

                proccess_key = "【No.{0}】{1}({2})".format(data_set_idx + 1, os.path.basename(data_set.motion.path), data_set.rep_model.name)
                self.options.tree_process_dict[proccess_key]["表情替换"] = True

        return True

    # 表情替换実行
    def replace_morph(self, data_set_idx: int, data_set: MOptionsDataSet):
        try:
            # 置換前のモーフリスト
            original_morphs = {}
            # 置換後のモーフリスト
            replaced_morphs = {}

            for (org_morph_name, rep_morph_name, morph_ratio) in data_set.morph_list:
                if org_morph_name in data_set.motion.morphs:
                    # 置換元モーフがある場合、保持
                    original_morphs[org_morph_name] = copy.deepcopy(data_set.motion.morphs[org_morph_name])

                if rep_morph_name in data_set.motion.morphs and org_morph_name != rep_morph_name:
                    # 置換先モーフがある場合、保持（元と先が同じ場合、スルー）
                    replaced_morphs[rep_morph_name] = copy.deepcopy(data_set.motion.morphs[rep_morph_name])
            
            # 保持したので、モーフ削除
            for (org_morph_name, rep_morph_name, morph_ratio) in data_set.morph_list:
                if org_morph_name in data_set.motion.morphs:
                    del data_set.motion.morphs[org_morph_name]
                
                if rep_morph_name in data_set.motion.morphs:
                    del data_set.motion.morphs[rep_morph_name]

            for (org_morph_name, rep_morph_name, morph_ratio) in data_set.morph_list:
                if org_morph_name in original_morphs and rep_morph_name not in replaced_morphs:
                    # 元にあって、先にない場合、置換元を置換先の名前で登録
                    for fno, org_morph_data in original_morphs[org_morph_name].items():
                        morph_data = VmdMorphFrame(fno)
                        # 名前を置き換える
                        morph_data.set_name(rep_morph_name)

                        # 大きさに比率をかける
                        morph_data.ratio = org_morph_data.ratio * morph_ratio

                        if rep_morph_name not in replaced_morphs:
                            replaced_morphs[rep_morph_name] = {}

                        # 置換後モーフデータを設定
                        replaced_morphs[rep_morph_name][fno] = morph_data
            
                elif org_morph_name in original_morphs and rep_morph_name in replaced_morphs:
                    # 元にあって、先にもある場合
                    for fno, org_morph_data in original_morphs[org_morph_name].items():
                        morph_data = VmdMorphFrame(fno)

                        # 名前を置き換える
                        morph_data.set_name(rep_morph_name)

                        # 大きさに比率をかける
                        morph_data.ratio = org_morph_data.ratio * morph_ratio

                        if fno in replaced_morphs[rep_morph_name]:
                            # 既に対象fnoが登録されている場合、加算して登録
                            morph_data.ratio += replaced_morphs[rep_morph_name][fno].ratio

                        # 置換後モーフデータを追加
                        replaced_morphs[rep_morph_name][fno] = morph_data

                logger.info("表情替换 %s → %s (%s)【No.%s】", org_morph_name, rep_morph_name, morph_ratio, (data_set_idx + 1))
            
            # 置換が全部終わったら、再登録
            for new_rep_morph_name, new_rep_morph_data in replaced_morphs.items():
                data_set.motion.morphs[new_rep_morph_name] = new_rep_morph_data
        except MKilledException as ke:
            raise ke
        except SizingException as se:
            logger.error("无法处理表情替换的数据结束。\n\n%s", se.message)
            return se
        except Exception as e:
            import traceback
            logger.error("表情替换处理以意外错误结束。\n\n%s", traceback.format_exc())
            raise e


