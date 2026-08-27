# Grok Video Uzatma

Grok Video Extend düğümü, mevcut bir videonun kesintisiz devamını oluşturmak için bir AI modeli kullanır. Kısa bir video ve bundan sonra ne olması gerektiğini açıklayan bir metin istemi sağlarsınız; düğüm, orijinalin devamı niteliğinde yeni bir video klibi oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video uzatma için kullanılacak model. | DYNAMIC_COMBO | Evet | `"grok-imagine-video"` |
| `istem` | Videoda bundan sonra ne olması gerektiğine dair metin açıklaması. | STRING | Evet | N/A |
| `video` | Uzatılacak kaynak video. MP4 formatında, 2-15 saniye. | VIDEO | Evet | N/A |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 2147483647 |

### grok-imagine-video Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `duration` | Uzatmanın süresi (saniye cinsinden) (varsayılan: 8). | INT | Evet | 2 ila 10 |

**Parametre Kısıtlamaları:**
*   `video` girdisi 2 ila 15 saniye uzunluğunda bir MP4 dosyası olmalı ve dosya boyutu 50MB'ı aşmamalıdır.
*   `prompt` boşluklar kırpıldıktan sonra en az bir karakter içermelidir.
*   `model` parametresi dinamik bir combo'dur. "grok-imagine-video" seçeneğinin seçilmesi, iç içe geçmiş `duration` parametresini ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Yeni oluşturulan video devamı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/tr.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
