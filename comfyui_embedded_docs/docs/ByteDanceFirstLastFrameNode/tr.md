> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/tr.md)

Bu düğüm, bir metin istemi ile birlikte ilk ve son kare görüntülerini kullanarak bir video oluşturur. Açıklamanızı ve iki ana kareyi alarak, aralarında geçiş yapan eksiksiz bir video dizisi oluşturur. Düğüm, videonun çözünürlüğü, en-boy oranı, süresi ve diğer oluşturma parametreleri üzerinde kontrol sağlamak için çeşitli seçenekler sunar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | combo | seedance_1_lite | seedance_1_lite | Model adı |
| `prompt` | STRING | string | - | - | Videoyu oluşturmak için kullanılan metin istemi. |
| `first_frame` | IMAGE | image | - | - | Video için kullanılacak ilk kare. |
| `last_frame` | IMAGE | image | - | - | Video için kullanılacak son kare. |
| `resolution` | COMBO | combo | - | 480p, 720p, 1080p | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | COMBO | combo | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | Çıktı videosunun en-boy oranı. |
| `duration` | INT | slider | 5 | 3-12 | Çıktı videosunun saniye cinsinden süresi. |
| `seed` | INT | number | 0 | 0-2147483647 | Oluşturma için kullanılacak seed değeri. (isteğe bağlı) |
| `camera_fixed` | BOOLEAN | boolean | False | - | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, kamerayı sabitleme talimatını isteminize ekler, ancak gerçek etkiyi garanti etmez. (isteğe bağlı) |
| `watermark` | BOOLEAN | boolean | True | - | Videoya "AI generated" (Yapay Zeka ile Oluşturulmuştur) filigranı eklenip eklenmeyeceği. (isteğe bağlı) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |