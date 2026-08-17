# Grok Video Uzatma

Grok Video Extend düğümü, mevcut bir videonun kesintisiz devamını oluşturmak için bir yapay zeka modeli kullanır. Kısa bir video ve ardından ne olması gerektiğini açıklayan bir metin istemi sağlarsınız; düğüm, orijinalin devamı niteliğinde yeni bir video klibi üretir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|---------|--------|
| `model` | Video uzatma için kullanılacak model. | DYNAMIC_COMBO | Evet | `"grok-imagine-video"` |
| `istem` | Videoda bundan sonra ne olması gerektiğine dair metin açıklaması. | STRING | Evet | N/A |
| `video` | Uzatılacak kaynak video. MP4 formatında, 2-15 saniye. | VIDEO | Evet | N/A |
| `tohum` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını belirler; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

### grok-imagine-video Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|---------|--------|
| `duration` | Uzatmanın saniye cinsinden uzunluğu (varsayılan: 8). | INT | Evet | 2 ile 10 arası |

**Parametre Kısıtlamaları:**

*   `video` girdisi, 2 ila 15 saniye arasında uzunluğa sahip bir MP4 dosyası olmalı ve dosya boyutu 50MB'ı aşmamalıdır.
*   `prompt` en az bir karakter içermelidir (boşluk karakterleri silinir).
*   `model` parametresi dinamik bir kombinasyondur. "grok-imagine-video" seçeneğinin seçilmesi, iç içe geçmiş `duration` parametresini ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-----------|-----------|
| `output` | Yeni oluşturulan devam videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfaf56dd12afab13c820345587db9ee871db87d60b8dc003f00f035513dbdf61`
