> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/tr.md)

ByteDance Image to Video düğümü, bir giriş görseli ve metin istemi aracılığıyla ByteDance modellerini kullanarak bir API üzerinden video oluşturur. Bir başlangıç görsel karesi alır ve sağlanan açıklamayı takip eden bir video dizisi oluşturur. Düğüm, video çözünürlüğü, en-boy oranı, süre ve diğer oluşturma parametreleri için çeşitli özelleştirme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Image2VideoModelName seçenekleri | Model adı |
| `prompt` | STRING | STRING | - | - | Videoyu oluşturmak için kullanılan metin istemi. |
| `image` | IMAGE | IMAGE | - | - | Video için kullanılacak ilk kare. |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | Çıktı videosunun en-boy oranı. |
| `duration` | INT | INT | 5 | 3-12 | Çıktı videosunun saniye cinsinden süresi. |
| `seed` | INT | INT | 0 | 0-2147483647 | Oluşturma için kullanılacak seed değeri. |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitleme talimatını ekler, ancak gerçek etkiyi garanti etmez. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Videoya "AI generated" (Yapay Zeka ile Oluşturulmuştur) filigranı eklenip eklenmeyeceği. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi görseli ve istem parametrelerine dayalı olarak oluşturulan video dosyası. |