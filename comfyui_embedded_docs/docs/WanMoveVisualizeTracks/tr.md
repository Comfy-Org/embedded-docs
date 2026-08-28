# WanMoveVisualizeTracks

WanMoveVisualizeTracks düğümü, hareket takip verilerini bir dizi görüntü veya video karesinin üzerine yerleştirir. Takip edilen noktaların hareket yollarını ve güncel konumlarını içeren görsel temsiller çizerek hareket verilerini görünür ve analiz edilmesi daha kolay hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görseller` | Üzerinde takip çizgilerinin görselleştirileceği girdi görüntüleri veya video kareleri dizisi. | IMAGE | Evet | - |
| `izler` | Nokta yollarını ve görünürlük bilgilerini içeren hareket takip verileri. Sağlanmazsa, girdi görüntüleri değiştirilmeden iletilir. | TRACKS | Hayır | - |
| `çizgi_çözünürlüğü` | Her takip için iz çizgisini çizerken kullanılacak önceki kare sayısı (varsayılan: 24). | INT | Evet | 1 - 1024 |
| `daire_boyutu` | Her takibin güncel konumuna çizilen dairenin boyutu (varsayılan: 12). | INT | Evet | 1 - 128 |
| `opaklık` | Çizilen takip katmanlarının opaklığı (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `çizgi_kalınlığı` | Takip yollarını çizmek için kullanılan çizgilerin kalınlığı (varsayılan: 16). | INT | Evet | 1 - 128 |

**Not:** Girdi görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısıyla eşleşmezse, görüntü dizisi takip uzunluğuna uyacak şekilde tekrarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Hareket takip verilerinin katman olarak görselleştirildiği görüntü dizisi. `tracks` sağlanmadıysa, orijinal girdi görüntüleri döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
