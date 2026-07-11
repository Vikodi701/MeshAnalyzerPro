"""
MeshAnalyzer Pro
Turkish Language Pack
"""

TEXT = {
    "app_name": "MeshAnalyzer Pro",

    "dashboard": "Panel",
    "mesh_view": "Mesh Görünümü",
    "heatmap": "Isı Haritası",
    "topography": "Topografya",
    "surface_3d": "3B Görünüm",
    "analysis": "Analiz",
    "diagnosis_recommendations": "Teşhis ve Öneriler",
    "compare": "Karşılaştırma",
    "history": "Geçmiş",
    "settings": "Ayarlar",

    "open_conf": "Conf. Dosyası Aç",
    "project_open": "Proje Aç",
    "project_save": "Proje Kaydet",
    "heatmap_jpg": "Isı Haritası JPG",
    "topography_jpg": "Topografya JPG",
    "surface_3d_jpg": "3B Görünüm JPG",
    "pdf": "PDF",
    "export_all": "Tümünü Dışa Aktar",

    "toolbar_tooltip_open_conf": (
        "<b>📂 Conf. Dosyası Aç</b><br>"
        "Mesh, conf veya desteklenen ölçüm dosyasını açar.<br><br>"
        "Dosya açıldığında Panel, Mesh Görünümü, Isı Haritası, Topografya, "
        "3B Görünüm, Analiz ve Teşhis sayfaları otomatik güncellenir."
    ),
    "toolbar_tooltip_project_open": (
        "<b>📁 Proje Aç</b><br>"
        "Daha önce kaydedilmiş MeshAnalyzer proje dosyasını açar.<br><br>"
        "Kayıtlı mesh verisi ve proje bilgileri yeniden yüklenir."
    ),
    "toolbar_tooltip_project_save": (
        "<b>💾 Proje Kaydet</b><br>"
        "Mevcut mesh analizini proje dosyası olarak kaydeder.<br><br>"
        "Daha sonra aynı analiz verisine tekrar dönmek için kullanılabilir."
    ),
    "toolbar_tooltip_heatmap_jpg": (
        "<b>🌈 Isı Haritası JPG</b><br>"
        "Mevcut mesh verisinin ısı haritası görselini JPG olarak dışa aktarır.<br><br>"
        "Renk dağılımı, yüksek ve düşük bölgeleri hızlıca incelemek için kullanılır."
    ),
    "toolbar_tooltip_topography_jpg": (
        "<b>〰 Topografya JPG</b><br>"
        "Mesh yüzeyinin kontur/topografya görünümünü JPG olarak dışa aktarır.<br><br>"
        "Yüzey eğimleri ve bölgesel seviye farklarını raporlamak için uygundur."
    ),
    "toolbar_tooltip_surface_3d_jpg": (
        "<b>🧊 3B Görünüm JPG</b><br>"
        "Mesh yüzeyinin üç boyutlu görünümünü JPG olarak dışa aktarır.<br><br>"
        "Yüzey formunu görsel olarak sunmak için kullanılır."
    ),
    "toolbar_tooltip_pdf": (
        "<b>📄 PDF Rapor</b><br>"
        "Mevcut analiz için PDF raporu oluşturur.<br><br>"
        "Rapor; özet değerler, kalite kontrol, grafikler ve mesh tablosu gibi bölümleri içerir."
    ),
    "toolbar_tooltip_export_all": (
        "<b>⬇ Tümünü Dışa Aktar</b><br>"
        "PDF raporu ve desteklenen görsel çıktıları tek klasöre aktarır.<br><br>"
        "Raporlama ve arşivleme için hızlı toplu çıktı almayı sağlar."
    ),
    "toolbar_tooltip_settings": (
        "<b>⚙ Ayarlar</b><br>"
        "Tolerans limitleri, tema ve dil seçeneklerini düzenler.<br><br>"
        "Değişiklikler kaydedildiğinde ilgili sayfalar otomatik güncellenir."
    ),

    "toolbar_status_open_conf": "Mesh veya conf dosyası aç",
    "toolbar_status_project_open": "Kayıtlı proje aç",
    "toolbar_status_project_save": "Mevcut projeyi kaydet",
    "toolbar_status_heatmap_jpg": "Isı haritasını JPG olarak dışa aktar",
    "toolbar_status_topography_jpg": "Topografyayı JPG olarak dışa aktar",
    "toolbar_status_surface_3d_jpg": "3B görünümü JPG olarak dışa aktar",
    "toolbar_status_pdf": "PDF rapor oluştur",
    "toolbar_status_export_all": "Tüm çıktıları dışa aktar",
    "toolbar_status_settings": "Ayarları aç",

    "ready": "Hazır",
    "mesh_waiting": "Mesh bekleniyor",
    "settings_title": "⚙ MeshAnalyzer Ayarları",
    "max_total_range": "Toplam Sapma Limiti (mm)",
    "max_rms": "RMS Limiti (mm)",
    "max_plane_deviation": "Düzlem Sapma Limiti (mm)",
    "theme": "Tema",
    "language": "Dil",
    "save_settings": "💾 Ayarları Kaydet",
    "success": "Başarılı",
    "settings_saved": "Ayarlar kaydedildi.",
    "close": "Kapat",
    "help": "Yardım",
    "modules": "Modüller",
    "file": "Dosya",
    "view": "Görünüm",
    "tools": "Araçlar",
    "help": "Yardım",
    "modules": "Modüller",
    "about": "Hakkında",
    "exit": "Çıkış",

    "tooltip_quality_status": (
        "<h3>✅ Kalite Durumu</h3>"
        "<b>Tanım</b><br>"
        "Mesh değerlerinin belirlenen tolerans limitleri içinde olup olmadığını gösterir.<br><br>"
        "<b>Sonuçlar</b><br>"
        "🟢 UYGUN: Değerler güvenli aralıktadır.<br>"
        "🟡 KABUL EDİLEBİLİR: Değerler limit içinde ancak sınıra yakındır.<br>"
        "🟠 UYARI: Değerler tolerans üstünde, kontrol önerilir.<br>"
        "🔴 BAŞARISIZ: Değerler tolerans dışındadır.<br><br>"
    ),

    "tooltip_machine_health": (
        "<h3>🩺 Makine Sağlığı</h3>"
        "<b>Tanım</b><br>"
        "Yüzey kalitesini 0-100 arasında özetleyen genel performans göstergesidir.<br><br>"
        "<b>Değerlendirilen veriler</b><br>"
        "• Toplam Sapma<br>"
        "• RMS<br>"
        "• Düzlem Sapması<br>"
        "• Akıllı Teşhis<br><br>"
        "<b>Yorum</b><br>"
        "🟢 90–100: Mükemmel<br>"
        "🟢 75–89: İyi<br>"
        "🟡 50–74: Kabul Edilebilir<br>"
        "🔴 0–49: Kritik<br><br>"
    ),

    "tooltip_total_range": (
        "<h3>📏 Toplam Sapma</h3>"
        "<b>Tanım</b><br>"
        "Mesh yüzeyindeki en yüksek ve en düşük nokta arasındaki toplam yükseklik farkıdır.<br><br>"
        "<b>Yorum</b><br>"
        "Düşük değer daha düzgün yüzey anlamına gelir.<br>"
        "Yüksek değer eğrilik veya deformasyon gösterebilir.<br><br>"
        "<b>Yorum</b><br>"

        "🟢 0.000–0.300 mm: Mükemmel<br>"
        "🟢 0.300–0.450 mm: İyi<br>"
        "🟡 0.450–0.600 mm: Kabul edilebilir<br>"
        "🔴 >0.600 mm: Kritik<br><br>"
        "<b>Birim</b><br>mm<br><br>"
    ),

    "tooltip_rms": (
        "<h3>📐 RMS</h3>"
        "<b>Tanım</b><br>"
        "Tüm ölçüm noktalarının referans yüzeye göre sapmalarının karelerinin "
        "ortalamasının kareköküdür.<br><br>"
        "<b>Neden önemlidir?</b><br>"
        "Tek bir uç değerden çok fazla etkilenmez ve tüm yüzeyi temsil eder.<br><br>"
        "<b>Yorum</b><br>"
        "🟢 0.000–0.120 mm: Mükemmel<br>"
        "🟢 0.120–0.180 mm: İyi<br>"
        "🟡 0.180–0.250 mm: Kabul edilebilir<br>"
        "🔴 >0.250 mm: Kritik<br><br>"
    ),

    "tooltip_plane_deviation": (
        "<h3>📊 Düzlem Sapması</h3>"
        "<b>Tanım</b><br>"
        "Mesh yüzeyinin en uygun referans düzleme olan maksimum uzaklığıdır.<br><br>"
        "<b>Kullanım Alanı</b><br>"
        "• Tabla eğriliği<br>"
        "• Montaj hataları<br>"
        "• Yüzey burulmaları<br><br>"
        "<b>Yorum</b><br>"
        "Düşük değer daha doğru hizalanmış yüzey anlamına gelir."
        "<b>Yorum</b><br>"

        "🟢 0.000–0.150 mm: Mükemmel<br>"
        "🟢 0.150–0.220 mm: İyi<br>"
        "🟡 0.220–0.300 mm: Kabul edilebilir<br>"
        "🔴 >0.300 mm: Kritik<br><br>"
    ),

    "tooltip_mesh_size": (
        "<h3>📂 Mesh Boyutu</h3>"
        "<b>Tanım</b><br>"
        "Analiz edilen yüzeydeki satır ve sütun sayısını gösterir.<br><br>"
        "<b>Örnek</b><br>"
        "20 × 30 = 600 ölçüm noktası"
    ),

    "tooltip_minimum": (
        "<h3>⬇ Minimum</h3>"
        "<b>Tanım</b><br>"
        "Mesh içerisindeki en düşük ölçüm değeridir.<br><br>"
        "<b>Kullanım</b><br>"
        "Toplam sapma hesaplamasında kullanılır.<br><br>"
        "<b>Birim</b><br>mm"
    ),

    "tooltip_maximum": (
        "<h3>⬆ Maksimum</h3>"
        "<b>Tanım</b><br>"
        "Mesh içerisindeki en yüksek ölçüm değeridir.<br><br>"
        "<b>Kullanım</b><br>"
        "Toplam sapma hesaplamasında kullanılır.<br><br>"
        "<b>Birim</b><br>mm"
    ),

    "tooltip_average": (
        "<h3>➗ Ortalama</h3>"
        "<b>Tanım</b><br>"
        "Tüm ölçüm noktalarının ortalama yüksekliğidir.<br><br>"
        "<b>Ne gösterir?</b><br>"
        "Yüzeyin genel referans seviyesini ifade eder.<br><br>"
        "<b>Birim</b><br>mm"
    ),

    "tooltip_file_info": (
        "<h3>📄 Dosya</h3>"
        "<b>Tanım</b><br>"
        "Son açılan mesh dosyasının adını gösterir.<br><br>"
        "<b>Ek bilgi</b><br>"
        "Analiz süresi de bu kartın alt kısmında görüntülenir."
    ),

    "tooltip_analysis_result": (
        "<h3>🧠 Son Analiz</h3>"
        "<b>Tanım</b><br>"
        "Analiz motorunun tüm hesaplamaları birlikte değerlendirerek oluşturduğu genel sonuçtur.<br><br>"
        "<b>Olası Sonuçlar</b><br>"
        "🟢 Uygun<br>"
        "🟡 Dikkat<br>"
        "🔴 Kontrol Gerekli<br><br>"
        "<b>İpucu</b><br>"
        "RMS, Toplam Sapma, Düzlem Sapması ve Makine Sağlığı birlikte değerlendirilir.<br>"
    ),

    "dashboard_title": "MeshAnalyzer Pro Paneli",

    "machine_health": "Makine Sağlığı",
    "quality_status": "Kalite Durumu",
    "total_deviation": "Toplam Sapma",
    "plane_deviation": "Düzlem Sapması",
    "mesh_size": "Mesh Boyutu",
    "minimum": "Minimum",
    "maximum": "Maksimum",
    "average": "Ortalama",
    "file": "Dosya",
    "analysis": "Analiz",

    "waiting_mesh": "Mesh bekleniyor",
    "waiting_result": "Sonuç bekleniyor",
    "no_file": "Henüz dosya yok",
    "rows_columns": "Satır × Sütun",
    "mesh_average": "Mesh ortalaması",
    "lowest_point": "En düşük nokta",
    "highest_point": "En yüksek nokta",

    "tolerance_ok": "Tolerans içinde",
    "analysis_ok": "Uygun",
    "mesh_quality_passed": "Mesh kalite kontrolünden geçti",
    "near_limit": "Sınıra yakın",
    "attention": "Dikkat",
    "mesh_near_limit": "Mesh tolerans sınırına yakın",
    "out_of_tolerance": "Tolerans dışında",
    "inspection_required": "Kontrol Gerekli",
    "mesh_out_of_limits": "Mesh limitlerin dışında",
    "limit": "Limit",
    "lowest_measurement": "En düşük ölçüm",
    "highest_measurement": "En yüksek ölçüm",
    "average_height": "Ortalama yükseklik",
    "last_opened_mesh": "Son açılan mesh",
    "analysis_time": "Analiz",
    "analysis_empty": "Mesh yüklendiğinde analiz sonuçları burada gösterilecek.",
    "analysis_result_for": "{name} analiz sonucu",
    "diagnosis_empty": "Mesh yüklendiğinde teşhis ve öneriler burada gösterilecek.",
    "diagnosis_result_for": "{name} teşhis ve önerileri",
    "analysis_duration": "Analiz Süresi",
    "analysis_calculation_time": "Hesaplama süresi",
    "overall_status": "Genel Durum",
    "geometry_section": "Düzlem ve Geometri",
    "quality_control": "Kalite Kontrol",
    "standard_deviation": "Standart Sapma",
    "plane_max_deviation": "Düzlem Maks. Sapma",
    "plane_rms_deviation": "Düzlem RMS Sapma",
    "x_slope": "X Eğimi",
    "y_slope": "Y Eğimi",
    "trend": "Trend Analizi",
    "smart_diagnostic": "Akıllı Teşhis",
    "mechanical_diagnostic": "Mekanik Teşhis",
    "status_pass": "UYGUN",
    "status_ok": "UYGUN",
    "status_excellent": "MÜKEMMEL",
    "status_good": "İYİ",
    "status_warning": "UYARI",
    "status_fail": "BAŞARISIZ",
    "status_error": "HATA",
    "status_bad": "KÖTÜ",
    "status_critical": "KRİTİK",


    "trend_no_data": "Yetersiz veri",
    "trend_improving": "İyileşiyor",
    "trend_degrading": "Bozuluyor",
    "trend_stable": "Stabil",
    "trend_min_records_required": "Trend analizi için en az 2 kayıt gerekli.",
    "trend_record_count": "Kayıt Sayısı",
    "trend_status": "Durum",
    "trend_first_total_deviation": "İlk Toplam Sapma",
    "trend_last_total_deviation": "Son Toplam Sapma",
    "trend_first_rms": "İlk RMS",
    "trend_last_rms": "Son RMS",
    "trend_change": "Değişim",

    "critical": "Kritik",
    "good": "İyi",
    "excellent": "Mükemmel",
    "needs_attention": "Kontrol Edilmeli",

    "mesh_summary": "Mesh Görünümü",
    "selected_point": "Seçilen Nokta",
    "selected_point_none": "Seçilen nokta: -",
    "point_status": "Durum",
    "normal_point": "Normal Nokta",
    "minimum_point": "Minimum Nokta",
    "maximum_point": "Maksimum Nokta",

    "tooltip_mesh_summary": (
        "<h3>Mesh Görünümü</h3>"

        "<b>Boyut</b><br>"
        "Mesh'in satır × sütun sayısını gösterir.<br><br>"

        "<b>Minimum</b><br>"
        "Ölçülen en düşük yükseklik değeridir.<br><br>"

        "<b>Maksimum</b><br>"
        "Ölçülen en yüksek yükseklik değeridir.<br><br>"

        "<b>Ortalama</b><br>"
        "Tüm ölçüm noktalarının ortalama yüksekliğidir.<br><br>"

        "<b>RMS</b><br>"
        "Yüzey kalitesini temsil eden en önemli istatistiksel ölçüdür.<br><br>"

        "<b>Toplam Sapma</b><br>"
        "Maksimum ve minimum yükseklik arasındaki farktır."
    ),

        "color_scale": "Renk Skalası",
        "color_palette": "Renk Paleti:",
        "heatmap_summary": "Isı Haritası",

        "heatmap_summary_tooltip": (
        "<b>Isı Haritası</b><br><br>"

        "Bu panel, oluşturulan mesh verisinin renk dağılımını ve temel "
        "istatistiklerini özetler.<br><br>"

        "<b>🎨 Renk Paleti</b><br>"
        "Isı haritasında kullanılacak renk skalasını seçebilirsiniz. "
        "Renk paleti yalnızca görünümü değiştirir, ölçüm verisini değiştirmez.<br><br>"

        "<b>📉 Minimum</b><br>"
        "Ölçülen en düşük Z değeridir.<br><br>"

        "<b>📈 Maksimum</b><br>"
        "Ölçülen en yüksek Z değeridir.<br><br>"

        "<b>📊 Ortalama</b><br>"
        "Tüm ölçüm noktalarının ortalama yüksekliğidir.<br><br>"

        "<b>📐 RMS</b><br>"
        "Yüzey düzensizliğini gösteren istatistiksel değerdir. "
        "Daha düşük RMS daha düzgün yüzey anlamına gelir.<br><br>"

        "<b>📏 Toplam Sapma</b><br>"
        "En yüksek ve en düşük nokta arasındaki toplam farktır.<br><br>"

        "<b>💡 İpuçları</b><br>"
        "• Hücre üzerine geldiğinizde kenarlık vurgulanır.<br>"
        "• Aynı değer renk skalasında işaretlenir.<br>"
        "• Farklı renk paletleri yalnızca görsel sunumu değiştirir."
        
    ),
}

