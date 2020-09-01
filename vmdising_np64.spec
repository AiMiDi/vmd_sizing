# -*- coding: utf-8 -*-
# -*- mode: python -*-
# VMDサイジング 64bit版

block_cipher = None


a = Analysis(['src\\executor.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['wx._adv', 'wx._html', 'pkg_resources.py2_warn', 'bezier', 'quaternion'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['mkl','libopenblas', 'tkinter', 'pkg_resources', 'win32comgenpy', 'traitlets', 'PIL', 'IPython', 'xml', 'pydoc'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('.\\src\\vmdsizing.ico','.\\src\\vmdsizing.ico', 'Data')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VmdSizing_5.01_β12_64bit',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='.\\src\\vmdsizing.ico')

