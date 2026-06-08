ComfyUI Wan2VideoContinuation düğümü, bir giriş video klibinin sonundan itibaren sorunsuz bir şekilde devam eden yeni bir video segmenti oluşturur. Devamı sentezlemek için Wan 2.7 modelini kullanır ve isteğe bağlı olarak bitişi belirli bir hedef kareye yönlendirebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak video oluşturma modeli. | COMBO | Evet | `"wan2.7-i2v"` |
| `model.prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. (varsayılan: boş dize) | STRING | Evet | - |
| `model.negative_prompt` | Kaçınılması gerekenleri tanımlayan olumsuz istem. (varsayılan: boş dize) | STRING | Evet | - |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.duration` | Saniye cinsinden toplam çıktı süresi. Model, giriş klibinden sonra kalan süreyi doldurmak için devamı oluşturur. (varsayılan: 5) | INT | Evet | 2 ile 15 |
| `ilk_klip` | Devam edilecek giriş videosu. Süre: 2s-10s. Çıktının en boy oranı bu videodan alınır. | VIDEO | Evet | - |
| `son_kare` | Son kare görüntüsü. Devam, bu kareye doğru geçiş yapacaktır. | IMAGE | Hayır | - |
| `tohum` | Oluşturma için kullanılacak tohum değeri. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |
| `istem_genişlet` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) | BOOLEAN | Evet | - |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Evet | - |

**Not:** `first_clip` giriş videosunun süresi 2 ile 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video devamı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/tr.md)

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
