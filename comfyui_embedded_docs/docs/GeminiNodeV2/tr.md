# Google Gemini

Google'ın Gemini modelleriyle metin yanıtları oluşturun. Bir metin istemi ve isteğe bağlı olarak bir veya daha fazla görsel, ses klibi, video veya dosyayı çok modlu bağlam olarak sağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Gemini modeli. | COMBO | Evet | `"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Modele metin girişi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. En az bir boşluk olmayan karakter içermelidir. (varsayılan: "") | STRING | Evet |  |
| `seed` | Örnekleme için tohum değeri. Rastgele tohum için 0 olarak ayarlayın. Belirleyici çıktı garanti edilmez. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır |  |

### Gemini 3.5 Flash Girdileri

Bu girdiler, `model` parametresi `"Gemini 3.5 Flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar derin düşündüğünü belirler. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokeni harcar ve daha yavaştır. (varsayılan: "MEDIUM") | COMBO | Evet | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Daha düşük değer daha odaklı/belirleyici, daha yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2.0 arası |
| `top_p` | Nükleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `max_output_tokens` | Üretilecek azami token sayısı; modelin dahili düşünmesi dahil. thinking_level HIGH iken düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesik geliyorsa bu değeri artırın. Model işi bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 ile 65536 arası |

### Gemini 3.1 Pro Girdileri

Bu girdiler, `model` parametresi `"Gemini 3.1 Pro"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar derin düşündüğünü belirler. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokeni harcar ve daha yavaştır. (varsayılan: "HIGH") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Daha düşük değer daha odaklı/belirleyici, daha yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2.0 arası |
| `top_p` | Nükleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `max_output_tokens` | Üretilecek azami token sayısı; modelin dahili düşünmesi dahil. thinking_level HIGH iken düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesik geliyorsa bu değeri artırın. Model işi bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 ile 65536 arası |

### Gemini 3.1 Flash-Lite Girdileri

Bu girdiler, `model` parametresi `"Gemini 3.1 Flash-Lite"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Modelin yanıtlamadan önce dahili olarak ne kadar derin düşündüğünü belirler. HIGH, zor görevlerde kaliteyi artırır ancak daha fazla (düşünme) tokeni harcar ve daha yavaştır. (varsayılan: "LOW") | COMBO | Evet | `"LOW"`<br>`"HIGH"` |
| `temperature` | Rastgeleliği kontrol eder. Daha düşük değer daha odaklı/belirleyici, daha yüksek değer daha yaratıcıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2.0 arası |
| `top_p` | Nükleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `max_output_tokens` | Üretilecek azami token sayısı; modelin dahili düşünmesi dahil. thinking_level HIGH iken düşük bir değer yanıt için yer bırakmayabilir; yanıtlar boş veya kesik geliyorsa bu değeri artırın. Model işi bittiğinde erken durur, bu nedenle daha yüksek bir üst sınır kısa yanıtlar için ek maliyet getirmez. (varsayılan: 32768) | INT | Evet | 16 ile 65536 arası |

### Medya ve Dosya Girdileri

Aşağıdaki girdiler üç model için de ortaktır ve modele özel girdilerin yanında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: 1 ila 16 görseli bağlayın (`image_1` ... `image_16`). Modele bağlam olarak kullanılacak isteğe bağlı görsel(ler). | IMAGE | Hayır | 0 ile 16 görsel arası |
| `audio` | Genişletilebilir yuva: bir ses klibi bağlayın (`audio_1`). Modele bağlam olarak kullanılacak isteğe bağlı ses klibi. | AUDIO | Hayır | 0 ile 1 klip arası |
| `video` | Genişletilebilir yuva: bir video klibi bağlayın (`video_1`). Modele bağlam olarak kullanılacak isteğe bağlı video klibi. | VIDEO | Hayır | 0 ile 1 klip arası |
| `files` | Modele bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır |  |

**Not:** Medya (görsel, ses veya video) eklendiğinde, düğüm ilk 10 medya öğesini ComfyAPI depolama alanına yükler ve bunları URL olarak iletir; bu URL bütçesi tüm medya türleri arasında paylaşılır ve sırayla tüketilir (önce video, sonra ses, ardından görseller). Geri kalan medya, toplam satır içi yükü en fazla 18 MB olacak şekilde base64 verisi olarak satır içi kodlanır. Satır içi yük 18 MB'ı aşarsa düğüm bir hata verir. `prompt` parametresi en az bir boşluk olmayan karakter içermelidir. `seed` değerini 0 olarak ayarlamak rastgele tohum talep eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Gemini modelinden üretilen metin yanıtı. Model hiçbir metin üretmezse, "Empty response from Gemini model..." dizesi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `e88c253d9ae987ab91b0fb6b0b55cfd9cd3671438770afcedd844f236b30dc36`
