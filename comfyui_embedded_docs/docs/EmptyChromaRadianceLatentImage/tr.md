EmptyChromaRadianceLatentImage düğümü, kroma parlaklık iş akışlarında kullanılmak üzere belirtilen boyutlarda boş bir gizli görüntü oluşturur. Gizli alan işlemleri için başlangıç noktası görevi gören sıfırlarla dolu bir tensör üretir. Düğüm, boş gizli görüntünün genişliğini, yüksekliğini ve toplu iş boyutunu tanımlamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Gizli görüntünün piksel cinsinden genişliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Gizli görüntünün piksel cinsinden yüksekliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `toplu_iş_boyutu` | Bir toplu işte oluşturulacak gizli görüntü sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda oluşturulan boş gizli görüntü tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
