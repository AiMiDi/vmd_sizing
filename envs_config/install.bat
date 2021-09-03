conda create -y -n vmdsizing_cython python=3.8
cd /d %~dp0
activate vmdsizing_cython  && pip install cython  && pip install numpy  && pip install wxpython  && pip install numpy-quaternion  && pip install bezier  && pip install pypiwin32
conda install pyinstaller