# WanMoveVisualizeTracks

WanMoveVisualizeTracks düğümü, hareket izleme verilerini bir görüntü veya video karesi dizisi üzerine yerleştirir. İzlenen noktaların görsel temsillerini, hareket yollarını ve mevcut konumlarını çizerek hareket verilerini görünür ve analiz edilmesi daha kolay hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İzlerin görselleştirileceği giriş görüntüleri veya video kareleri dizisi. | IMAGE | Evet | - |
| `tracks` | Nokta yollarını ve görünürlük bilgilerini içeren hareket izleme verileri. Sağlanmazsa, giriş görüntüleri değiştirilmeden geçirilir. | TRACKS | Hayır | - |
| `line_resolution` | Her iz için kuyruk yol çizgisi çizilirken kullanılacak önceki kare sayısı (varsayılan: 24). | INT | Evet | 1 - 1024 |
| `circle_size` | Her izin mevcut konumunda çizilen dairenin boyutu (varsayılan: 12). Gelişmiş parametre olarak işaretlenmiştir. | INT | Evet | 1 - 128 |
| `opacity` | Çizilen iz kaplamalarının opaklığı (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `line_width` | İz yollarını çizmek için kullanılan çizgilerin genişliği (varsayılan: 16). Gelişmiş parametre olarak işaretlenmiştir. | INT | Evet | 1 - 128 |

**Not:** Giriş görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısıyla eşleşmiyorsa, görüntü dizisi iz uzunluğuyla eşleşecek şekilde yinelenir.

**Not:** İz noktaları sınırlı sayıda yinelenen renkle çizilir ve bir noktanın görünürlük bayrağı o karede sıfır olduğunda nokta o karede atlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Hareket izleme verilerinin kaplamalar olarak görselleştirildiği görüntü dizisi. `tracks` sağlanmadıysa, orijinal giriş görüntüleri döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
