# VOIDSampler

## Genel Bakış

VOIDSampler düğümü, VOID inpaint modelleri için özel olarak tasarlanmış bir DDIM örnekleme yöntemi sağlar. Standart KSampler'ların uyguladığı gürültü ölçeklemesi olmadan, VOID model eğitimi sırasında kullanılan aynı gürültü giderme sürecini uygular. Bu düğüm, SamplerCustom veya SamplerCustomAdvanced düğümleriyle kullanılmak üzere tasarlanmıştır ve RandomNoise veya VOIDWarpedNoiseSource ile eşleştirilmelidir.

## Girdiler

Bu düğümün yapılandırılabilir girdi parametresi yoktur. Sabit bir DDIM örnekleme algoritması uygulayan bağımsız bir örnekleyicidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm herhangi bir girdi parametresi kabul etmez. | - | - | - |

Not: VOID modelleri, girdi standart sapmasının yaklaşık 1 olduğu alfa uzayında çalışan diffusers CogVideoXDDIMScheduler ile eğitilmiştir. Standart KSampler'ın uyguladığı yaklaşık 4500 katlık gürültü ölçeklemesi bu eğitimle uyumsuzdur. VOIDSampler bu ölçeklemeyi atlar ve DDIM güncelleme kuralını doğrudan sigma-alfa dönüşümü kullanarak uygular.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | VOID DDIM algoritmasını uygulayan, SamplerCustom veya SamplerCustomAdvanced düğümlerine bağlanmaya hazır bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/tr.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
