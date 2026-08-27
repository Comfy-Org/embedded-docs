# Nano Banana Pro (Google Gemini Image)

GeminiImage2Node, Google Vertex AI Gemini modelini kullanarak görüntüler oluşturur veya düzenler. Bir metin istemi ve isteğe bağlı olarak referans görüntüler veya dosyalar sağlarsınız; düğüm bunları API'ye gönderir ve oluşturulan görüntüyü, istendiğinde ayrıca bir metin yanıtını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken kısıtlamaları, stilleri veya ayrıntıları ekleyin. İstem, boşluk karakterleri kaldırıldıktan sonra en az bir karakter içermelidir. | STRING | Evet | N/A |
| `model` | Oluşturma için kullanılacak belirli Gemini modeli. "Nano Banana 2 (Gemini 3.1 Flash Image)" seçeneği dahili olarak `gemini-3.1-flash-image` modeline, "gemini-3-pro-image-preview" ise `gemini-3-pro-image` modeline eşlenir. | COMBO | Evet | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Tohum (seed) belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamaya çalışır. Belirleyici (deterministik) çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. Varsayılan: 42. | INT | Evet | 0 ile 18446744073709551615 |
| `aspect_ratio` | 'auto' olarak ayarlanırsa, girdi görüntünüzün en-boy oranıyla eşleşir; hiçbir görüntü sağlanmazsa, genellikle 16:9 en-boy oranında bir görüntü oluşturulur. Varsayılan: "auto". | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini büyütücü kullanılır. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Yalnızca görüntü çıktısı için 'IMAGE' veya hem oluşturulan görüntüyü hem de metin yanıtını döndürmek için 'IMAGE+TEXT' seçeneğini belirleyin. | COMBO | Evet | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | İsteğe bağlı referans görüntü(ler)i. Birden fazla görüntü eklemek için Batch Images düğümünü kullanın (en fazla 14). | IMAGE | Hayır | N/A |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel yönergeler. Varsayılan: Görüntü üretimi için önceden tanımlanmış bir sistem istemi. | STRING | Hayır | N/A |

**Kısıtlamalar:**

* `images` girdisi en fazla 14 görüntü destekler. Daha fazlası sağlanırsa bir hata oluşturulur.
* 10'dan fazla görüntü sağlandığında, ilk 10'u URL referansları olarak yüklenir ve kalan görüntüler istekte satır içi (inline) olarak gönderilir.
* `files` girdisi, `GEMINI_INPUT_FILES` veri türünü çıktı olarak veren bir düğüme bağlanmalıdır.
* `response_modalities` "IMAGE" olarak ayarlandığında, yalnızca görüntü döndürülür ve metin çıktısı boş olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Gemini modeli tarafından oluşturulan veya düzenlenen görüntü. | IMAGE |
| `string` | Modelden gelen metin yanıtı. `response_modalities` "IMAGE" olarak ayarlanırsa bu çıktı boş olur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/tr.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
