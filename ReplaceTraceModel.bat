@echo off
rem --- 
rem ---  vmd�f�[�^�̃g���[�X���f����ϊ�
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

rem ---  ����vmd�t�@�C���p�X
echo ��������vmd�t�@�C���̃t���p�X���w�肵�ĉ������B
echo ���̐ݒ�͕K�{���ڂł��B
set INPUT_VMD=
set /P INPUT_VMD=�������Ώ�vmd�t�@�C���p�X: 
rem echo INPUT_VMD�F%INPUT_VMD%

IF /I "%INPUT_VMD%" EQU "" (
    ECHO �����Ώ�vmd�t�@�C���p�X���ݒ肳��Ă��Ȃ����߁A�����𒆒f���܂��B
    EXIT /B
)


rem ---  �g���[�X�����f���{�[���\��CSV�t�@�C��
echo --------------
set MODEL_BONE_CSV=born\���ɂ܂����~�N���W��.csv
echo �g���[�X�����f���̃{�[���\��CSV�t�@�C���̑��΃p�X����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�u%MODEL_BONE_CSV%�v�̃t�@�C����ǂݍ��݂܂��B
set /P MODEL_BONE_CSV="���g���[�X�����f���{�[���\��CSV�t�@�C��: "

rem ---  �g���[�X�ϊ��惂�f���{�[���\��CSV�t�@�C��
echo --------------
set REPLACE_MODEL_BONE_CSV=born\���ɂ܂����~�N���W��.csv
echo �g���[�X�ϊ��惂�f���̃{�[���\��CSV�t�@�C���̑��΃p�X����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�u%REPLACE_MODEL_BONE_CSV%�v�̃t�@�C����ǂݍ��݂܂��B
set /P REPLACE_MODEL_BONE_CSV="���g���[�X�ϊ��惂�f���{�[���\��CSV�t�@�C��: "


rem rem ---  �g���[�X�ϊ��惂�f�����_�\��CSV�t�@�C��
rem echo --------------
set REPLACE_MODEL_VERTEX_CSV=%REPLACE_MODEL_BONE_CSV:born=vertex%
rem echo �g���[�X�ϊ��惂�f���̒��_�\��CSV�t�@�C���̑��΃p�X����͂��ĉ������B
rem echo �������͂����AENTER�����������ꍇ�A�u%REPLACE_MODEL_VERTEX_CSV%�v�̃t�@�C����ǂݍ��݂܂��B
rem set /P REPLACE_MODEL_VERTEX_CSV="���g���[�X�ϊ��惂�f�����_�\��CSV�t�@�C��: "


rem ---  �ڍ׃��O�L��

echo --------------
echo �ڍׂȃ��O���o�����Ayes �� no ����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�ʏ탍�O���o�͂��܂��B
set VERBOSE=2
set IS_DEBUG=yes
set /P IS_DEBUG="���ڍ׃��O[yes/no]: "

IF /I "%IS_DEBUG%" EQU "yes" (
    set VERBOSE=3
)

rem ---  python ���s
python src/main.py --vmd_path %INPUT_VMD% --trace_bone_path %MODEL_BONE_CSV% --replace_bone_path %REPLACE_MODEL_BONE_CSV% --replace_vertex_path %REPLACE_MODEL_VERTEX_CSV% --verbose %VERBOSE%


