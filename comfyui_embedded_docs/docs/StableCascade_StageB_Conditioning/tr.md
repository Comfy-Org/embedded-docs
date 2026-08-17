# StabilKaskad_AşamaB_Koşullandırma

The StableCascade_StageB_Conditioning düğümü, Stable Cascade Stage B üretimi için koşullandırma verilerini, mevcut koşullandırma bilgilerini Stage C'den gelen önceki latent temsillerle birleştirerek hazırlar. Her koşullandırma girdisine Stage C'den gelen latent örneklerini ekler ve böylece üretim sürecinin daha tutarlı çıktılar için önceki bilgilerden yararlanmasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Stage C önceki bilgisiyle değiştirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `stage_c` | Koşullandırma için önceki örnekleri içeren Stage C latent temsili | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Stage C önceki bilgisi entegre edilmiş değiştirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
