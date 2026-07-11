# MeshAnalyzer Pro

**MeshAnalyzer Pro** is a desktop application for analyzing 3D printer bed mesh / leveling data.  
It helps users inspect surface deviation, visualize mesh behavior, compare measurements, generate reports, and make more informed mechanical adjustment decisions.

The application is designed especially for workflows where mesh data is exported from printer log/config packages such as `AC_CONF.pack` or `AC_LOG.pack`.

---

## Features

- Import mesh/config files
- Mesh table view with coordinate orientation
- Heatmap visualization
- Topography visualization
- 3D surface visualization
- Mesh statistics:
  - Minimum
  - Maximum
  - Average
  - Total deviation
  - RMS
  - Plane deviation
- Machine health score
- Four-level quality status:
  - PASS
  - ACCEPTABLE
  - WARNING
  - FAIL
- Smart diagnosis and mechanical recommendations
- Measurement history
- Favorite, label, and note support for history records
- Compare current mesh with previous measurements
- Export:
  - PDF report
  - Heatmap JPG
  - Topography JPG
  - 3D view JPG
  - Full export package
- Turkish and English language support
- Dark / light theme support
- Windows EXE packaging support with PyInstaller

---

## Coordinate Standard

MeshAnalyzer Pro uses the following coordinate standard:

```text
Front Left  = X1 / Y1
Front Right = Xmax / Y1
Rear Left   = X1 / Ymax
Rear Right  = Xmax / Ymax
```

In visual views and reports, the mesh is interpreted according to this orientation.

---

## Conf / Log File Import Notes

There are two supported ways to obtain the required files.

### 1. Anycubic Wiki Method

Open the official Anycubic Wiki page:

```text
https://wiki.anycubic.com/en/fdm-3d-printer/kobra-s1-combo/fault-log-export
```

Follow the steps on the page, then open the `AC_CONF.pack` file from the USB drive.

> **Warning:** Do not use `AC_LOG.pack` with this method.

### 2. Export From Device

Insert a USB drive into the printer.  
On the printer screen, follow this path:

```text
Setting → Device → Export logs to U-Disk
```

Then insert the USB drive into your computer and open the `AC_LOG.pack` file.

---

## PDF Reports

PDF reports include mesh summary, geometry metrics, machine health, visual graphs, diagnosis, recommendations, and a coordinate-labeled mesh table.

The mesh table is shown with X/Y coordinates, for example:

```text
       X1      X2      X3 ...
Y5   value   value   value
Y4   value   value   value
Y3   value   value   value
Y2   value   value   value
Y1   value   value   value
```

---

## Disclaimer

MeshAnalyzer Pro is based on mathematical calculations and software-based analysis.  
Any physical intervention on the printer, such as tightening screws, adding shims, adjusting mechanical parts, or modifying the device, is the responsibility of the user.

---

## Requirements

Typical Python requirements are listed in `requirements.txt`.

Main dependencies include:

- Python 3
- PySide6
- NumPy
- Matplotlib
- ReportLab

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

---

## Run From Source

```bash
python main.py
```

---

## Build Windows EXE

The project includes a PyInstaller spec file.

Recommended build command:

```bash
python -m PyInstaller MeshAnalyzerPro.spec
```

If PyInstaller is not installed:

```bash
python -m pip install pyinstaller
```

The generated executable will be located under:

```text
dist/
```

---

## Project Structure

```text
MeshAnalyzerPro/
├── assets/          # Icons and visual assets
├── config/          # Application configuration
├── controllers/     # Controller layer
├── core/            # Mesh parsing, analysis, diagnostics, config
├── database/        # History database logic
├── graphs/          # Graph widgets
├── gui/             # PySide6 user interface
├── help/            # Help documents
├── languages/       # Language files
├── reports/         # PDF/JPG export logic
├── themes/          # QSS themes
├── utils/           # Utility helpers
├── main.py
└── MeshAnalyzerPro.spec
```

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

# MeshAnalyzer Pro — Türkçe

**MeshAnalyzer Pro**, 3D yazıcı tabla mesh / leveling verilerini analiz etmek için geliştirilmiş bir masaüstü uygulamasıdır.  
Kullanıcının yüzey sapmalarını incelemesini, mesh davranışını görselleştirmesini, ölçümleri karşılaştırmasını, rapor oluşturmasını ve mekanik düzeltme kararlarını daha bilinçli şekilde vermesini sağlar.

Uygulama özellikle `AC_CONF.pack` veya `AC_LOG.pack` gibi yazıcı log/config paketlerinden mesh verisi alınan iş akışları için tasarlanmıştır.

---

## Özellikler