TEXT.update({
    "surface_summary": "3B Görünüm",
    "surface_view_angle": "Bakış Açısı:",
    "surface_view_default": "Varsayılan",
    "surface_view_front": "Önden",
    "surface_view_side": "Yandan",
    "surface_view_top": "Üstten",
    "surface_view_detail": "Detay",
    "surface_matrix_mode": "Matris",
    "surface_probed_matrix": "Probed matrix",
    "surface_mesh_matrix": "Mesh matrix",
    "surface_wireframe": "Tel kafes",
    "surface_zero_plane": "Yüzey düzlemini göster",
    "surface_color_scale": "Renk ölçeği",
    "surface_box_scale": "Kutu ölçeği",
    "surface_reset_color_scale": "Renk ölçeğini varsayılana döndür",
    "surface_reset_box_scale": "Kutu ölçeğini varsayılana döndür",
    "surface_measurement": "Ölçüm",
    "surface_real_x": "Gerçek X",
    "surface_real_y": "Gerçek Y",
    "surface_color_scale_position": "Renk skalası",
    "surface_summary_tooltip": (
        "<b>3B Görünüm</b><br><br>"
        "Ölçülen mesh yüzeyini üç boyutlu olarak gösterir. "
        "Eğim, düşük/yüksek bölgeler ve genel yüzey formunu incelemek için kullanılır."
    ),
    "surface_minimum_tooltip": (
        "<b>Minimum</b><br><br>"
        "Geçerli mesh içindeki en düşük ölçülen Z değeridir."
    ),
    "surface_maximum_tooltip": (
        "<b>Maksimum</b><br><br>"
        "Geçerli mesh içindeki en yüksek ölçülen Z değeridir."
    ),
    "surface_average_tooltip": (
        "<b>Ortalama</b><br><br>"
        "Tüm ölçüm noktalarının ortalama Z yüksekliğidir."
    ),
    "surface_rms_tooltip": (
        "<b>RMS</b><br><br>"
        "Yüzey düzensizliğini gösteren değerdir. Daha düşük RMS daha düz yüzey anlamına gelir."
    ),
    "surface_total_range_tooltip": (
        "<b>Toplam Sapma</b><br><br>"
        "En yüksek ve en düşük ölçüm noktası arasındaki farktır."
    ),
    "topography_summary": "Topografya",
    "contour_levels": "Kontur Seviyesi:",
    "topography_summary_tooltip": (
        "<b>Topografya</b><br><br>"
        "Bu panel mesh yüzeyini eş yükseklik eğrileriyle yorumlamak için "
        "kullanılır.<br><br>"
        "<b>Renk Paleti</b><br>"
        "Haritada kullanılan renk dağılımını değiştirir. Ölçüm verisi değişmez.<br><br>"
        "<b>Kontur Seviyesi</b><br>"
        "Haritadaki yükseklik bantlarının ve çizgilerin ayrıntı yoğunluğunu belirler. "
        "Yüksek değer daha detaylı, düşük değer daha sade görünüm verir."
    ),
    "history_title": "Geçmiş",
    "history_tooltip": (
        "<b>Geçmiş</b><br><br>"
        "Daha önce açılan mesh kayıtlarını listeler. "
        "Bir kaydı çift tıklayarak veya seçip açarak tekrar yükleyebilirsiniz."
    ),
    "history_info": (
        "Daha önce açılan mesh kayıtları burada tutulur. "
        "Bir satıra çift tıklayarak kaydı tekrar açabilir, seçili kaydı silebilir "
        "veya tüm geçmişi temizleyebilirsiniz."
    ),
    "history_refresh": "Geçmişi Yenile",
    "history_open_selected": "Seçili Kaydı Aç",
    "history_delete_selected": "Seçili Kaydı Sil",
    "history_clear": "Geçmişi Temizle",
    "history_id": "ID",
    "history_date": "Tarih",
    "history_file": "Dosya",
    "history_rows": "Satır",
    "history_cols": "Sütun",
    "history_empty": "Geçmiş kaydı yok.",
    "history_record_count": "{count} kayıt listeleniyor.",
    "history_load_failed_title": "Mesh Bulunamadı",
    "history_load_failed_message": "Seçilen geçmiş kaydı yüklenemedi.",
    "history_delete_title": "Kaydı Sil",
    "history_delete_message": "Seçili geçmiş kaydı silinsin mi?",
    "history_clear_title": "Geçmişi Temizle",
    "history_clear_message": "Tüm geçmiş kalıcı olarak silinsin mi?",
})

