# Vidu Video Uzatma

Vidu Video Extension düğümü, mevcut bir videonun uzunluğunu uzatmak için ek kareler üretir. Kaynak videoya ve isteğe bağlı bir metin istemine dayalı bir devam oluşturmak için belirtilen bir yapay zekâ modelini kullanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video uzatma için kullanılacak model. Bir model seçildiğinde, o modele özgü süre ve çözünürlük ayarları gösterilir. | DYNAMIC_COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | Uzatılacak kaynak video. | VIDEO | Evet | - |
| `prompt` | Uzatılmış video için isteğe bağlı metin istemi (en fazla 2000 karakter; varsayılan: boş). | STRING | Evet | - |
| `seed` | Üretimin rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). | INT | Evet | 0 - 2147483647 |
| `end_frame` | Uzatma için hedef bitiş karesi olarak kullanılacak isteğe bağlı görüntü. | IMAGE | Hayır | - |

### viduq2-pro ve viduq2-turbo Girdileri

Bu ayarlar her iki modelde de ortaktır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `duration` | Uzatılan videonun saniye cinsinden süresi (varsayılan: 4). Bu ayar, bir model seçildikten sonra görünür. | INT | Evet | 1 - 7 |
| `resolution` | Çıktı videosunun çözünürlüğü. Bu ayar, bir model seçildikten sonra görünür. | COMBO | Evet | `"720p"`<br>`"1080p"` |

**Not:** Kaynak `video`, 4 ile 55 saniye arasında bir süreye sahip olmalıdır. `end_frame` sağlanırsa, en-boy oranı 1:4 ile 4:1 arasında olmalı ve genişliğinin ve yüksekliğinin her biri en az 128 piksel olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Uzatılmış görüntüleri içeren yeni üretilmiş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
