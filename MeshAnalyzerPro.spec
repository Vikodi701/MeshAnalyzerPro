# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

block_cipher = None
project_dir = Path(SPECPATH)
icon_file = project_dir / 'assets' / 'icons' / 'app.ico'

a = Analysis(
    ['main.py'],
    pathex=[str(project_dir)],
    binaries=[],
    datas=[
        (str(project_dir / 'assets'), 'assets'),
        (str(project_dir / 'themes'), 'themes'),
        (str(project_dir / 'config'), 'config'),
        (str(project_dir / 'help'), 'help'),
        (str(project_dir / 'languages'), 'languages'),
        (str(project_dir / 'assets' / 'icons' / 'app.ico'), '.'),
        (str(project_dir / 'assets' / 'icons' / 'app.png'), '.'),
    ],
    hiddenimports=[
        'PySide6.QtSvg',
        'PySide6.QtSvgWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MeshAnalyzerPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(icon_file),
)
