@echo off
rem --- 
rem ---  exe�𐶐�
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

rem activate vmdsizing_cython_exe1 && src\setup_install.bat && pyinstaller --clean vmdising_np64.spec

pyinstaller --clean vmdising_np64.spec

