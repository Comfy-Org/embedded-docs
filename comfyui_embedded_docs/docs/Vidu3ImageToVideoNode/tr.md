# Vidu Q3 Görüntüden Videoya Üretim

Vidu Q3 Görüntüden Videoya Oluşturma düğümü, girdi görüntüsünden başlayarak bir video dizisi oluşturur. Görüntüyü hareketlendirmek için bir Vidu Q3 modeli kullanır; isteğe bağlı olarak bir metin istemiyle yönlendirilir ve bir video dosyası çıktısı verir.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image` | Oluşturulan videonun başlangıç karesi olarak kullanılacak bir görüntü. | IMAGE | Evet | - |
| `prompt` | Video oluşturma için isteğe bağlı bir metin istemi (en fazla 2000 karakter) (varsayılan: boş). | STRING | Hayır | - |
| `seed` | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). | INT | Hayır | 0 ile 2147483647 |

### viduq3-pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `model.duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ile 16 |
| `model.audio` | Etkinleştirildiğinde, videoyu sesle (diyalog ve ses efektleri dahil) çıkarır (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

### viduq3-turbo Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `model.duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ile 16 |
| `model.audio` | Etkinleştirildiğinde, videoyu sesle (diyalog ve ses efektleri dahil) çıkarır (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

**Not:** `image` görüntüsünün en-boy oranı 1:4 ile 4:1 (dikey ve yatay) arasında olmalıdır. `prompt` isteğe bağlıdır ancak 2000 karakteri aşamaz. Çözünürlük seçenekleri seçilen modele bağlıdır: `"viduq3-pro"` `"720p"`, `"1080p"` ve `"2K"` destekler; `"viduq3-turbo"` `"720p"` ve `"1080p"` destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
