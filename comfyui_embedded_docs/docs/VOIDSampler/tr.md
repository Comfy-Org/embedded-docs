# VOIDSampler

VOIDSampler, VOID inpainting modelleri için özel olarak tasarlanmış bir DDIM sampler'dır. VOID'in eğitildiği aynı gürültü giderme işlemini, standart KSampler'ların uyguladığı gürültü ölçeklemesi olmadan uygular. Bu düğümü, RandomNoise veya VOIDWarpedNoiseSource ile eşleştirilmiş SamplerCustom veya SamplerCustomAdvanced ile birlikte kullanın.

## Girdiler

Bu düğümün yapılandırılabilir girdi parametresi yoktur. Sabit bir DDIM örnekleme algoritması uygulayan, kendi içinde eksiksiz bir sampler'dır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm hiçbir girdi parametresi kabul etmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | VOID DDIM algoritmasını uygulayan, SamplerCustom veya SamplerCustomAdvanced düğümlerine bağlanmaya hazır bir sampler nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/tr.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
