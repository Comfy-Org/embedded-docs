# StabilKaskad_AşamaB_Koşullandırma

StableCascade_StageB_Conditioning düğümü, mevcut conditioning bilgilerini Stage C'den gelen önceki latent temsillerle birleştirerek Stable Cascade Stage B üretimi için conditioning verisi hazırlar. Her conditioning girdisini kopyalar ve Stage C latent örneklerini içine ekleyerek üretim sürecinin daha tutarlı çıktılar için önceki bilgilerden yararlanmasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Stage C önceki bilgileriyle değiştirilecek conditioning verisi | CONDITIONING | Evet | - |
| `aşama_c` | Conditioning için önceki örnekleri içeren Stage C latent temsili | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Stage C önceki bilgileri entegre edilmiş, değiştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
