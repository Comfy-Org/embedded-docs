# HunyuanRefinerLatent

HunyuanRefinerLatent düğümü, iyileştirme işlemleri için koşullandırma ve latent girdilerini işler. Hem pozitif hem de negatif koşullandırmaya gürültü artırımı uygular, latent görüntü verisini dahil eder ve daha sonraki işlemler için belirli boyutlara sahip yeni bir latent çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İşlenecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | İşlenecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `latent` | Latent temsil girdisi | LATENT | Evet | - |
| `noise_augmentation` | Uygulanacak gürültü artırımı miktarı (varsayılan: 0.10, adım: 0.01, gelişmiş parametre) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Uygulanan gürültü artırımı ve latent görüntü birleştirmesiyle işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Uygulanan gürültü artırımı ve latent görüntü birleştirmesiyle işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Girdi `latent` ile aynı parti boyutuna ve aynı son üç boyut boyutuna sahip, ancak 32 kanallı, sıfırlarla doldurulmuş yeni bir latent | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/tr.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
