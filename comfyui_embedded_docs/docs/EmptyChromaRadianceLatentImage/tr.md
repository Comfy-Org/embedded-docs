# BoşKromaIşımaGizliGörsel

EmptyChromaRadianceLatentImage düğümü, chroma radiance iş akışlarında kullanılmak üzere belirttiğiniz boyutlarda boş bir latent görüntü oluşturur. Latent uzayı işlemleri için başlangıç noktası işlevi gören sıfırlarla dolu bir tensör üretir; böylece boş latent görüntünün genişliğini, yüksekliğini ve batch boyutunu tanımlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent görüntünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |
| `toplu_iş_boyutu` | Bir batch içinde oluşturulacak latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

Not: `width` ve `height` 16 adım aralığıyla tanımlanır; bu nedenle değerler 16'nın katları olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla dolu, şekli batch_size x 3 x height x width olan oluşturulmuş boş latent görüntü tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
