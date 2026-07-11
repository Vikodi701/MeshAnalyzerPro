# Windows EXE build note

Ekran görüntüsündeki farkın sebebi EXE içinde theme/assets dosyalarının doğru bulunamamasıydı.
Bu paketle:
- themes/*.qss artık resource_path ile okunur.
- sidebar/toolbar SVG iconları resource_path ile okunur.
- PyInstaller için MeshAnalyzerPro.spec eklendi.

Önerilen build:
    pyinstaller MeshAnalyzerPro.spec

Tek komutla build gerekiyorsa:
    pyinstaller --noconsole --name MeshAnalyzerPro --icon assets/icons/app.ico --add-data "assets;assets" --add-data "themes;themes" --add-data "config;config" --add-data "help;help" --add-data "languages;languages" main.py

Not:
Windows'ta --add-data ayıracı noktalı virgüldür (;).
Linux/macOS tarafında iki nokta üst üste (:) kullanılır.
