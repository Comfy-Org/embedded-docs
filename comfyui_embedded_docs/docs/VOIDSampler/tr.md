# VOIDSampler

VOIDSampler, VOID inpainting modelleri için tasarlanmış özel bir DDIM örnekleyicisidir. VOID'in eğitildiği tam gürültü giderme sürecini yeniden üretir ve standart KSampler'ların uyguladığı gürültü ölçeklemeyi atlar. Bu düğümü, RandomNoise veya VOIDWarpedNoiseSource ile eşleştirilmiş SamplerCustom ya da SamplerCustomAdvanced ile birlikte kullanın.

## Girdiler

Bu düğümün yapılandırılabilir girdi parametresi yoktur. Sabit bir DDIM örnekleme algoritması uygulayan, kendi kendine yeten bir örnekleyicidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm herhangi bir girdi parametresi kabul etmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | SamplerCustom veya SamplerCustomAdvanced düğümlerine bağlanmaya hazır, VOID DDIM algoritmasını uygulayan bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/tr.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
