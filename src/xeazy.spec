# -*- mode: python -*-

block_cipher = None


a = Analysis(['xeazy.py'],
             pathex=['./'],
             binaries=[],
             datas=[('templates/assets/sass/paper/mixins/*', 'templates/assets/sass/paper/mixins/.'), ('templates/assets/sass/paper/*', 'templates/assets/sass/paper/.'), ('templates/assets/sass/*', 'templates/assets/sass/.'), ('templates/assets/img/faces/*', 'templates/assets/img/faces/.'), ('templates/assets/img/*', 'templates/assets/img/.'), ('templates/assets/js/*', 'templates/assets/js/.'), ('templates/assets/fonts/*', 'templates/assets/fonts/.'), ('templates/assets/css/*', 'templates/assets/css/.'), ('templates/assets/*', 'templates/assets/.'), ('templates/template.html', 'templates/.')],
             hiddenimports=['jinja2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='xeazy',
          debug=False,
          strip=False,
          upx=True,
          console=True )
