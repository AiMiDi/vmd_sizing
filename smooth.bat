@echo off
rem --- 
rem ---  �X���[�W���O
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

set MOTION_PATH="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�����tIII �Ȃ�\nac_aikotoba3_300-468_��Ԏ��~�N_���W��_T_20200917_222601.vmd"
set MODEL_PATH=D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\��Ԏ��~�N\��Ԏ��~�N_���W��.pmx
set LOOP_CNT=2
set INTERPOLATION=0
set BONE_LIST="�E�r;�E�r��;�E�Ђ�;�E�蝀;�E���;���r;���r��;���Ђ�;���蝀;�����;"
rem set BONE_LIST="�E�Ђ�"
rem set BONE_LIST="�E�r"
rem set BONE_LIST="�����"

set VERBOSE="10"


activate vmdsizing_cython && src\setup.bat && python src/executor_smooth.py --motion_path %MOTION_PATH%  --model_path %MODEL_PATH%  --loop_cnt %LOOP_CNT%  --interpolation %INTERPOLATION%  --bone_list %BONE_LIST% --verbose %VERBOSE% 


