> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/tr.md)

WanMoveVisualizeTracks düğümü, hareket takip verilerini bir görüntü dizisi veya video kareleri üzerine bindirir. İzlenen noktaların hareket yollarını ve mevcut konumlarını içeren görsel temsillerini çizer, böylece hareket verilerini görünür ve analiz etmesi kolay hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | İzlerin görselleştirileceği giriş görüntüleri veya video kareleri dizisi. |
| `tracks` | TRACKS | Hayır | - | Nokta yollarını ve görünürlük bilgilerini içeren hareket takip verisi. Sağlanmazsa, giriş görüntüleri değiştirilmeden geçirilir. |
| `line_resolution` | INT | Evet | 1 - 1024 | Her bir iz için kuyruk yol çizgisi çizerken kullanılacak önceki kare sayısı (varsayılan: 24). |
| `circle_size` | INT | Evet | 1 - 128 | Her bir izin mevcut konumunda çizilen dairenin boyutu (varsayılan: 12). |
| `opacity` | FLOAT | Evet | 0.0 - 1.0 | Çizilen iz bindirmelerinin opaklığı (varsayılan: 0.75). |
| `line_width` | INT | Evet | 1 - 128 | İz yollarını çizmek için kullanılan çizgilerin kalınlığı (varsayılan: 16). |

**Not:** Giriş görüntülerinin sayısı, sağlanan `tracks` verisindeki kare sayısı ile eşleşmezse, görüntü dizisi iz uzunluğu ile eşleşecek şekilde tekrarlanacaktır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Hareket takip verisinin bindirme olarak görselleştirildiği görüntü dizisi. Eğer `tracks` sağlanmadıysa, orijinal giriş görüntüleri döndürülür. |
