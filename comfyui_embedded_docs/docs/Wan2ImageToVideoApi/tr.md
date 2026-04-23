> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/tr.md)

Wan 2.7 Görüntüden Videoya düğümü, bir ilk kare görüntüsünden başlayarak bir video oluşturur. İsteğe bağlı olarak, iki kare arasında geçiş oluşturmak için bir son kare görüntüsü veya videonun hareketini ve zamanlamasını yönlendirmek için bir ses dosyası sağlayabilirsiniz. Düğüm, metin açıklamanıza dayanarak sahneyi canlandırmak için bir yapay zeka modeli kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | COMBO | Evet | `"wan2.7-i2v"` | Video oluşturma için kullanılacak yapay zeka modeli. |
| `model.prompt` | STRING | Evet | - | Videoda istediğiniz öğelerin ve görsel özelliklerin metin açıklaması. İngilizce ve Çinceyi destekler. |
| `model.negative_prompt` | STRING | Evet | - | Modelin kaçınmasını istediğiniz öğelerin veya özelliklerin metin açıklaması. |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı videosunun çözünürlüğü. |
| `model.duration` | INT | Evet | 2 ila 15 | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). |
| `first_frame` | IMAGE | Evet | - | Videonun ilk karesi olarak kullanılacak görüntü. Çıktı videosunun en-boy oranı bu görüntüden türetilir. |
| `last_frame` | IMAGE | Hayır | - | Son kare olarak kullanılacak isteğe bağlı bir görüntü. Sağlandığında model, ilk kareden bu son kareye geçiş yapan bir video oluşturur. |
| `audio` | AUDIO | Hayır | - | Video oluşturmayı yönlendirmek için isteğe bağlı bir ses dosyası; dudak senkronizasyonu veya ritim eşleştirmeli hareket için kullanışlıdır. Süre 2 ila 30 saniye arasında olmalıdır. Sağlanmazsa model, eşleşen arka plan müziği veya ses efektleri oluşturur. |
| `seed` | INT | Evet | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 0). |
| `prompt_extend` | BOOLEAN | Evet | - | Etkinleştirildiğinde düğüm, metin isteminizi geliştirmek için yapay zeka yardımı kullanır (varsayılan: True). Bu gelişmiş bir ayardır. |
| `watermark` | BOOLEAN | Evet | - | Etkinleştirildiğinde, son videoya yapay zeka tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). Bu gelişmiş bir ayardır. |

**Not:** `audio` girişinin bir süre sınırlaması vardır. Sağlanırsa, ses dosyası 2 ila 30 saniye uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası. |