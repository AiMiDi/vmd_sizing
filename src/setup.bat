cls

cd /d %~dp0

rem -- �s�v���t�@�C���p
kernprof -l setup.py build_ext --inplace


rem -- �ʏ�p
rem python setup.py build_ext --inplace

cd ..
