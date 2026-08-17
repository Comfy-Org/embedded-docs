# Nano Banana 2

Bu düğüm, Google'ın Vertex AI Gemini modelini (Nano Banana 2 / Gemini 3.1 Flash Image) kullanarak görüntüleri eşzamanlı olarak oluşturur veya düzenler. API'ye isteğe bağlı referans görüntüleri veya dosyalarla birlikte bir metin istemi gönderir ve oluşturulan görüntüyü, varsa eşlik eden metni ve isteğe bağlı olarak modelin düşünme sürecinden bir görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken kısıtlamaları, stilleri veya ayrıntıları ekleyin. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | N/A |
| `model` | Görüntü oluşturma için kullanılacak belirli Gemini modeli. Mevcut tek seçenek, `gemini-3.1-flash-image-preview` modeline karşılık gelir. | COMBO | Evet | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak üzere elinden gelenin en iyisini yapar. Deterministik çıktı garanti edilmez. Ayrıca, model veya sıcaklık gibi parametre ayarlarının değiştirilmesi, aynı seed değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 to 18446744073709551615 |
| `aspect_ratio` | 'auto' olarak ayarlanırsa, girdi görüntünüzün en-boy oranına uyar; görüntü sağlanmazsa, genellikle 16:9 en-boy oranında bir görüntü oluşturulur. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini yükseltici kullanılır. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Modelin döndürdüğü içerik türünü belirler: `IMAGE` yalnızca görüntüyü döndürür, `IMAGE+TEXT` ayrıca modelin akıl yürütme metnini de döndürür. (gelişmiş) | COMBO | Evet | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Modelin akıl yürütme sürecinin derinliğini kontrol eder. | COMBO | Evet | `"MINIMAL"`<br>`"HIGH"` |
| `images` | İsteğe bağlı referans görüntü(ler)i. Birden fazla görüntü eklemek için Batch Images düğümünü kullanın (en fazla 14). | IMAGE | Hayır | En fazla 14 görüntü |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdileri kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. (varsayılan: modelin her zaman bir görüntü üretmesini gerektiren yerleşik talimatlar) (gelişmiş) | STRING | Hayır | N/A |

**Not:** `images` girdisi en fazla 14 görüntü kabul eder; daha fazlası sağlanırsa hata oluşur. 10'dan fazla referans görüntüsü sağlandığında, ilk 10'u dosya URL'si olarak gönderilir ve geri kalan görüntüler satır içi veri olarak gönderilir. `prompt`, boşluklar çıkarıldıktan sonra boş olmamalıdır. Bu düğüm kullanımdan kaldırılmış (deprecated) olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Model tarafından oluşturulan veya düzenlenen ana görüntü. | IMAGE |
| `string` | Model tarafından döndürülen herhangi bir metin içeriği. | STRING |
| `thought_image` | Modelin düşünme sürecinden ilk görüntü. Yalnızca thinking_level HIGH ve IMAGE+TEXT kipiyle kullanılabilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/tr.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
