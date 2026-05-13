> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

EmptyChromaRadianceLatentImage düğümü, kroma parlaklık iş akışlarında kullanılmak üzere belirtilen boyutlarda boş bir gizli görüntü oluşturur. Gizli alan işlemleri için başlangıç noktası görevi gören sıfırlarla dolu bir tensör üretir. Düğüm, boş gizli görüntünün genişliğini, yüksekliğini ve toplu iş boyutunu tanımlamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16 ile MAX_RESOLUTION arası | Gizli görüntünün piksel cinsinden genişliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) |
| `height` | INT | Evet | 16 ile MAX_RESOLUTION arası | Gizli görüntünün piksel cinsinden yüksekliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) |
| `batch_size` | INT | Hayır | 1 ile 4096 arası | Bir toplu işte oluşturulacak gizli görüntü sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Belirtilen boyutlarda oluşturulan boş gizli görüntü tensörü |

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
