# PixVerse V6 Görüntüden Videoya

Bu düğüm, bir girdi görüntüsünü PixVerse V6 modeliyle canlandırır ve isteğe bağlı olarak yerel bir ses parçası içeren bir video döndürür. Çıktı videosu, girdi görüntüsünün en-boy oranını korur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model ve üretim ayarları. | DYNAMIC_COMBO | Evet | "PixVerse V6" |
| `görüntü` | Canlandırılacak girdi görüntüsü. | IMAGE | Evet | Tek görüntü |

### PixVerse V6 Girdileri

Bu ayarlar, "PixVerse V6" modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için istem (varsayılan: boş). | STRING | Evet | 1 ile 5000 karakter arası |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px (varsayılan: "720p"). | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Üretilen videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 1 ile 15 arası |
| `generate_audio` | Video ile birlikte yerel bir ses parçası oluştur (varsayılan: true). | BOOLEAN | Evet | true or false |
| `multi_clip` | Modelin videoyu tek bir kesintisiz çekim yerine birden fazla çekime bölmesine izin ver (varsayılan: false). | BOOLEAN | Evet | true or false |
| `seed` | Video üretimi için tohum (seed). PixVerse bunu kaydeder ancak ondan bir çalışmayı yeniden üretmez (varsayılan: 42, üretim sonrası kontrol etkinleştirilmiştir). | INT | Evet | 0 ile 2147483647 arası |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş). | STRING | Hayır | En fazla 2048 karakter |
| `style` | Videonun tamamına uygulanan isteğe bağlı görsel stil (varsayılan: yok). | COMBO | Hayır | Birden fazla seçenek mevcut (PixVerse V6 stil ön ayarları) |

Not: İstem, en az bir boşluk olmayan karakter içermeli ve en fazla 5000 karakter olmalıdır; negatif istem, sağlanmışsa, en fazla 2048 karakter olmalıdır. Çıktı videosu her zaman girdi görüntüsünün en-boy oranıyla eşleşir, bu nedenle en-boy oranı ayarı gerekmez. Yalnızca tek bir girdi görüntüsü kabul edilir. PixVerse; içerik denetimi başarısız olursa, sağlayıcı hesabının kredisi biterse veya aynı anda çalışan maksimum üretim sayısına ulaşılmışsa isteği reddedebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video; `generate_audio` etkinleştirildiğinde yerel ses parçası dahildir. En-boy oranı girdi görüntüsüyle eşleşir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`