- Mesh/config dosyası içe aktarma
- Koordinat yönlendirmesine sahip mesh tablo görünümü
- Isı haritası görselleştirme
- Topografya görselleştirme
- 3B yüzey görselleştirme
- Mesh istatistikleri:
  - Minimum
  - Maksimum
  - Ortalama
  - Toplam sapma
  - RMS
  - Düzlem sapması
- Makine sağlığı skoru
- Dört seviyeli kalite durumu:
  - UYGUN
  - KABUL EDİLEBİLİR
  - UYARI
  - BAŞARISIZ
- Akıllı teşhis ve mekanik öneriler
- Ölçüm geçmişi
- Geçmiş kayıtları için favori, etiket ve not desteği
- Mevcut mesh ile önceki ölçümleri karşılaştırma
- Dışa aktarma:
  - PDF raporu
  - Isı haritası JPG
  - Topografya JPG
  - 3B görünüm JPG
  - Tümünü dışa aktarma paketi
- Türkçe ve İngilizce dil desteği
- Koyu / açık tema desteği
- PyInstaller ile Windows EXE paketleme desteği

---

## Koordinat Standardı

MeshAnalyzer Pro aşağıdaki koordinat standardını kullanır:

```text
Sol Ön   = X1 / Y1
Sağ Ön   = Xmax / Y1
Sol Arka = X1 / Ymax
Sağ Arka = Xmax / Ymax
```

Görsel ekranlarda ve raporlarda mesh bu yönlendirmeye göre yorumlanır.

---

## Conf / Log Dosyası Alma Notları

Gerekli dosyaları almanın iki yöntemi vardır.

### 1. Anycubic Wiki Yöntemi

Resmi Anycubic Wiki sayfasını açın:

```text
https://wiki.anycubic.com/en/fdm-3d-printer/kobra-s1-combo/fault-log-export
```

Sitedeki adımları takip edin ve ardından USB içindeki `AC_CONF.pack` dosyasını açın.

> **Uyarı:** Bu yöntemde `AC_LOG.pack` dosyasını kullanmayın.

### 2. Cihaz Üzerinden Dışa Aktarma

Yazıcıya USB takın.  
Yazıcı ekranında şu yolu takip edin:

```text
Setting → Device → Export logs to U-Disk
```

Ardından USB’yi bilgisayara takın ve `AC_LOG.pack` dosyasını açın.

---

## PDF Raporları

PDF raporları mesh özeti, geometri metrikleri, makine sağlığı, görsel grafikler, teşhis, öneriler ve koordinatlı mesh tablosu içerir.

Mesh tablosu X/Y koordinatlarıyla gösterilir. Örnek:

```text
       X1      X2      X3 ...
Y5   değer   değer   değer
Y4   değer   değer   değer
Y3   değer   değer   değer
Y2   değer   değer   değer
Y1   değer   değer   değer
```

---

## Sorumluluk Reddi

MeshAnalyzer Pro matematiksel hesaplamalara ve yazılım tabanlı analize dayanır.  
Yazıcı üzerinde yapılacak vida sıkma, pul ekleme, mekanik parça ayarı veya cihaz üzerinde yapılacak herhangi bir fiziksel müdahale kullanıcının sorumluluğundadır.

---

## Gereksinimler

Tipik Python gereksinimleri `requirements.txt` dosyasında listelenmiştir.

Ana bağımlılıklar:

- Python 3
- PySide6
- NumPy
- Matplotlib
- ReportLab

Bağımlılıkları kurmak için:

```bash
python -m pip install -r requirements.txt
```

---

## Kaynak Koddan Çalıştırma

```bash
python main.py
```

---

## Windows EXE Oluşturma

Projede PyInstaller spec dosyası bulunur.

Önerilen build komutu:

```bash
python -m PyInstaller MeshAnalyzerPro.spec
```

PyInstaller kurulu değilse:

```bash
python -m pip install pyinstaller
```

Oluşturulan EXE dosyası şu klasörde yer alır:

```text
dist/
```

---

## Proje Yapısı

```text
MeshAnalyzerPro/
├── assets/          # İkonlar ve görsel dosyalar
├── config/          # Uygulama ayarları
├── controllers/     # Controller katmanı
├── core/            # Mesh ayrıştırma, analiz, teşhis, config
├── database/        # Geçmiş veritabanı mantığı
├── graphs/          # Grafik widgetları
├── gui/             # PySide6 kullanıcı arayüzü
├── help/            # Yardım dokümanları
├── languages/       # Dil dosyaları
├── reports/         # PDF/JPG dışa aktarma mantığı
├── themes/          # QSS temaları
├── utils/           # Yardımcı araçlar
├── main.py
└── MeshAnalyzerPro.spec
```
