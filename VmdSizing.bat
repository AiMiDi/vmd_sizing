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


rem ---  �g���[�X�����f��PMX�t�@�C��
echo --------------
set MODEL_PMX=born\���ɂ܂����~�N���W��.csv
echo �g���[�X�����f����PMX�t�@�C���̑��΃p�X����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�u%MODEL_PMX%�v�̃t�@�C����ǂݍ��݂܂��B
set /P MODEL_PMX="���g���[�X�����f��PMX�t�@�C��: "

rem ---  �g���[�X�ϊ��惂�f��PMX�t�@�C��
echo --------------
set REPLACE_MODEL_PMX=born\���ɂ܂����~�N���W��.csv
echo �g���[�X�ϊ��惂�f����PMX�t�@�C���̑��΃p�X����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�u%REPLACE_MODEL_PMX%�v�̃t�@�C����ǂݍ��݂܂��B
set /P REPLACE_MODEL_PMX="���g���[�X�ϊ��惂�f��PMX�t�@�C��: "


rem ---  ���_���L��

echo --------------
echo �����Ƙr�̒��_������s�����Ayes �� no ����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A���_������s���܂���B
set AVOIDANCE=0
set IS_AVOIDANCE=no
set /P IS_AVOIDANCE="�����_�������[yes/no]: "

IF /I "%IS_AVOIDANCE%" EQU "yes" (
    set AVOIDANCE=1
)

rem ---  �ڍ׃��O�L��

echo --------------
echo �ڍׂȃ��O���o�����Ayes �� no ����͂��ĉ������B
echo �������͂����AENTER�����������ꍇ�A�ʏ탍�O���o�͂��܂��B
set VERBOSE=2
set IS_DEBUG=no
set /P IS_DEBUG="���ڍ׃��O[yes/no]: "

IF /I "%IS_DEBUG%" EQU "yes" (
    set VERBOSE=3
)

rem ---  python ���s
python src/main.py --vmd_path %INPUT_VMD% --trace_pmx_path %MODEL_PMX% --replace_pmx_path %REPLACE_MODEL_PMX% --avoidance %AVOIDANCE% --verbose %VERBOSE%


