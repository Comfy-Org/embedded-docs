# PixVerse V6 Metinden Videoya

PixVerse V6 Text to Video, PixVerse'in V6 modelini kullanarak bir metin isteminden video oluşturur. Düğüm, istemi seçtiğiniz çözünürlük, süre, en-boy oranı ve diğer ayarlarla birlikte PixVerse'e gönderir, oluşturmanın bitmesini bekler ve ardından sonuçtaki videoyu döndürür — ses oluşturma etkinleştirildiğinde yerel bir ses parçası dahil.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model ve oluşturma ayarları. Modeli seçin ve oluşturma seçeneklerini yapılandırın. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için istem. (varsayılan: "") | STRING | Evet | 1–5000 karakter |
| `aspect_ratio` | Çıktı en-boy oranı. PixVerse V6 tarafından desteklenen en-boy oranlarından birini seçin. | COMBO | Evet | Birden fazla seçenek mevcut |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı belirler: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px'dir. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu. (varsayılan: 5) | INT | Evet | 1–15 |
| `generate_audio` | Video ile birlikte yerel bir ses parçası oluşturun. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `multi_clip` | Modelin videoyu tek bir sürekli çekim yerine birkaç sahneye bölmesine izin verin. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `seed` | Video oluşturma için tohum değeri. PixVerse bunu kaydeder ancak bir çalıştırmayı bundan yeniden üretmez. Oluşturma sonrası rastgeleleştirmeyi destekler. (varsayılan: 42) | INT | Evet | 0–2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") | STRING | Hayır | 0–2048 karakter |
| `style` | Videonun tamamına uygulanan isteğe bağlı görsel stil. (varsayılan: "none") | COMBO | Hayır | Birden fazla seçenek mevcut |

**Not:** `prompt` zorunludur ve baştaki ve sondaki boşluklar silindikten sonra boş olmamalıdır; maksimum uzunluğu 5000 karakterdir. `negative_prompt` 2048 karakterle sınırlıdır. `style` alanını "none" (varsayılan) olarak ayarlamak hiçbir görsel stilin uygulanmayacağı anlamına gelir. `seed`, PixVerse tarafından kaydedilir ancak aynı çalıştırmayı yeniden üretmek için kullanılamaz. Düğüm, PixVerse'in videoyu oluşturmayı bitirmesini bekler ve ardından videoyu indirir; istek başarısız olursa — örneğin PixVerse aynı anda maksimum sayıda oluşturma işlemini zaten çalıştırıyorsa, sağlayıcı hesabının kredisi yoksa veya içerik denetimi istemi reddederse — düğüm bir hata döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan video. `generate_audio` etkinleştirilirse video, yerel ses parçasını içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