TEXT.update({
    "message": "Mesaj",
    "general_assessment": "Genel Değerlendirme",
    "no_mechanical_issue": "Belirgin mekanik problem tespit edilmedi.",
    "corner_analysis": "Köşe Analizi",
    "lowest_corner": "En düşük köşe",
    "highest_corner": "En yüksek köşe",
    "corner_front_left": "Ön Sol",
    "corner_front_right": "Ön Sağ",
    "corner_rear_left": "Arka Sol",
    "corner_rear_right": "Arka Sağ",
    "slope_analysis": "Eğim Analizi",
    "x_direction": "X Yönü",
    "y_direction": "Y Yönü",
    "x_axis_balanced": "X ekseni dengeli",
    "y_axis_balanced": "Y ekseni dengeli",
    "right_higher_than_left": "Sağ taraf sol tarafa göre yüksek",
    "left_higher_than_right": "Sol taraf sağ tarafa göre yüksek",
    "rear_higher_than_front": "Arka taraf ön tarafa göre yüksek",
    "front_higher_than_rear": "Ön taraf arka tarafa göre yüksek",
    "twist_analysis": "Burulma Analizi",
    "twist_value": "Burulma Değeri",
    "direction": "Yön",
    "severity": "Şiddet",
    "no_significant_twist": "Belirgin burulma yok",
    "clockwise_twist": "Saat yönü burulma eğilimi",
    "counter_clockwise_twist": "Saat yönü tersi burulma eğilimi",
    "severity_none": "Yok",
    "severity_light": "Hafif",
    "severity_medium": "Orta",
    "severity_high": "Yüksek",
    "shim_recommendations": "Shim Önerileri",
    "shim_no_change": "Değişiklik gerekmez",
    "shim_add_raise": "Shim ekle / yükselt",
    "shim_reduce_lower": "Shim azalt / alçalt",
    "main_recommendation": "Ana Öneri",
    "main_recommendation_sentence": "{name} için yaklaşık {delta} mm düzeltme önerilir.",
    "action": "İşlem",
    "recommended_action": "Önerilen İşlem",
    "remeasure_after_adjustment": "Mekanik düzeltme sonrası yeniden mesh ölçümü alın.",
    "apply_largest_shim_first": "Önce en büyük shim önerisini uygulayın.",
    "run_auto_level_again": "Ardından tekrar otomatik seviyeleme yapın.",
    "mesh_within_tolerance": "Mesh tolerans içinde.",
    "mesh_near_tolerance": "Mesh sınır değere yakın.",
    "mesh_out_of_tolerance": "Mesh tolerans dışında.",
    "table_almost_flat": "Tabla neredeyse tamamen düz.",
    "table_good_condition": "Tabla iyi durumda.",
    "table_slight_warp": "Hafif tabla eğriliği mevcut.",
    "table_serious_warp": "Tabla ciddi şekilde eğri.",
    "x_right_side_high": "X ekseninde sağ taraf yukarı eğimli.",
    "x_left_side_high": "X ekseninde sol taraf yukarı eğimli.",
    "surface_very_smooth": "Yüzey oldukça düzgün.",
    "surface_acceptable": "Yüzey kabul edilebilir.",
    "surface_local_waves": "Yüzeyde lokal dalgalanmalar mevcut.",
    "surface_serious_deformation": "Yüzey ciddi deformasyon gösteriyor.",
    "recommendations": "Öneriler",
    "raise": "Yükselt",
    "lower": "Alçalt",
    "compare_open_old": "Eski Mesh Aç",
    "compare_open_new": "Yeni Mesh Aç",
    "compare_action": "Karşılaştır",
    "compare_old_mesh": "Eski Mesh",
    "compare_new_mesh": "Yeni Mesh",
    "compare_old_label": "Eski",
    "compare_new_label": "Yeni",
    "compare_old_not_selected": "Eski mesh seçilmedi",
    "compare_new_not_selected": "Yeni mesh seçilmedi",
    "compare_no_previous_short": "Geçmişte önceki kayıt yok",
    "compare_auto_hint": "İki mesh seçildiğinde otomatik karşılaştırılır.",
    "compare_no_previous_history": "Karşılaştırma için geçmişte önceki mesh kaydı bulunamadı.",
    "compare_select_two_mesh": "Lütfen iki mesh dosyası seçin.",
    "compare_open_old_title": "Eski Mesh Aç",
    "compare_open_new_title": "Yeni Mesh Aç",
    "mesh_file_filter": "Mesh Dosyaları (*.pack *.csv *.txt *.json);;Tüm Dosyalar (*)",
    "compare_report_title": "MESH KARŞILAŞTIRMA",
    "compare_old_total_deviation": "Eski Toplam Sapma",
    "compare_new_total_deviation": "Yeni Toplam Sapma",
    "compare_improvement": "İyileşme",
    "compare_delta_min": "Delta Min",
    "compare_delta_max": "Delta Max",
    "compare_delta_average": "Delta Ortalama",
    "compare_delta_mesh": "Delta Mesh",
    "compare_delta_heatmap": "Fark Haritası",
    "compare_cell_value": "Değer",
    "compare_cell_difference": "Fark",
})


