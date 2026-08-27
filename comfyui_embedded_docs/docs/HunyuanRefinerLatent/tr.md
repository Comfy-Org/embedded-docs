# HunyuanRefinerLatent

HunyuanRefinerLatent düğümü, Hunyuan video iyileştirme süreci için conditioning ve latent verilerini hazırlar. Girdi latent görüntü verilerini hem pozitif hem de negatif conditioning'e ekler, bunlara bir gürültü artırma değeri uygular ve daha sonraki işlemler için 32 kanallı, sıfırlarla doldurulmuş yeni bir latent oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İşlenecek pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negative` | İşlenecek negatif conditioning girdisi | CONDITIONING | Evet | - |
| `latent` | Latent temsil girdisi; conditioning için latent görüntü verisi olarak kullanılır ve çıktı latentinin boyutlarını tanımlar | LATENT | Evet | - |
| `noise_augmentation` | Uygulanacak gürültü artırma miktarı (varsayılan: 0.10). Bu parametre düğümün gelişmiş bölümünde gösterilir. | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Latent görüntü verisi eklenmiş ve gürültü artırma uygulanmış işlenmiş pozitif conditioning | CONDITIONING |
| `negative` | Latent görüntü verisi eklenmiş ve gürültü artırma uygulanmış işlenmiş negatif conditioning | CONDITIONING |
| `latent` | Girdi latent ile aynı batch boyutuna ve aynı son üç boyuta sahip, 32 kanallı, sıfırlarla doldurulmuş yeni bir latent | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/tr.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
