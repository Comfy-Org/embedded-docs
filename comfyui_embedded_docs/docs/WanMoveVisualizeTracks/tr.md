WanMoveVisualizeTracks düğümü, hareket takip verilerini bir dizi görüntü veya video karesi üzerine yerleştirir. Takip edilen noktaların hareket yolları ve mevcut konumları dahil olmak üzere görsel temsillerini çizerek hareket verilerini görünür hale getirir ve analiz edilmesini kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görseller` | İzlerin görselleştirileceği giriş görüntüleri veya video kareleri dizisi. | IMAGE | Evet | - |
| `izler` | Nokta yolları ve görünürlük bilgilerini içeren hareket takip verileri. Sağlanmazsa, giriş görüntüleri değiştirilmeden iletilir. | TRACKS | Hayır | - |
| `çizgi_çözünürlüğü` | Her bir iz için takip çizgisi çizilirken kullanılacak önceki kare sayısı (varsayılan: 24). | INT | Evet | 1 - 1024 |
| `daire_boyutu` | Her bir izin mevcut konumunda çizilen dairenin boyutu (varsayılan: 12). | INT | Evet | 1 - 128 |
| `opaklık` | Çizilen iz katmanlarının opaklığı (varsayılan: 0.75). | FLOAT | Evet | 0.0 - 1.0 |
| `çizgi_kalınlığı` | İz yollarını çizmek için kullanılan çizgilerin genişliği (varsayılan: 16). | INT | Evet | 1 - 128 |

**Not:** Giriş görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısıyla eşleşmezse, görüntü dizisi iz uzunluğuna uyacak şekilde tekrarlanır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Hareket takip verilerinin katman olarak görselleştirildiği görüntü dizisi. Hiçbir `izler` sağlanmadıysa, orijinal giriş görüntüleri döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
