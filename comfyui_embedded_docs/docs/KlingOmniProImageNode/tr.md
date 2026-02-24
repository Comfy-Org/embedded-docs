> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/tr.md)

Kling Omni Image (Pro) düğümü, Kling AI modelini kullanarak görüntüler oluşturur veya düzenler. Metin açıklamasına dayalı görüntüler oluşturur ve stil veya içeriği yönlendirmek için referans görüntüler sağlamanıza olanak tanır. Düğüm, görevi işleyen ve nihai görüntüyü döndüren harici bir API'ye istek gönderir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Evet | `"kling-image-o1"` | Görüntü oluşturma için kullanılacak belirli Kling AI modeli. |
| `prompt` | STRING | Evet | - | Görüntü içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. Metin uzunluğu 1 ile 2500 karakter arasında olmalıdır. |
| `resolution` | COMBO | Evet | `"1K"`<br>`"2K"` | Oluşturulan görüntü için hedef çözünürlük. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | Oluşturulan görüntü için istenen en-boy oranı (genişlik-yükseklik). |
| `reference_images` | IMAGE | Hayır | - | En fazla 10 adet ek referans görüntüsü. Her görüntünün hem genişliği hem de yüksekliği en az 300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
| :--- | :--- | :--- |
| `image` | IMAGE | Kling AI modeli tarafından oluşturulan veya düzenlenen nihai görüntü. |
