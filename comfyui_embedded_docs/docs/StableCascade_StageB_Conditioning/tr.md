> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/tr.md)

StableCascade_StageB_Conditioning düğümü, mevcut koşullandırma bilgilerini Stage C'den gelen önsel gizil temsillerle birleştirerek Stable Cascade Stage B üretimi için koşullandırma verilerini hazırlar. Stage C'den gelen gizil örnekleri koşullandırma verilerine dahil ederek, üretim sürecinin daha tutarlı çıktılar için önsel bilgilerden yararlanmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `koşullandırma` | CONDITIONING | Evet | - | Stage C önsel bilgisiyle değiştirilecek koşullandırma verileri |
| `aşama_c` | LATENT | Evet | - | Koşullandırma için önsel örnekler içeren Stage C'den gelen gizil temsil |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Stage C önsel bilgisi entegre edilmiş değiştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
