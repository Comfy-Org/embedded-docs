# Google Gemini

Google'ın Gemini modelleriyle metin yanıtları oluşturun. Çok modlu bağlam olarak bir metin istemi ve isteğe bağlı olarak bir veya daha fazla görsel, ses klibi, video veya dosya sağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Gemini modeli. | DYNAMIC_COMBO | Evet | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Model için metin girdisi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. En az bir boşluk olmayan karakter içermelidir. (varsayılan: "") | STRING | Evet |  |
| `seed` | Örnekleme için tohum. Rastgele tohum için 0 olarak ayarlayın. Belirleyici çıktı garanti edilmez. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır |  |

### Gemini 3.8 Flash Girdileri

Bu girdiler `model` parametresi `"Gemini 3.8 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token gerektirir ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

**Not:** Bu model `temperature` veya `top_p` örnekleme kontrollerini sunmaz.

### Gemini 3.7 Flash Girdileri

Bu girdiler `model` parametresi `"Gemini 3.7 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token gerektirir ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirleyici, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.5 Flash Girdileri

Bu girdiler `model` parametresi `"Gemini 3.5 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token gerektirir ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirleyici, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.1 Pro Girdileri

Bu girdiler `model` parametresi `"Gemini 3.1 Pro"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token gerektirir ve daha yavaştır. (varsayılan: "HIGH") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirleyici, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.1 Flash-Lite Girdileri

Bu girdiler `model` parametresi `"Gemini 3.1 Flash-Lite"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token gerektirir ve daha yavaştır. (varsayılan: "LOW") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirleyici, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Medya ve Dosya Girdileri

Aşağıdaki girdiler tüm modeller tarafından paylaşılır ve modele özgü girdilerin yanında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1 ila 16 görsel bağlayın (`image_1` ... `image_16`). Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 16 görsel. | IMAGE | Hayır | 0 - 16 görsel |
| `audio` | Genişletilebilir yuva: bir ses klibi bağlayın (`audio_1`). Model için bağlam olarak kullanılacak isteğe bağlı ses klibi. | AUDIO | Hayır | 0 - 1 klip |
| `video` | Genişletilebilir yuva: bir video klibi bağlayın (`video_1`). Model için bağlam olarak kullanılacak isteğe bağlı video klibi. | VIDEO | Hayır | 0 - 1 klip |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdileri kabul eder. | GEMINI_INPUT_FILES | Hayır |  |

**Not:** Medya (görseller, ses veya video) eklendiğinde, düğüm ilk 10 medya öğesini ComfyAPI depolamasına yükler ve bunları URL olarak iletir; bu URL bütçesi tüm medya türleri arasında paylaşılır ve sırayla tüketilir (önce video, sonra ses, sonra görseller). Kalan medya, toplam satır içi yükü en fazla 18 MB olacak şekilde base64 verisi olarak satır içi kodlanır. Satır içi yük 18 MB'ı aşarsa düğüm bir hata verir. `prompt` parametresi en az bir boşluk olmayan karakter içermelidir. `seed` değerini 0 olarak ayarlamak rastgele bir tohum ister.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Gemini modelinden oluşturulan metin yanıtı. Model hiç metin üretmezse, "Empty response from Gemini model..." dizesi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `98a19d1b29e80907477d24d813593950a028021ee8bcf634f505e11a15daa383`
