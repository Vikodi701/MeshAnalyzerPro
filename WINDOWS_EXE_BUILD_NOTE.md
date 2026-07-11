# Windows EXE icon fix

Bu sürümde EXE icon için üç katmanlı düzeltme var:

1. `MeshAnalyzerPro.spec` içinde icon yolu absolute path olarak verildi.
2. `app.ico` ve `app.png` EXE içine ayrıca kök dizine de dahil edildi.
3. Windows HWND seviyesinde `WM_SETICON` ile küçük/büyük pencere icon'u yeniden uygulanıyor.

Önerilen build komutu:

```bat
python -m PyInstaller --clean --noconfirm MeshAnalyzerPro.spec
```

Eğer Windows hâlâ eski icon gösterirse bu genelde Windows icon cache / eski taskbar pin cache sebebidir.

Kontrol listesi:

```bat
rmdir /s /q build
rmdir /s /q dist
python -m PyInstaller --clean --noconfirm MeshAnalyzerPro.spec
```

Sonra:
- Eski taskbar pin'ini kaldırın.
- Yeni EXE'yi farklı klasörden veya farklı isimle deneyin.
- Gerekirse Windows Explorer'ı yeniden başlatın veya icon cache'i temizleyin.