TEXT.update({
    "report_title": "MeshAnalyzer Pro Raporu",
    "report_date": "Tarih",
    "report_file": "Dosya",
    "report_mesh_summary_section": "Mesh Özeti",
    "report_geometry_section": "Geometri Analizi",
    "report_machine_health_section": "Makine Sağlığı Skoru",
    "report_heatmap_section": "Isı Haritası",
    "report_topography_section": "Topografik Harita",
    "report_surface_section": "3B Yüzey",
    "report_smart_diagnostic_section": "Akıllı Teşhis",
    "report_mechanical_diagnostic_section": "Mekanik Teşhis",
    "report_mesh_table_section": "Mesh Tablosu",
    "report_heatmap_title": "Isı Haritası",
    "report_topography_title": "Topografik Harita",
    "report_surface_title": "3B Yüzey",
    "report_x_coordinate": "X Koordinatı",
    "report_y_coordinate": "Y Koordinatı",
    "report_height_mm": "Yükseklik (mm)",
    "report_score": "Skor",
    "report_status": "Durum",
    "report_category": "Kategori",
})

TEXT.update({
    "export_mesh_required_message": "Önce bir mesh dosyası açmalısın.",
    "export_pdf_failed_title": "PDF Oluşturulamadı",
    "export_pdf_save_title": "PDF Rapor Kaydet",
    "export_pdf_error_title": "PDF Hatası",
    "export_pdf_created_status": "PDF oluşturuldu: {filename}",
    "export_pdf_failed_status": "PDF oluşturulamadı.",
    "export_jpeg_failed_title": "JPEG Oluşturulamadı",
    "export_heatmap_jpeg_save_title": "Isı Haritası JPEG Kaydet",
    "export_topography_jpg_save_title": "Topografya JPG Kaydet",
    "export_surface_jpg_save_title": "3B Görünüm JPG Kaydet",
    "export_jpeg_error_title": "JPEG Hatası",
    "export_jpeg_created_status": "JPEG oluşturuldu: {filename}",
    "export_jpeg_failed_status": "JPEG oluşturulamadı.",
})


