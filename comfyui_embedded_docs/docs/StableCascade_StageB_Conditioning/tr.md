# StabilKaskad_AşamaB_Koşullandırma

StableCascade_StageB_Conditioning düğümü, mevcut koşullandırma bilgisini Stage C tarafından üretilen önceki latent temsiliyle birleştirerek Stable Cascade Stage B üretimi için koşullandırma verisini hazırlar. Her koşullandırma girişini kopyalar ve Stage C latent örneklerini içine kaydeder; böylece sonraki üretim adımları daha tutarlı sonuçlar için bu önceki bilgiyi kullanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Stage C önceki bilgisiyle değiştirilecek koşullandırma verisi. Listedeki her giriş kopyalanır ve ona Stage C örnekleri atanır. | CONDITIONING | Evet | - |
| `stage_c` | Stage C'den gelen latent temsili. `samples` değeri, koşullandırmaya eklenen önceki bilgi olarak kullanılır. | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Stage C önceki bilgisi entegre edilmiş değiştirilmiş koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
