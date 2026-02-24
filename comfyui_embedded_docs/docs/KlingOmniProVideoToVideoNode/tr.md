> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/tr.md)

Bu düğüm, bir giriş videosu ve isteğe bağlı referans görsellerine dayanarak yeni bir video oluşturmak için Kling AI modelini kullanır. İstenilen içeriği tanımlayan bir metin istemi sağlarsınız ve düğüm referans videosunu buna göre dönüştürür. Ayrıca çıktının stilini ve içeriğini yönlendirmek için en fazla dört ek referans görselini dahil edebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling modeli. |
| `prompt` | STRING | Evet | Yok | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan video için istenen en-boy oranı. |
| `duration` | INT | Evet | 3 ila 10 | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 3). |
| `reference_video` | VIDEO | Evet | Yok | Referans olarak kullanılacak video. |
| `keep_original_sound` | BOOLEAN | Evet | Yok | Referans videosundaki sesin çıktıda korunup korunmayacağını belirler (varsayılan: True). |
| `reference_images` | IMAGE | Hayır | Yok | En fazla 4 ek referans görseli. |
| `resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Oluşturulan video için çözünürlük (varsayılan: "1080p"). |

**Parametre Kısıtlamaları:**

* `prompt` 1 ile 2500 karakter arasında olmalıdır.
* `reference_video` süresi 3.0 ile 10.05 saniye arasında olmalıdır.
* `reference_video` boyutları 720x720 ile 2160x2160 piksel arasında olmalıdır.
* En fazla 4 `reference_images` sağlanabilir. Her görsel en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Yeni oluşturulan video. |
