# Grok Video Uzatma

Grok Video Extend düğümü, mevcut bir videoyu metin istemine dayalı kesintisiz bir devamla uzatır. Kısa bir kaynak video sağlayın ve ardından ne olması gerektiğini açıklayın; düğüm, orijinalden devam eden yeni bir video klibi döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video uzatma için kullanılacak model. `"grok-imagine-video"` seçeneğini seçmek, modele özgü ayarlarını gösterir. | DYNAMIC_COMBO | Evet | `"grok-imagine-video"` |
| `prompt` | Videoda bundan sonra ne olması gerektiğinin metin açıklaması. | STRING | Evet | N/A |
| `video` | Uzatılacak kaynak video. MP4 formatı, 2-15 saniye. | VIDEO | Evet | MP4, 2-15 saniye, maksimum 50MB |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için seed; gerçek sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 - 2147483647 |

### grok-imagine-video Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `duration` | Uzatmanın saniye cinsinden uzunluğu (varsayılan: 8). | INT | Evet | 2 - 10 |

**Parametre Kısıtlamaları:**
*   `video` girdisi, uzunluğu 2 ile 15 saniye arasında olan bir MP4 dosyası olmalıdır ve dosya boyutu 50MB'ı aşamaz.
*   `prompt`, boşluklar kırpıldıktan sonra en az bir karakter içermelidir.
*   `model` parametresi dinamik bir birleşik kutudur. `"grok-imagine-video"` seçeneğinin seçilmesi, iç içe `duration` parametresini ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Yeni oluşturulan video uzatması. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/tr.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
