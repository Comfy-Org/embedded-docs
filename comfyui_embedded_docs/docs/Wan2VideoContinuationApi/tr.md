> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/tr.md)

ComfyUI Wan2VideoContinuation düğümü, bir giriş video klibinin sonundan itibaren sorunsuz bir şekilde devam eden yeni bir video segmenti oluşturur. Devamı sentezlemek için Wan 2.7 modelini kullanır ve isteğe bağlı olarak bitişi belirli bir hedef kareye yönlendirebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Evet | `"wan2.7-i2v"` | Kullanılacak video oluşturma modeli. |
| `model.prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. (varsayılan: boş dize) |
| `model.negative_prompt` | STRING | Evet | - | Kaçınılması gerekenleri tanımlayan olumsuz istem. (varsayılan: boş dize) |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı videosunun çözünürlüğü. |
| `model.duration` | INT | Evet | 2 ile 15 | Saniye cinsinden toplam çıktı süresi. Model, giriş klibinden sonra kalan süreyi doldurmak için devamı oluşturur. (varsayılan: 5) |
| `ilk_klip` | VIDEO | Evet | - | Devam edilecek giriş videosu. Süre: 2s-10s. Çıktının en boy oranı bu videodan alınır. |
| `son_kare` | IMAGE | Hayır | - | Son kare görüntüsü. Devam, bu kareye doğru geçiş yapacaktır. |
| `tohum` | INT | Evet | 0 ile 2147483647 | Oluşturma için kullanılacak tohum değeri. (varsayılan: 0) |
| `istem_genişlet` | BOOLEAN | Evet | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) |
| `filigran` | BOOLEAN | Evet | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) |

**Not:** `first_clip` giriş videosunun süresi 2 ile 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
| :--- | :--- | :--- |
| `output` | VIDEO | Oluşturulan video devamı. |

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
