Kling Omni Image (Pro) düğümü, en yeni Kling AI modelini kullanarak görseller oluşturur veya düzenler. Bir metin açıklamasına dayanarak görseller üretir ve isteğe bağlı olarak stili veya içeriği yönlendirmek için referans görselleri kullanabilir. Düğüm, harici bir API'ye istek gönderir; API, görevi işler ve nihai görsel(ler)i döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Görsel oluşturma için kullanılacak belirli Kling AI modeli. | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-image-o1"` |
| `prompt` | Görsel içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Metin 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | - |
| `resolution` | Oluşturulan görsel için hedef çözünürlük. Not: 4K çözünürlük `kling-image-o1` modeli tarafından desteklenmez. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `aspect_ratio` | Oluşturulan görsel için istenen en-boy oranı (genişlik/yükseklik). | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` |
| `seri_sayısı` | Bir dizi görsel oluşturun. Bu özellik `kling-image-o1` modeli tarafından desteklenmez. (varsayılan: "disabled") | COMBO | Evet | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |
| `reference_images` | En fazla 10 adet ek referans görseli. Her görselin genişlik ve yüksekliği en az 300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Hayır | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Kling AI modeli tarafından oluşturulan veya düzenlenen nihai görsel(ler). Bir dizi talep edilmişse, birden fazla görsel bir toplu iş olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `7bbed260436bc60e284c99e091cd28b2b0cf50e98e876f94278f1ac2834e61f8`
