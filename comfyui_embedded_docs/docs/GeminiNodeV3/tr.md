# GeminiNodeV3

Google'ın Gemini modelleriyle metin yanıtları üretin. Bir metin istemi ve isteğe bağlı olarak çok modlu bağlam amacıyla bir veya daha fazla görsel, ses klibi, video ya da dosya sağlayın. Seçilen model, hangi ek ayarların görüneceğini belirler.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı üretmek için kullanılan Gemini modeli. Seçilen model, hangi ek girdilerin gösterileceğini belirler. | DYNAMIC_COMBO | Evet | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |

### Medya Girdileri

Bu büyütülebilir medya girdileri her model seçeneği için kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 16 görsel. Büyütülebilir yuva: görselleri `image_1` ile `image_16` arasına bağlayın. | IMAGE | Hayır | En fazla 16 görsel |
| `audio` | Model için bağlam olarak kullanılacak isteğe bağlı ses klibi. Büyütülebilir yuva: `audio_1`. | AUDIO | Hayır | 1 ses klibi |
| `video` | Model için bağlam olarak kullanılacak isteğe bağlı video klibi. Büyütülebilir yuva: `video_1`. | VIDEO | Hayır | 1 video klibi |

### Gemini 3.8 Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin (en az bir boşluk olmayan karakter içermelidir) |
| `video_processing` | Modelin eklenen videoyu nasıl okuduğu. `static`, kareleri sabit bir hızda örnekler ve tümünü bağlam olarak gönderir; `agentic` ise modelin zaman çizelgesinde kendi başına gezinmesine ve yalnızca ihtiyaç duyduğu kareleri, sesi veya transkripti yüklemesine olanak tanır; bu, uzun videolarda çok daha az girdi tokenı maliyeti çıkarır. | COMBO | Evet | `"static"`<br>`"agentic"` (varsayılan: `"static"`) |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokenı maliyeti çıkarır ve daha yavaştır. | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (varsayılan: `"MEDIUM"`) |
| `max_output_tokens` | Modelin dahili düşünmesi dahil olmak üzere üretilecek maksimum token sayısı. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur; bu nedenle daha yüksek bir üst sınır, kısa yanıtlar için ek maliyet çıkarmaz. | INT | Evet | 16-65536 (varsayılan: 32768) |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |

### Gemini 3.7 Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin (en az bir boşluk olmayan karakter içermelidir) |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokenı maliyeti çıkarır ve daha yavaştır. | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (varsayılan: `"MEDIUM"`) |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/deterministik, yüksek değer daha yaratıcıdır. | FLOAT | Evet | 0.0-2.0 (varsayılan: 1.0) |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapar. | FLOAT | Evet | 0.0-1.0 (varsayılan: 0.95) |
| `max_output_tokens` | Modelin dahili düşünmesi dahil olmak üzere üretilecek maksimum token sayısı. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur; bu nedenle daha yüksek bir üst sınır, kısa yanıtlar için ek maliyet çıkarmaz. | INT | Evet | 16-65536 (varsayılan: 32768) |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |

### Gemini 3.5 Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin (en az bir boşluk olmayan karakter içermelidir) |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokenı maliyeti çıkarır ve daha yavaştır. | COMBO | Evet | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (varsayılan: `"MEDIUM"`) |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/deterministik, yüksek değer daha yaratıcıdır. | FLOAT | Evet | 0.0-2.0 (varsayılan: 1.0) |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapar. | FLOAT | Evet | 0.0-1.0 (varsayılan: 0.95) |
| `max_output_tokens` | Modelin dahili düşünmesi dahil olmak üzere üretilecek maksimum token sayısı. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur; bu nedenle daha yüksek bir üst sınır, kısa yanıtlar için ek maliyet çıkarmaz. | INT | Evet | 16-65536 (varsayılan: 32768) |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |

### Gemini 3.1 Pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin (en az bir boşluk olmayan karakter içermelidir) |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokenı maliyeti çıkarır ve daha yavaştır. | COMBO | Evet | `"LOW"`<br>`"HIGH"` (varsayılan: `"HIGH"`) |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/deterministik, yüksek değer daha yaratıcıdır. | FLOAT | Evet | 0.0-2.0 (varsayılan: 1.0) |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapar. | FLOAT | Evet | 0.0-1.0 (varsayılan: 0.95) |
| `max_output_tokens` | Modelin dahili düşünmesi dahil olmak üzere üretilecek maksimum token sayısı. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur; bu nedenle daha yüksek bir üst sınır, kısa yanıtlar için ek maliyet çıkarmaz. | INT | Evet | 16-65536 (varsayılan: 32768) |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |

### Gemini 3.1 Flash-Lite Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin (en az bir boşluk olmayan karakter içermelidir) |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokenı maliyeti çıkarır ve daha yavaştır. | COMBO | Evet | `"LOW"`<br>`"HIGH"` (varsayılan: `"LOW"`) |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/deterministik, yüksek değer daha yaratıcıdır. | FLOAT | Evet | 0.0-2.0 (varsayılan: 1.0) |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapar. | FLOAT | Evet | 0.0-1.0 (varsayılan: 0.95) |
| `max_output_tokens` | Modelin dahili düşünmesi dahil olmak üzere üretilecek maksimum token sayısı. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur; bu nedenle daha yüksek bir üst sınır, kısa yanıtlar için ek maliyet çıkarmaz. | INT | Evet | 16-65536 (varsayılan: 32768) |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |

Not: Gemini 3.8 Flash için `temperature` ve `top_p` kullanılamaz ve `video_processing` yalnızca bu model seçeneği için kullanılabilir. `thinking_level` seçenekleri ve varsayılanı, yukarıda listelendiği gibi modele göre farklılık gösterir.

Not: `prompt` girdisi boş olmamalıdır. Düğüm, en az bir boşluk olmayan karakter içerdiğini doğrular.

Not: Düğüm, ilk 10 medya öğesine kadarını URL olarak yükler; öncelik sırası videolar, ardından sesler, sonra görsellerdir. Kalan medyalar base64 olarak satır içi gönderilir. Toplam satır içi medya 18 MB ile sınırlıdır; bu aşılırsa düğüm, eklenen medya sayısını veya boyutunu azaltmanızı isteyen bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Seçilen Gemini modeli tarafından üretilen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/tr.md)

---
**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`
