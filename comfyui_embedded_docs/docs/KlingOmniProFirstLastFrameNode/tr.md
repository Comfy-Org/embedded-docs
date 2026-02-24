> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/tr.md)

Bu düğüm, bir video oluşturmak için Kling AI modelini kullanır. Bir başlangıç görseli ve bir metin istemi gerektirir. İsteğe bağlı olarak, videonun içeriğini ve stilini yönlendirmek için bir bitiş görseli veya en fazla altı referans görseli sağlayabilirsiniz. Düğüm, belirli bir süre ve çözünürlükte bir video oluşturmak için bu girdileri işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling AI modeli. |
| `prompt` | STRING | Evet | - | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz tanımlamalar içerebilir. |
| `duration` | INT | Evet | 3 ila 10 | Oluşturulan videonun istenen uzunluğu, saniye cinsinden (varsayılan: 5). |
| `first_frame` | IMAGE | Evet | - | Video dizisi için başlangıç görseli. |
| `end_frame` | IMAGE | Hayır | - | Video için isteğe bağlı bir bitiş karesi. Bu, `reference_images` ile aynı anda kullanılamaz. |
| `reference_images` | IMAGE | Hayır | - | En fazla 6 ek referans görseli. |
| `resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Oluşturulan video için çıktı çözünürlüğü (varsayılan: "1080p"). |

**Önemli Kısıtlamalar:**

* `end_frame` girdisi, `reference_images` girdisi ile aynı anda kullanılamaz.
* Bir `end_frame` veya herhangi bir `reference_images` sağlamazsanız, `duration` yalnızca 5 veya 10 saniye olarak ayarlanabilir.
* Tüm girdi görselleri (`first_frame`, `end_frame` ve herhangi bir `reference_images`) hem genişlik hem de yükseklikte minimum 300 piksel boyutuna sahip olmalıdır.
* Tüm girdi görsellerinin en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
* `reference_images` girdisi aracılığıyla en fazla 6 görsel sağlanabilir.
* `prompt` metni 1 ile 2500 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
