> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/tr.md)

GeminiImage2Node, Google'ın Vertex AI Gemini modelini kullanarak görüntüler oluşturur veya düzenler. API'ye bir metin istemi ve isteğe bağlı referans görüntüler veya dosyalar gönderir ve oluşturulan görüntüyü ve/veya bir metin açıklamasını döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin uyması gereken kısıtlamaları, stilleri veya detayları ekleyin. |
| `model` | COMBO | Evet | `"gemini-3-pro-image-preview"` | Oluşturma için kullanılacak belirli Gemini modeli. |
| `seed` | INT | Evet | 0 - 18446744073709551615 | Belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı vermek için elinden geleni yapar. Deterministik çıktı garanti edilmez. Modeli veya diğer ayarları değiştirmek, aynı seed değeriyle bile varyasyonlara neden olabilir. Varsayılan: 42. |
| `aspect_ratio` | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Çıktı görüntüsü için istenen en-boy oranı. 'auto' olarak ayarlanırsa, girdi görüntünüzün en-boy oranıyla eşleşir; eğer görüntü sağlanmazsa genellikle 16:9 kare bir görüntü oluşturulur. Varsayılan: "auto". |
| `resolution` | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini yükselticisi kullanılır. |
| `response_modalities` | COMBO | Evet | `"IMAGE+TEXT"`<br>`"IMAGE"` | Sadece görüntü çıktısı için 'IMAGE' seçin veya hem oluşturulan görüntüyü hem de bir metin yanıtını döndürmek için 'IMAGE+TEXT' seçin. |
| `images` | IMAGE | Hayır | Yok | İsteğe bağlı referans görüntü(leri). Birden fazla görüntü eklemek için Batch Images düğümünü kullanın (en fazla 14). |
| `files` | CUSTOM | Hayır | Yok | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden gelen girdileri kabul eder. |
| `system_prompt` | STRING | Hayır | Yok | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: Görüntü oluşturma için önceden tanımlanmış bir sistem istemi. |

**Kısıtlamalar:**

* `images` girişi maksimum 14 görüntüyü destekler. Daha fazlası sağlanırsa bir hata oluşur.
* `files` girişi, `GEMINI_INPUT_FILES` veri türünü çıktı olarak veren bir düğüme bağlanmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Gemini modeli tarafından oluşturulan veya düzenlenen görüntü. |
| `string` | STRING | Modelden gelen metin yanıtı. Eğer `response_modalities` "IMAGE" olarak ayarlanmışsa bu çıkış boş olacaktır. |