TEXT.update({
    "tooltip_analysis_overall_status": (
        "<h3>✅ Genel Durum</h3>"
        "Analiz sonucunun toleranslara göre genel geçme/kalma durumunu gösterir.<br><br>"
        "FAIL değeri, en az bir kalite kontrol limitinin aşıldığını belirtir."
    ),
    "tooltip_analysis_duration": (
        "<h3>⏱ Analiz Süresi</h3>"
        "Mesh verisinin analiz motoru tarafından ne kadar sürede işlendiğini gösterir.<br><br>"
        "Bu değer performans bilgisidir; ölçüm kalitesini doğrudan değiştirmez."
    ),
    "tooltip_analysis_mesh_summary": (
        "<h3>📊 Mesh Özeti</h3>"
        "Mesh boyutu, minimum, maksimum, ortalama, RMS ve toplam sapma gibi temel istatistikleri gösterir.<br><br>"
        "Bu bölüm yüzeyin genel ölçüm karakterini hızlıca okumak için kullanılır."
    ),
    "tooltip_analysis_geometry": (
        "<h3>📐 Düzlem ve Geometri</h3>"
        "Yüzeyin referans düzleme göre eğimini, RMS düzlem sapmasını ve maksimum düzlem sapmasını gösterir.<br><br>"
        "Tabla eğriliği, montaj hatası veya yüzey burulması hakkında fikir verir."
    ),
    "tooltip_analysis_quality_control": (
        "<h3>🧪 Kalite Kontrol</h3>"
        "Toplam sapma, RMS ve düzlem sapması değerlerini ayarlarda tanımlanan limitlerle karşılaştırır.<br><br>"
        "Kırmızı durum limit aşımı, sarı durum sınıra yakınlık, yeşil durum uygunluk anlamına gelir."
    ),
    "tooltip_analysis_trend": (
        "<h3>📈 Trend</h3>"
        "Geçmiş kayıtlar varsa önceki meshlerle karşılaştırmalı eğilim bilgisi verir.<br><br>"
        "Trend analizi için en az iki geçmiş kayıt gerekir."
    ),
    "tooltip_diagnosis_smart": (
        "<h3>🧠 Akıllı Teşhis</h3>"
        "Analiz motorunun mesh istatistiklerini yorumlayarak oluşturduğu özet teşhistir.<br><br>"
        "Olası yüzey problemi, risk seviyesi ve genel durumu hızlı okumak için kullanılır."
    ),
    "tooltip_diagnosis_mechanical": (
        "<h3>🛠 Mekanik Teşhis</h3>"
        "Mesh davranışına göre olası mekanik nedenleri ve uygulanabilecek önerileri listeler.<br><br>"
        "Tabla ayarı, mekanik gevşeklik, eğrilik veya hizalama sorunlarını yorumlamaya yardımcı olur."
    ),
    "tooltip_compare_old_mesh": (
        "<h3>⬅ Eski Mesh</h3>"
        "Karşılaştırmada referans alınan önceki mesh verisini gösterir.<br><br>"
        "Yeni mesh ile fark hesaplaması bu veri üzerinden yapılır."
    ),
    "tooltip_compare_new_mesh": (
        "<h3>➡ Yeni Mesh</h3>"
        "Mevcut veya son yüklenen mesh verisini gösterir.<br><br>"
        "Eski mesh ile karşılaştırılarak iyileşme veya kötüleşme hesaplanır."
    ),
    "tooltip_compare_report": (
        "<h3>📋 Mesh Karşılaştırma</h3>"
        "Eski ve yeni mesh arasındaki toplam sapma, iyileşme oranı ve delta değerlerini özetler.<br><br>"
        "Pozitif/negatif değişimler yüzeyin hangi yönde değiştiğini gösterir."
    ),
    "tooltip_compare_delta_heatmap": (
        "<h3>🌡 Fark Haritası</h3>"
        "Yeni mesh ile eski mesh arasındaki hücresel farkları renkli olarak gösterir.<br><br>"
        "Sıfıra yakın değerler az değişim, yüksek pozitif veya negatif değerler belirgin değişim anlamına gelir."
    ),
})



