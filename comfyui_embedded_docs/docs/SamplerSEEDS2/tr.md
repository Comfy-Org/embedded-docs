# SamplerSEEDS2

Bu düğüm, görüntü üretimi için yapılandırılabilir bir örnekleyici sağlar. Stokastik diferansiyel denklem (SDE) çözücüsü olan SEEDS-2 algoritmasını uygular. Parametrelerini ayarlayarak, `seeds_2`, `exp_heun_2_x0` ve `exp_heun_2_x0_sde` dahil olmak üzere birkaç belirli örnekleyici gibi davranacak şekilde yapılandırabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `solver_type` | Örnekleyici için temel çözücü algoritmasını seçer. | COMBO | Evet | `"phi_1"`<br>`"phi_2"` |
| `eta` | Stokastik güç (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 100.0 |
| `s_noise` | SDE gürültü çarpanı (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 100.0 |
| `r` | Ara aşama (c2 düğümü) için bağıl adım boyutu (varsayılan: 0.5). | FLOAT | Hayır | 0.01 - 1.0 |

Parametre ayarlarına bağlı olarak, bu örnekleyici şunları temsil edebilir:

- `seeds_2` — varsayılan ayarlar
- `exp_heun_2_x0` — `solver_type`=`phi_2`, `r`=1.0, `eta`=0.0
- `exp_heun_2_x0_sde` — `solver_type`=`phi_2`, `r`=1.0, `eta`=1.0, `s_noise`=1.0

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `sampler` | Diğer örnekleme düğümlerine aktarılabilen yapılandırılmış bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/tr.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
