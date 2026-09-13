# PixVerse V6 Görüntüden Videoya

Bu düğüm, bir giriş görüntüsünü PixVerse V6 modeliyle canlandırır ve isteğe bağlı olarak yerel bir ses parçası içeren bir video döndürür. Çıktı videosu, giriş görüntüsünün en-boy oranını korur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Canlandırılacak giriş görüntüsü. | IMAGE | Evet | Tek görüntü |
| `model` | Model ve oluşturma ayarları. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

Bu ayarlar "PixVerse V6" modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için istem (varsayılan: boş). | STRING | Evet | 1 ila 5000 karakter |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px'tir (varsayılan: "720p"). | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 1 ila 15 |
| `generate_audio` | Video ile birlikte yerel bir ses parçası oluşturur (varsayılan: true). | BOOLEAN | Evet | true veya false |
| `multi_clip` | Modelin videoyu tek bir sürekli çekim yerine birkaç plana bölmesini sağlar (varsayılan: false). | BOOLEAN | Evet | true veya false |
| `seed` | Video oluşturma için tohum. PixVerse bunu kaydeder ancak bundan bir çalıştırmayı yeniden üretmez (varsayılan: 42, oluşturma sonrası kontrol etkindir). | INT | Evet | 0 ila 2147483647 |
| `negative_prompt` | Videodaki istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş). | STRING | Hayır | En fazla 2048 karakter |
| `style` | Tüm videoya uygulanan isteğe bağlı görsel stil (varsayılan: yok). | COMBO | Hayır | Birden çok seçenek mevcut (PixVerse V6 stil ön ayarları) |

Not: İstem en az bir boşluk olmayan karakter içermeli ve en fazla 5000 karakter olmalıdır; negatif istem sağlanırsa en fazla 2048 karakter olmalıdır. Çıktı videosu her zaman giriş görüntüsünün en-boy oranıyla eşleşir, bu nedenle en-boy oranı ayarı gerekmez. Yalnızca tek bir giriş görüntüsü kabul edilir. PixVerse, içerik denetimi başarısız olduğunda, sağlayıcı hesabının kredisi tükendiğinde veya eşzamanlı oluşturma üst sınırına zaten ulaşıldığında bir isteği reddedebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video; `generate_audio` etkinleştirildiğinde yerel ses parçasını içerir. En-boy oranı giriş görüntüsüyle eşleşir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`
