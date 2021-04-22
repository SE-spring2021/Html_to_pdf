# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\appgui.py'],
             pathex=['D:\\ComputerScience\\MyCourses\\GSU\\2021-spring\\6350-002-SOFTWARE ENGINEERING\\Project\\Repo\\Html_to_pdf'],
             binaries=[],
             datas=[('src/appgui.kv', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='appgui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='appgui')
