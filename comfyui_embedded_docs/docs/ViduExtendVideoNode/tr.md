# Vidu Video Uzatma

ViduExtendVideoNode, mevcut bir videonun uzunluğunu uzatmak için ek kareler oluşturur. Kaynak videoya ve isteğe bağlı bir metin istemine dayalı olarak kesintisiz bir devam oluşturmak için belirtilen bir yapay zeka modeli kullanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video uzatma için kullanılacak model. Bir model seçmek, modele özgü süre ve çözünürlük ayarlarını ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | Uzatılacak kaynak video. | VIDEO | Evet | - |
| `prompt` | Uzatılmış video için isteğe bağlı metin istemi (en fazla 2000 karakter, varsayılan: boş). | STRING | Hayır | - |
| `seed` | Üretimin rastgeleliğini kontrol etmek için kullanılan tohum değeri (varsayılan: 1). | INT | Hayır | 0 ile 2147483647 arası |
| `bitiş karesi` | Uzatma için hedef bitiş karesi olarak kullanılacak isteğe bağlı bir görsel. | IMAGE | Hayır | - |

### viduq2-pro ve viduq2-turbo Girdileri

Bu ayarlar her iki model tarafından da paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `süre` | Uzatılmış videonun süresi (saniye cinsinden, varsayılan: 4). Bu ayar, bir model seçtikten sonra görünür. | INT | Evet | 1 ile 7 arası |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. Bu ayar, bir model seçtikten sonra görünür. | COMBO | Evet | `"720p"`<br>`"1080p"` |

**Not:** Kaynak `video` 4 ila 55 saniye arasında bir süreye sahip olmalıdır. `end_frame` sağlanmışsa, en-boy oranı 1:4 ile 4:1 arasında olmalı ve genişliği ile yüksekliği en az 128 piksel olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Uzatılmış görüntüyü içeren yeni oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
