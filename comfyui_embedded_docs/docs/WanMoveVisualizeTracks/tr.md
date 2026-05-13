> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

WanMoveVisualizeTracks düğümü, hareket takip verilerini bir dizi görüntü veya video karesi üzerine yerleştirir. Takip edilen noktaların hareket yolları ve mevcut konumları dahil olmak üzere görsel temsillerini çizerek hareket verilerini görünür hale getirir ve analiz edilmesini kolaylaştırır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görseller` | IMAGE | Evet | - | İzlerin görselleştirileceği giriş görüntüleri veya video kareleri dizisi. |
| `izler` | TRACKS | Hayır | - | Nokta yolları ve görünürlük bilgilerini içeren hareket takip verileri. Sağlanmazsa, giriş görüntüleri değiştirilmeden iletilir. |
| `çizgi_çözünürlüğü` | INT | Evet | 1 - 1024 | Her bir iz için takip çizgisi çizilirken kullanılacak önceki kare sayısı (varsayılan: 24). |
| `daire_boyutu` | INT | Evet | 1 - 128 | Her bir izin mevcut konumunda çizilen dairenin boyutu (varsayılan: 12). |
| `opaklık` | FLOAT | Evet | 0.0 - 1.0 | Çizilen iz katmanlarının opaklığı (varsayılan: 0.75). |
| `çizgi_kalınlığı` | INT | Evet | 1 - 128 | İz yollarını çizmek için kullanılan çizgilerin genişliği (varsayılan: 16). |

**Not:** Giriş görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısıyla eşleşmezse, görüntü dizisi iz uzunluğuna uyacak şekilde tekrarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Hareket takip verilerinin katman olarak görselleştirildiği görüntü dizisi. Hiçbir `izler` sağlanmadıysa, orijinal giriş görüntüleri döndürülür. |

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
