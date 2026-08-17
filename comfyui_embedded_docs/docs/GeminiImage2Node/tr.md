# Nano Banana Pro (Google Gemini Image)

Nano Banana Pro (Google Gemini Image), Google'ın Vertex AI Gemini görüntü modellerini kullanarak görüntüler oluşturur veya düzenler. Metin istemini, isteğe bağlı referans görüntüler veya dosyalarla birlikte Gemini API'sine gönderir ve oluşturulan görüntüyü isteğe bağlı bir metin yanıtıyla birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken kısıtlamaları, stilleri veya ayrıntıları ekleyin. Varsayılan: boş dize. | STRING | Evet | N/A |
| `model` | Kullanılacak Gemini görüntü modeli. "Nano Banana 2 (Gemini 3.1 Flash Image)" seçeneği API'ye `gemini-3.1-flash-image` olarak gönderilir; "gemini-3-pro-image-preview" seçeneği ise `gemini-3-pro-image` olarak gönderilir. | COMBO | Evet | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamaya çalışır. Deterministik çıktı garanti edilmez. Modeli veya diğer parametre ayarlarını değiştirmek, aynı seed değerinde bile yanıtta farklılıklara neden olabilir. Varsayılan: 42. | INT | Evet | 0 ila 18446744073709551615 |
| `aspect_ratio` | Çıktı görüntüsünün istenen en-boy oranı. "auto" olarak ayarlanırsa, giriş görüntünüzün en-boy oranıyla eşleşir; görüntü sağlanmazsa, genellikle 16:9 en-boy oranında bir görüntü oluşturulur. Varsayılan: "auto". | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için Gemini'nin yerleşik yükselticisi (upscaler) kullanılır. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Yalnızca görüntü çıktısı için "IMAGE" veya hem oluşturulan görüntüyü hem de metin yanıtını döndürmek için "IMAGE+TEXT" seçeneğini belirleyin. | COMBO | Evet | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Görsel bağlam olarak kullanılan isteğe bağlı referans görüntü(ler). Birden fazla görüntü eklemek için Batch Images düğümünü kullanın (en fazla 14). | IMAGE | Hayır | N/A |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. Varsayılan: modele her zaman bir görüntü oluşturmasını söyleyen önceden tanımlanmış bir sistem istemi. | STRING | Hayır | N/A |

**Kısıtlamalar:**

* `prompt` alanı, baştaki ve sondaki boşluklar kaldırıldıktan sonra boş olmamalıdır; aksi takdirde bir hata oluşturulur.
* `images` girdisi en fazla 14 görüntü kabul eder. 14'ten fazla görüntü sağlanırsa bir hata oluşturulur.
* `files` girdisi, `GEMINI_INPUT_FILES` veri türünü çıktı olarak veren bir düğüme bağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Gemini modeli tarafından oluşturulan veya düzenlenen görüntü. | IMAGE |
| `string` | Modelden gelen metin yanıtı. `response_modalities` "IMAGE" olarak ayarlandığında bu çıktı boştur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/tr.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
