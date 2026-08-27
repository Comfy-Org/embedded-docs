# BoşKromaIşımaGizliGörsel

The EmptyChromaRadianceLatentImage düğümü, kroma radiance iş akışlarında kullanılmak üzere belirtilen boyutlarda boş bir latent görüntü oluşturur. Sıfırlarla doldurulmuş bir tensör üretir; bu tensör, latent uzay işlemleri için bir başlangıç noktası görevi görür. Düğüm, boş latent görüntünün genişliğini, yüksekliğini ve batch boyutunu tanımlamanızı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent görüntünün piksel cinsinden genişliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `toplu_iş_boyutu` | Bir batch içinde oluşturulacak latent görüntü sayısı (varsayılan: 1) | INT | Hayır | 1 ila 4096 |

Not: `width` ve `height` parametreleri 16 adım aralığıyla tanımlanır, bu yüzden 16'nın katları olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş, batch_size x 3 x height x width şeklindeki oluşturulan boş latent görüntü tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
