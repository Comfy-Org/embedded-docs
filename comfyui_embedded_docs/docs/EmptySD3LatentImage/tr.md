# BoşSD3GizliGörüntü

EmptySD3LatentImage, Stable Diffusion 3 modellerinin beklediği düzende boş (tamamen sıfır) bir latent görüntü oluşturur. Latent boş olduğundan, normalde bir üretim iş akışının bir görüntüyle dolduracağı başlangıç noktası olarak kullanılır. Seçtiğiniz genişlik ve yükseklik, nihai görüntünün boyutunu belirler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent görüntünün piksel cinsinden genişliği (varsayılan: 1024). Değerler 16'lık artışlarla adımlanır. | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) |
| `yükseklik` | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 1024). Değerler 16'lık artışlarla adımlanır. | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) |
| `toplu_boyut` | Toplu işlemde oluşturulacak latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | SD3 uyumlu biçimde boş (tamamen sıfır) örnekler içeren bir latent tensörü. Tensör 16 kanallıdır, `width` ve `height` değerlerine göre 8 kat küçültülmüştür ve 8'lik bir uzamsal küçültme oranı taşır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
