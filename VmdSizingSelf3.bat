@echo off
rem --- 
rem ---  vmd�f�[�^�̃g���[�X���f����ϊ�
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

set VMD_PATH="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�����tIII �Ȃ�\nac_aikotoba3_0-500_���쒆�S.vmd"
rem set VMD_PATH="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�����tIII �Ȃ�\nac_aikotoba3.vmd"
set TRACE_PMX_PATH="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\��Ԏ��~�N\��Ԏ��~�N_���W��.pmx"
set REPLACE_PMX_PATH="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N_�����΂����l�g���[�X���f���z�z v1.07\Tda�������~�N_�����΂���M�g���[�X���f��v1.07.pmx"
set ALTERNATIVE_MODEL=1
set NO_DELEGATE=0

set AVOIDANCE=0
set AVOIDANCE_FINGER=0
set HAND_IK=0
set HAND_DISTANCE=0
set FLOOR_HAND=0
set FLOOR_HAND_UP=0
set FLOOR_HAND_DOWN=0
set HAND_FLOOR_DISTANCE=0
set LEG_FLOOR_DISTANCE=0
set FINGER_IK=0
set FINGER_DISTANCE=0
set VMD_CHOICE_VALUES=
set REP_CHOICE_VALUES=
set REP_RATE_VALUES=
set CAMERA_VMD_PATH=
set CAMERA_PMX_PATH=
set CAMERA_Y_OFFSET=0
set TARGET_AVOIDANCE_RIGIDS=
set TARGET_AVOIDANCE_BONES=
set TEST_PARAM=
set VERBOSE=2

python src\wrapper.py --vmd_path %VMD_PATH% --trace_pmx_path %TRACE_PMX_PATH% --replace_pmx_path %REPLACE_PMX_PATH% --avoidance "%AVOIDANCE%" --avoidance_finger "%AVOIDANCE_FINGER%" --hand_ik "%HAND_IK%" --hand_distance "%HAND_DISTANCE%" --floor_hand "%FLOOR_HAND%" --floor_hand_up "%FLOOR_HAND_UP%" --floor_hand_down "%FLOOR_HAND_DOWN%" --hand_floor_distance "%HAND_FLOOR_DISTANCE%" --leg_floor_distance "%LEG_FLOOR_DISTANCE%" --finger_ik "%FINGER_IK%" --finger_distance "%FINGER_DISTANCE%" --vmd_choice_values "%VMD_CHOICE_VALUES%" --rep_choice_values "%REP_CHOICE_VALUES%" --rep_rate_values "%REP_RATE_VALUES%" --camera_vmd_path "%CAMERA_VMD_PATH%" --camera_pmx_path "%CAMERA_PMX_PATH%" --camera_y_offset "%CAMERA_Y_OFFSET%" --output_path "%OUTPUT_PATH%" --alternative_model "%ALTERNATIVE_MODEL%" --no_delegate "%NO_DELEGATE%" --target_avoidance_rigids "%TARGET_AVOIDANCE_RIGIDS%" --target_avoidance_bones "%TARGET_AVOIDANCE_BONES%" --test_param "%TEST_PARAM%" --verbose "%VERBOSE%" --output_path ""

