Wan 2.7 Görüntüden Videoya düğümü, bir başlangıç karesi görüntüsünden başlayarak bir video oluşturur. İsteğe bağlı olarak, iki kare arasında geçiş oluşturmak için bir bitiş karesi görüntüsü veya videonun hareketini ve zamanlamasını yönlendirmek için bir ses dosyası sağlayabilirsiniz. Düğüm, metin açıklamanıza dayanarak sahneyi canlandırmak için bir yapay zeka modeli kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak yapay zeka modeli. | COMBO | Evet | `"wan2.7-i2v"` |
| `model.prompt` | Videoda görmek istediğiniz öğelerin ve görsel özelliklerin metin açıklaması. İngilizce ve Çinceyi destekler. | STRING | Evet | - |
| `model.negative_prompt` | Modelin kaçınmasını istediğiniz öğelerin veya özelliklerin metin açıklaması. | STRING | Evet | - |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ila 15 |
| `first_frame` | Videonun ilk karesi olarak kullanılacak görüntü. Çıktı videosunun en-boy oranı bu görüntüden türetilir. | IMAGE | Evet | - |
| `last_frame` | Son kare olarak kullanılacak isteğe bağlı bir görüntü. Sağlandığında model, ilk kareden bu son kareye geçiş yapan bir video oluşturur. | IMAGE | Hayır | - |
| `audio` | Video oluşturmayı yönlendirmek için isteğe bağlı bir ses dosyası; dudak senkronizasyonu veya ritim eşleştirmeli hareket için kullanışlıdır. Süre 2 ila 30 saniye arasında olmalıdır. Sağlanmazsa model, eşleşen arka plan müziği veya ses efektleri oluşturur. | AUDIO | Hayır | - |
| `seed` | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 0). | INT | Evet | 0 ila 2147483647 |
| `prompt_extend` | Etkinleştirildiğinde düğüm, metin isteminizi geliştirmek için yapay zeka yardımı kullanır (varsayılan: True). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | - |
| `watermark` | Etkinleştirildiğinde, son videoya yapay zeka tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | - |

**Not:** `audio` girişinin bir süre sınırlaması vardır. Sağlanırsa, ses dosyası 2 ila 30 saniye uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`
