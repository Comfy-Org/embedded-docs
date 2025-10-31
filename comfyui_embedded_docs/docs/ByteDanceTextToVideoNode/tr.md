> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/tr.md)

ByteDance Text to Video düğümü, metin istemlerine dayalı olarak bir API aracılığıyla ByteDance modellerini kullanarak videolar oluşturur. Bir metin açıklaması ve çeşitli video ayarlarını girdi olarak alır, ardından sağlanan özelliklere uygun bir video oluşturur. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | Combo | seedance_1_pro | Text2VideoModelName seçenekleri | Model adı |
| `prompt` | STRING | String | - | - | Videoyu oluşturmak için kullanılan metin istemi. |
| `resolution` | STRING | Combo | - | ["480p", "720p", "1080p"] | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | STRING | Combo | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | Çıktı videosunun en-boy oranı. |
| `duration` | INT | Int | 5 | 3-12 | Çıktı videosunun saniye cinsinden süresi. |
| `seed` | INT | Int | 0 | 0-2147483647 | Oluşturma için kullanılacak seed değeri. (İsteğe bağlı) |
| `camera_fixed` | BOOLEAN | Boolean | False | - | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, kamerayı sabitleme talimatını isteminize ekler, ancak gerçek etkiyi garanti etmez. (İsteğe bağlı) |
| `watermark` | BOOLEAN | Boolean | True | - | Videoya "AI generated" (Yapay Zeka ile Oluşturuldu) filigranı eklenip eklenmeyeceği. (İsteğe bağlı) |

**Parametre Kısıtlamaları:**

- `prompt` parametresi, boşluklar kaldırıldıktan sonra en az 1 karakter içermelidir
- `prompt` parametresi şu metin parametrelerini içeremez: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark"
- `duration` parametresi 3 ile 12 saniye arasındaki değerlerle sınırlıdır
- `seed` parametresi 0 ile 2,147,483,647 arasındaki değerleri kabul eder

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |