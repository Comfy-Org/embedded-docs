# Google Gemini

Google'ın Gemini modelleriyle metin yanıtları oluşturun. Çok modlu bağlam olarak bir metin istemi ve isteğe bağlı olarak bir veya daha fazla görüntü, ses klibi, video veya dosya sağlayın. Düğüm, istemi ve eklenen tüm medyayı seçilen modele gönderir ve modelin metin yanıtını döndürür.

**Not:** Bu düğüm kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Gemini modeli. Bir model seçildiğinde, aşağıda o modele ait girdi kümesi görünür. | DYNAMIC_COMBO | Evet | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Modele metin girdisi. Ayrıntılı yönergeler, sorular veya bağlam ekleyin. (varsayılan: "") | STRING | Evet | En az bir boşluk olmayan karakter içermelidir |
| `seed` | Örnekleme için tohum. Rastgele bir tohum için 0 olarak ayarlayın. Belirlenimci çıktı garanti edilmez. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel yönergeler. (varsayılan: "") | STRING | Hayır |  |

### Gemini 3.8 Flash Girdileri

Bu girdiler, `model` `"Gemini 3.8 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token harcar ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ekstra maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

**Not:** Bu model `temperature` veya `top_p` örnekleme kontrollerini sunmaz.

### Gemini 3.7 Flash Girdileri

Bu girdiler, `model` `"Gemini 3.7 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token harcar ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirlenimci, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Nucleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ekstra maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.5 Flash Girdileri

Bu girdiler, `model` `"Gemini 3.5 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token harcar ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirlenimci, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Nucleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ekstra maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.1 Pro Girdileri

Bu girdiler, `model` `"Gemini 3.1 Pro"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token harcar ve daha yavaştır. (varsayılan: "HIGH") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirlenimci, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Nucleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ekstra maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Gemini 3.1 Flash-Lite Girdileri

Bu girdiler, `model` `"Gemini 3.1 Flash-Lite"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar yoğun akıl yürüttüğü. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) token harcar ve daha yavaştır. (varsayılan: "LOW") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/belirlenimci, yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 |
| `top_p` | Nucleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapın. (varsayılan: 0.95) | FLOAT | Evet | 0.0 - 1.0 |
| `max_output_tokens` | Üretilecek maksimum token sayısı, modelin dahili düşünmesi dahil. thinking_level HIGH ile düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesilmiş gelirse bunu artırın. Model bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ekstra maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 - 65536 |

### Medya ve Dosya Girdileri

Aşağıdaki girdiler tüm modeller tarafından paylaşılır ve modele özgü girdilerin yanında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1 ila 16 görüntü bağlayın (`image_1` ... `image_16`). Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). En fazla 16 görüntü. | IMAGE | Hayır | 0 - 16 görüntü |
| `audio` | Genişletilebilir yuva: bir ses klibi bağlayın (`audio_1`). Model için bağlam olarak kullanılacak isteğe bağlı ses klibi. | AUDIO | Hayır | 0 - 1 klip |
| `video` | Genişletilebilir yuva: bir video klibi bağlayın (`video_1`). Model için bağlam olarak kullanılacak isteğe bağlı video klibi. | VIDEO | Hayır | 0 - 1 klip |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır |  |

**Not:** Medya (görüntüler, ses veya video) eklendiğinde, düğüm ilk 10 medya öğesini ComfyAPI depolamasına yükler ve bunları URL olarak iletir; bu URL bütçesi tüm medya türleri arasında paylaşılır ve sırayla tüketilir (önce video, sonra ses, sonra görüntüler). Kalan medya, satır içi base64 verisi olarak kodlanır ve birleşik satır içi yük en fazla 18 MB olabilir. Satır içi yük 18 MB'ı aşacaksa düğüm bir hata oluşturur. `prompt` parametresi en az bir boşluk olmayan karakter içermelidir. `seed` değerinin 0 olarak ayarlanması rastgele bir tohum ister.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Gemini modelinden oluşturulan metin yanıtı. Model metin üretmezse, "Empty response from Gemini model..." dizesi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `8ae14c6465569695e1e99b0040cb2c745e5f3d9ddcd3b03013530dc7e7135b87`
