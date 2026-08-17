# WanMoveVisualizeTracks

WanMoveVisualizeTracks düğümü, hareket takip verilerini bir dizi görüntü veya video karesi üzerine çizer. Her takip edilen noktanın mevcut konumuna bir daire yerleştirir ve noktanın son karelerde nerede hareket ettiğini gösteren, solan bir yol çizgisi çizer. Takip verisi sağlanmazsa, giriş görüntüleri değiştirilmeden döndürülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Takip verilerinin görselleştirileceği giriş görüntüleri veya video kareleri dizisi. | IMAGE | Evet | - |
| `tracks` | Nokta konumlarını ve görünürlük bilgilerini içeren hareket takip verisi. Sağlanmazsa, giriş görüntüleri değiştirilmeden iletilir. | TRACKS | Hayır | - |
| `line_resolution` | Her takip için iz çizgisini çizerken kullanılacak önceki kare sayısı (varsayılan: 24). | INT | Evet | 1 - 1024 |
| `circle_size` | Her takip edilen noktanın mevcut konumuna çizilen dairenin boyutu (varsayılan: 12). | INT | Evet | 1 - 128 |
| `opacity` | Çizilen takip katmanlarının opaklığı (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `line_width` | Takip yollarını çizmek için kullanılan çizgilerin genişliği (varsayılan: 16). | INT | Evet | 1 - 128 |

**Not:** Giriş görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısıyla eşleşmezse, giriş görüntü dizisi takip verisiyle hizalanacak şekilde tekrarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Hareket takip verilerinin katman olarak çizildiği görüntü dizisi. `tracks` sağlanmadıysa, orijinal giriş görüntüleri değiştirilmeden döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
