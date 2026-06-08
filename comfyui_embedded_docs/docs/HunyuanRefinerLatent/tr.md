HunyuanRefinerLatent düğümü, iyileştirme işlemleri için conditioning ve latent girdilerini işler. Pozitif ve negatif conditioning'e gürültü artırımı uygularken latent görüntü verilerini de dahil eder ve daha ileri işlemler için belirli boyutlara sahip yeni bir latent çıktısı oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İşlenecek pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negative` | İşlenecek negatif conditioning girdisi | CONDITIONING | Evet | - |
| `latent` | Latent temsil girdisi | LATENT | Evet | - |
| `noise_augmentation` | Uygulanacak gürültü artırımı miktarı (varsayılan: 0.10) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negative` | Uygulanan gürültü artırımı ve latent görüntü birleştirmesi ile işlenmiş pozitif conditioning | CONDITIONING |
| `latent` | Uygulanan gürültü artırımı ve latent görüntü birleştirmesi ile işlenmiş negatif conditioning | CONDITIONING |
| `latent` | [batch_size, 32, height, width, channels] boyutlarında yeni bir latent çıktısı | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/tr.md)

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
