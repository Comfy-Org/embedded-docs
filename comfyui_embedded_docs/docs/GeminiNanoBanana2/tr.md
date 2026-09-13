# Nano Banana 2

Nano Banana 2 düğümü, Gemini 3.1 Flash Image modelini kullanarak Google Vertex API üzerinden görselleri eşzamanlı olarak üretir veya düzenler. Bir metin istemi ile isteğe bağlı referans görselleri veya dosyaları gönderir ve üretilen görseli, varsa eşlik eden metni ve isteğe bağlı olarak modelin düşünme sürecinden bir görseli döndürür. Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek görseli veya uygulanacak düzenlemeleri açıklayan metin istemi. Modelin uyması gereken tüm kısıtlamaları, stilleri veya ayrıntıları ekleyin. Boş veya yalnızca boşluk karakterlerinden oluşamaz. (varsayılan: boş) | STRING | Evet | N/A |
| `model` | Görsel üretimi için kullanılacak Gemini modeli. | COMBO | Evet | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | `seed` belirli bir değere sabitlendiğinde, model yinelenen istekler için aynı yanıtı sağlamak amacıyla elinden geleni yapar. Belirlenimci çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı `seed` değerini kullansanız bile yanıtta farklılıklara yol açabilir. Varsayılan olarak rastgele bir `seed` değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 - 18446744073709551615 |
| `aspect_ratio` | 'auto' olarak ayarlanırsa girdi görselinizin en boy oranıyla eşleşir; görsel sağlanmazsa genellikle 16:9 oranında bir görsel üretilir. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerel Gemini üst ölçekleyicisi kullanılır. | COMBO | Evet | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Modelin döndürdüğü içeriğin türünü belirler: "IMAGE" yalnızca bir görsel döndürür, "IMAGE+TEXT" ayrıca metin de döndürür. (gelişmiş) | COMBO | Evet | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Modelin akıl yürütme sürecinin derinliğini kontrol eder. | COMBO | Evet | "MINIMAL"<br>"HIGH" |
| `images` | İsteğe bağlı referans görsel(ler). Birden çok görsel eklemek için Batch Images düğümünü kullanın (en fazla 14). | IMAGE | Hayır | 1 - 14 görsel |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdileri kabul eder. | CUSTOM | Hayır | N/A |
| `system_prompt` | Bir yapay zekânın davranışını belirleyen temel talimatlar. (varsayılan: modele her zaman bir görsel üretmesini söyleyen önceden ayarlanmış bir istem) (gelişmiş) | STRING | Hayır | N/A |

**Not:** `images` girdisi en fazla 14 görseli destekler. Daha fazlası sağlanırsa düğüm bir hata verir. `prompt` girdisi boş veya yalnızca boşluk karakterlerinden oluşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Model tarafından üretilen veya düzenlenen birincil görsel. | IMAGE |
| `string` | Model tarafından döndürülen herhangi bir metin içeriği. | STRING |
| `thought_image` | Modelin düşünme sürecinden gelen ilk görsel. Yalnızca `thinking_level` HIGH olarak ayarlandığında ve IMAGE+TEXT modalitesiyle kullanılabilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/tr.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
