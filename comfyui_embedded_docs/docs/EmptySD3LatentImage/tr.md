# BoşSD3GizliGörüntü

EmptySD3LatentImage, Stable Diffusion 3 modelleri için özel olarak biçimlendirilmiş boş bir latent görüntü tensörü oluşturur. SD3 işlem hatlarının beklediği doğru boyutlara ve yapıya sahip, sıfırlarla dolu bir tensör üretir. Bu, görüntü oluşturma iş akışları için genellikle başlangıç noktası olarak kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Çıktı latent görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `yükseklik` | Çıktı latent görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `toplu_boyut` | Bir toplu işlemde (batch) oluşturulacak latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | SD3 ile uyumlu boyutlara sahip boş örnekler içeren bir latent tensör. Tensör, 16 kanala sahiptir ve girdi genişlik ve yüksekliğine kıyasla uzamsal olarak 8 kat küçültülmüştür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
