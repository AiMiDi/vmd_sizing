@echo off
rem --- 
rem ---  VMD�T�C�W���O�̃e�X�g�P�[�X���s����
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

rem ---  python ���s
python test/test_utils.py
python test/test_arm_ik.py
python test/test_morph.py

