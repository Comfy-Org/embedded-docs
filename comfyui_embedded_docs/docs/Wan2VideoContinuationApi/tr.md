> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/tr.md)

Wan 2.7 Video Devam Düğümü, bir giriş video klibinin sonundan itibaren sorunsuz bir şekilde devam eden yeni bir video segmenti oluşturur. Devamı sentezlemek için Wan 2.7 modelini kullanır ve isteğe bağlı olarak bitişi belirli bir hedef kareye yönlendirebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Evet | `"wan2.7-i2v"` | Kullanılacak video oluşturma modeli. |
| `model.prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. (varsayılan: boş dize) |
| `model.negative_prompt` | STRING | Evet | - | Kaçınılması gerekenleri tanımlayan olumsuz istem. (varsayılan: boş dize) |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı videosunun çözünürlüğü. |
| `model.duration` | INT | Evet | 2 ila 15 | Saniye cinsinden toplam çıktı süresi. Model, giriş klibinden sonra kalan süreyi doldurmak için devamı oluşturur. (varsayılan: 5) |
| `first_clip` | VIDEO | Evet | - | Devam edilecek giriş videosu. Süre: 2sn-10sn. Çıktı en-boy oranı bu videodan türetilir. |
| `last_frame` | IMAGE | Hayır | - | Son kare görüntüsü. Devam, bu kareye doğru geçiş yapacaktır. |
| `seed` | INT | Evet | 0 ila 2147483647 | Oluşturma için kullanılacak tohum değeri. (varsayılan: 0) |
| `prompt_extend` | BOOLEAN | Evet | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) |
| `watermark` | BOOLEAN | Evet | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) |

**Not:** `first_clip` giriş videosunun süresi 2 ila 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
| :--- | :--- | :--- |
| `output` | VIDEO | Oluşturulan video devamı. |