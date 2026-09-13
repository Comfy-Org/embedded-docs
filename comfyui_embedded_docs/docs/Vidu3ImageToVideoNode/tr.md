# Vidu Q3 Görüntüden Videoya Üretim

Vidu Q3 Görüntüden Videoya Oluşturma düğümü, bir giriş görselinden başlayarak bir video dizisi oluşturur. Görseli canlandırmak için bir Vidu Q3 modeli kullanır, isteğe bağlı olarak bir metin istemiyle yönlendirilebilir ve bir video dosyası çıkarır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. | DYNAMIC_COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image` | Oluşturulan videonun başlangıç karesi olarak kullanılacak bir görsel. | IMAGE | Evet | - |
| `prompt` | Video oluşturma için isteğe bağlı bir metin istemi (en fazla 2000 karakter) (varsayılan: boş). | STRING | Evet | - |
| `seed` | Oluşturmanın rastgeleliğini kontrol etmek için kullanılan seed değeri (varsayılan: 1). | INT | Evet | 0 ile 2147483647 |

### viduq3-pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ile 16 |
| `audio` | Etkinleştirildiğinde, sesli video çıkarır (diyalog ve ses efektleri dahil) (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

### viduq3-turbo Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ile 16 |
| `audio` | Etkinleştirildiğinde, sesli video çıkarır (diyalog ve ses efektleri dahil) (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

**Not:** `image`, 1:4 ile 4:1 arasında bir en-boy oranına sahip olmalıdır (dikeyden yataya). `prompt` isteğe bağlıdır ancak 2000 karakteri aşamaz. Kullanılabilir `resolution` seçenekleri seçilen modele bağlıdır: `"viduq3-pro"` `"720p"`, `"1080p"` ve `"2K"` destekler; `"viduq3-turbo"` `"720p"` ve `"1080p"` destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