TEXT.update({
    "empty_conf_waiting_title": "Conf. dosyası bekleniyor",
    "empty_conf_waiting_message": "Bir mesh veya conf dosyası açıldığında bu alan otomatik olarak güncellenecek.",
    "compare_old_total_range": "Eski Toplam Sapma",
    "compare_new_total_range": "Yeni Toplam Sapma",
    "reset_to_default": "Varsayılana Dön",
    "settings_applied": "Ayarlar uygulandı",
    "settings_total_deviation_limit_tooltip": "<b>Toplam Sapma Limiti</b><br><br>Mesh üzerindeki en yüksek ve en düşük ölçüm noktası arasındaki toplam farkı sınırlar. Genel yatak yükseklik farkını hızlı değerlendirmek için kullanılır.<br><br><b>Mükemmel:</b> ≤ 0,300 mm<br><b>İyi:</b> ≤ 0,450 mm<br><b>Kabul edilebilir:</b> ≤ 0,600 mm<br><b>Kritik:</b> &gt; 0,600 mm",
    "settings_rms_limit_tooltip": "<b>RMS Limiti</b><br><br>Tüm mesh noktalarının genel yüzey düzensizliğini istatistiksel olarak ifade eder. Düşük RMS, yüzeyin daha dengeli ve düzgün olduğunu gösterir.<br><br><b>Mükemmel:</b> ≤ 0,120 mm<br><b>İyi:</b> ≤ 0,180 mm<br><b>Kabul edilebilir:</b> ≤ 0,250 mm<br><b>Kritik:</b> &gt; 0,250 mm",
    "settings_plane_deviation_limit_tooltip": "<b>Düzlem Sapma Limiti</b><br><br>Mesh yüzeyinin ideal düzleme göre ne kadar saptığını sınırlar. Yatak eğimi, mekanik hizalama ve düzlemsel bozuklukları yorumlamak için kullanılır.<br><br><b>Mükemmel:</b> ≤ 0,150 mm<br><b>İyi:</b> ≤ 0,220 mm<br><b>Kabul edilebilir:</b> ≤ 0,300 mm<br><b>Kritik:</b> &gt; 0,300 mm",
    "settings_graph_defaults": "Grafik Varsayılanları",
    "settings_default_heatmap_palette": "Varsayılan Isı Haritası Paleti",
    "settings_default_topography_palette": "Varsayılan Topografya Paleti",
    "settings_default_surface_palette": "Varsayılan 3B Görünüm Paleti",
    "settings_default_surface_view": "Varsayılan 3B Bakış Açısı",
    "settings_report_settings": "Rapor Ayarları",
    "settings_report_include_graphs": "PDF rapora grafikler eklensin",
    "settings_report_include_diagnostics": "PDF rapora teşhis ve öneriler eklensin",
    "settings_report_include_mesh_table": "PDF rapora mesh tablosu eklensin",
    "settings_export_jpg_show_cell_values": "JPG ısı haritasında hücre değerleri gösterilsin",
    "settings_appearance_settings": "Görünüm Ayarları",
    "settings_appearance_show_table_values": "Tablo hücrelerinde değerleri göster",
    "settings_appearance_show_colorbar": "Grafiklerde colorbar göster",
    "settings_appearance_show_hover_info": "Hover bilgi kutularını göster",
    "settings_appearance_start_maximized": "Başlangıçta pencereyi tam ekran aç",
    "dashboard_disclaimer": "<b>Sorumluluk Reddi:</b> Yazılım matematiksel hesaplamalara dayanır. Cihaz üzerinde yapacağınız fiziksel müdahaleler (vidalama, pul ekleme vb.) kullanıcı sorumluluğundadır.",
    "settings_tolerance_settings": "Tolerans Ayarları",
    "settings_general_settings": "Genel Ayarlar",
    "mechanical_priority_recommendations": "Öncelikli Mekanik Öneriler",
    "no_priority_correction_needed": "Öncelikli mekanik düzeltme gerekmiyor.",
    "apply_largest_correction_first": "Önce en büyük farktan başlayın:",
    "compare_summary_section": "Sonuç Özeti",
    "compare_metric_changes": "Metrik Değişimleri",
    "compare_total_range_change": "Toplam Sapma Değişimi",
    "compare_old_rms": "Eski RMS",
    "compare_new_rms": "Yeni RMS",
    "compare_rms_change": "RMS Değişimi",
    "compare_regional_changes": "Bölgesel Değişimler",
    "compare_most_improved_area": "En çok düzelmiş bölge",
    "compare_most_worsened_area": "En çok kötüleşmiş bölge",
    "compare_delta_statistics": "Delta İstatistikleri",
    "compare_delta_abs_max": "Delta Mutlak Maksimum",
    "compare_summary_better": "Genel sonuç: Yeni mesh önceki ölçüme göre iyileşmiş görünüyor.",
    "compare_summary_worse": "Genel sonuç: Yeni mesh önceki ölçüme göre kötüleşmiş görünüyor.",
    "compare_summary_similar": "Genel sonuç: Yeni mesh önceki ölçüme yakın; belirgin iyileşme veya kötüleşme sınırlı.",
    "report_result_summary_section": "Sonuç Özeti",
    "report_summary_general_status": "Genel Durum",
    "report_summary_score": "Sağlık Skoru",
    "report_summary_tolerance": "Tolerans Durumu",
    "report_summary_main_problem": "Ana Problem",
    "report_summary_recommended_action": "Önerilen İşlem",
    "report_summary_status_good": "İyi / Kabul Edilebilir",
    "report_summary_status_warning": "Dikkat Gerektiriyor",
    "report_summary_status_critical": "Kritik / Kontrol Gerekli",
    "report_summary_problem_tolerance": "Mesh değerleri belirlenen tolerans sınırlarının dışında.",
    "report_summary_problem_plane": "Düzlemsel sapma yüksek görünüyor.",
    "report_summary_problem_x_slope": "X yönünde belirgin eğim var.",
    "report_summary_problem_y_slope": "Y yönünde belirgin eğim var.",
    "report_summary_problem_none": "Belirgin ana problem tespit edilmedi.",
    "report_summary_recommendation_shim": "{name} için yaklaşık {delta:.3f} mm düzeltme önerilir.",
    "report_summary_recommendation_remeasure": "Mekanik kontrol sonrası yeniden mesh ölçümü alın.",
    "history_favorite": "Favori",
    "history_label": "Etiket",
    "history_note": "Not",
    "history_toggle_favorite": "⭐ Favori",
    "history_edit_note_label": "Not / Etiket",
    "history_compare_previous": "Öncekiyle Karşılaştır",
    "history_edit_label_title": "Ölçüm Etiketi",
    "history_edit_label_message": "Bu ölçüm için kısa etiket girin:",
    "history_edit_note_title": "Ölçüm Notu",
    "history_edit_note_message": "Bu ölçüm için not girin:",
    "history_no_previous_for_compare": "Bu kayıt için karşılaştırılacak önceki mesh kaydı bulunamadı.",
    "mesh_validation_info": "Dosya açılırken mesh boşluk, satır/sütun tutarlılığı, sayısal değerler ve olağan dışı değer aralığı açısından kontrol edilir.",
    "coordinate_standard_info": "<b>Koordinat Standardı:</b> Ön Sol = X1/Y1 · Ön Sağ = Xmax/Y1 · Arka Sol = X1/Ymax · Arka Sağ = Xmax/Ymax",
    "acceptable": "Kabul Edilebilir",
    "status_acceptable": "KABUL EDİLEBİLİR",
    "acceptable_range": "Kabul edilebilir aralıkta",
    "mesh_quality_acceptable": "Mesh kabul edilebilir aralıkta",
    "check_recommended": "Kontrol önerilir",
    "mesh_check_recommended": "Mesh tolerans üstünde, kontrol önerilir",
    "conf_help_card_title": "Conf. Dosyası Nasıl Alınır",
    "conf_help_wiki_button": "Anycubic Wiki",
    "conf_help_device_button": "2. Cihaz Üzerinden",
    "conf_help_wiki_title": "Anycubic Wiki ile Conf. Dosyası Alma",
    "conf_help_wiki_message": "https://wiki.anycubic.com/en/fdm-3d-printer/kobra-s1-combo/fault-log-export bu siteyi açın.\\n\\nSitedeki adımları takip edin ve ardından USB`deki AC_CONF.pack dosyasını açın.\\n\\nUYARI: Bu yöntemde AC_LOG.pack dosyasını kullanmayın!",
    "conf_help_device_title": "Cihaz Üzerinden Conf. Dosyası Alma",
    "conf_help_device_message": "Yazıcıya USB takın ardından yazıcı ekranında Setting - Device - Export logs to U-Disk yolunu takip edin.\\n\\nUSB`yi bilgisayara takın ve AC_LOG.pack dosyasını açın.",
    "dialog_ok": "Tamam",
    "dialog_cancel": "İptal",
    "dialog_yes": "Evet",
    "dialog_no": "Hayır",
    "dialog_open": "Aç",
    "dialog_save": "Kaydet",
    "history_edit_label_button": "Etiket",
    "history_edit_note_button": "Not",
    "report_mesh_table_coordinate_note": "Koordinatlar: Sol Ön = X1/Y1 · Sağ Ön = Xmax/Y1 · Sol Arka = X1/Ymax · Sağ Arka = Xmax/Ymax",
})
