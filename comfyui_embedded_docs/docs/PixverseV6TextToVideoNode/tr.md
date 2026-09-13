# PixVerse V6 Metinden Videoya

PixVerse V6 Metinden Videoya, PixVerse'in V6 modelini kullanarak bir metin isteminden video oluşturur. Düğüm, istemi seçtiğiniz en boy oranı, çözünürlük, süre ve diğer ayarlarla birlikte PixVerse'e gönderir, oluşturmanın tamamlanmasını bekler ve ardından ortaya çıkan videoyu döndürür — ses oluşturma etkinleştirildiğinde yerleşik bir ses parçası dahil.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model ve oluşturma ayarları. Modeli seçin ve oluşturma seçeneklerini yapılandırın. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için istem. (varsayılan: "") | STRING | Evet | 1–5000 karakter |
| `aspect_ratio` | Çıktı en boy oranı. PixVerse V6 tarafından desteklenen en boy oranlarından birini seçin. | COMBO | Evet | Birden çok seçenek mevcut |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu. (varsayılan: 5) | INT | Evet | 1–15 |
| `generate_audio` | Video ile birlikte yerleşik bir ses parçası oluştur. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `multi_clip` | Modelin videoyu tek bir sürekli çekim yerine birkaç çekime bölmesine izin ver. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `seed` | Video oluşturma için tohum. PixVerse bunu kaydeder ancak bundan bir çalıştırmayı yeniden üretmez. Oluşturma sonrasında rastgeleleştirmeyi destekler. (varsayılan: 42) | INT | Evet | 0–2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") | STRING | Hayır | 0–2048 karakter |
| `style` | Tüm videoya uygulanan isteğe bağlı görsel stil. (varsayılan: "none") | COMBO | Hayır | Birden çok seçenek mevcut |

**Not:** `prompt` gereklidir ve boşluklar kırpıldıktan sonra boş olmamalıdır; maksimum uzunluğu 5000 karakterdir. `negative_prompt` 2048 karakter ile sınırlıdır. `style` değerini "none" (varsayılan) olarak ayarlamak, hiçbir görsel stil uygulanmadığı anlamına gelir. `seed` PixVerse tarafından kaydedilir ancak aynı çalıştırmayı yeniden üretmek için kullanılamaz. Düğüm, PixVerse'in videoyu oluşturmayı bitirmesini bekler ve ardından videoyu indirir; istek başarısız olursa — örneğin PixVerse zaten maksimum eşzamanlı oluşturma sayısına ulaşmışsa, sağlayıcı hesabında kredi kalmamışsa veya içerik moderasyonu istemi reddederse — düğüm bir hata döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan video. `generate_audio` etkinse, video yerleşik ses parçasını içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
