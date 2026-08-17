# BoşSD3GizliGörüntü

EmptySD3LatentImage düğümü, Stable Diffusion 3 modelleri için özel olarak biçimlendirilmiş boş bir latent görüntü tensörü oluşturur. SD3 işlem hatlarının beklediği doğru boyut ve yapıya sahip, sıfırlarla doldurulmuş bir tensör üretir. Bu düğüm, görüntü oluşturma iş akışları için genellikle bir başlangıç noktası olarak kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Çıktı latent görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) |
| `height` | Çıktı latent görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 16) |
| `batch_size` | Bir batch içinde oluşturulacak latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | SD3 uyumlu boyutlarda boş örnekler içeren bir latent tensör. Tensör 16 kanala sahiptir ve girdi genişlik ve yüksekliğine kıyasla uzamsal olarak 8 kat küçültülmüştür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
