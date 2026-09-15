# Nano Banana Pro (Google Gemini Image)

Google Vertex AI Gemini API'si aracılığıyla görselleri eşzamanlı olarak oluşturun veya düzenleyin. Bir metin istemi sağlarsınız ve isteğe bağlı olarak referans görseller veya Gemini girdi dosyaları ekleyebilirsiniz. Düğüm, oluşturulan görseli ve seçilen yanıt moduna bağlı olarak bir metin yanıtı döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görseli veya uygulanacak düzenlemeleri açıklayan metin istemi. Modelin uyması gereken tüm kısıtlamaları, stilleri veya ayrıntıları ekleyin. Boşluklar kaldırıldıktan sonra istem en az bir karakter içermelidir. | STRING | Evet | N/A |
| `model` | Oluşturma için kullanılacak Gemini modeli. "Nano Banana 2 (Gemini 3.1 Flash Image)" seçeneği `gemini-3.1-flash-image` olarak gönderilir; "gemini-3-pro-image-preview" ise `gemini-3-pro-image` olarak gönderilir. | COMBO | Evet | "gemini-3-pro-image-preview"<br>"Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Seed belirli bir değere sabitlendiğinde, model yinelenen istekler için aynı yanıtı sağlamak adına elinden geleni yapar. Deterministik çıktı garanti edilmez. Ayrıca, sıcaklık gibi model veya parametre ayarlarının değiştirilmesi, aynı seed değerini kullansanız bile yanıtta değişikliklere neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. Varsayılan: 42. | INT | Evet | 0 ile 18446744073709551615 |
| `aspect_ratio` | Eğer 'auto' olarak ayarlanırsa, girdi görselinizin en-boy oranıyla eşleşir; görsel sağlanmazsa genellikle 16:9 kare oluşturulur. Varsayılan: "auto". | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini büyütücüsü kullanılır. | COMBO | Evet | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Yalnızca görsel çıktısı için 'IMAGE' veya hem oluşturulan görseli hem de metin yanıtını döndürmek için 'IMAGE+TEXT' seçin. Gelişmiş ayar. | COMBO | Evet | "IMAGE+TEXT"<br>"IMAGE" |
| `images` | İsteğe bağlı referans görsel(ler). Birden fazla görsel eklemek için Batch Images düğümünü kullanın (en fazla 14). | IMAGE | Hayır | N/A |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `system_prompt` | Bir yapay zekânın davranışını belirleyen temel talimatlar. Varsayılan: görsel oluşturma için önceden tanımlanmış bir sistem istemi. Gelişmiş ayar. | STRING | Hayır | N/A |

**Kısıtlamalar:**

* `images` girdisi en fazla 14 görseli destekler. Daha fazlası sağlanırsa bir hata oluşur.
* 10'dan fazla görsel sağlandığında, ilk 10 görsel URL referansı olarak yüklenir ve kalan görseller istekte satır içi olarak gönderilir.
* `files` girdisi, `GEMINI_INPUT_FILES` veri türünü çıkaran bir düğüme bağlanmalıdır.
* `response_modalities` `"IMAGE"` olarak ayarlandığında, yalnızca görsel döndürülür ve metin çıktısı boş olur.
* `prompt` girdisi doğrulanır ve boşluklar kaldırıldıktan sonra en az bir karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Gemini modeli tarafından oluşturulan veya düzenlenen görsel. | IMAGE |
| `string` | Modelden gelen metin yanıtı. `response_modalities` `"IMAGE"` olarak ayarlanırsa bu çıktı boş olur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/tr.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
