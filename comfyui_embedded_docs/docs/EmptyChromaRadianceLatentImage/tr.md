# BoşKromaIşımaGizliGörsel

EmptyChromaRadianceLatentImage düğümü, chroma radiance iş akışlarında kullanılmak üzere belirtilen boyutlarda boş bir latent görüntü oluşturur. Latent uzay işlemleri için başlangıç noktası görevi gören sıfırlarla dolu (3 renk kanalı içeren) bir tensör üretir. Düğüm, boş latent görüntünün genişliğini, yüksekliğini ve yığın boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Latent görüntünün piksel cinsinden genişliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `batch_size` | Bir yığın içinde oluşturulacak latent görüntü sayısı (varsayılan: 1) | INT | Hayır | 1 to 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda, sıfırlarla dolu olarak oluşturulan boş latent görüntü tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
