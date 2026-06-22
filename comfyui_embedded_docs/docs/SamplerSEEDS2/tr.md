# SamplerSEEDS2

Bu düğüm, görüntü oluşturmak için yapılandırılabilir bir örnekleyici sağlar. Stokastik diferansiyel denklem (SDE) çözücüsü olan SEEDS-2 algoritmasını uygular. Parametrelerini ayarlayarak, `seeds_2`, `exp_heun_2_x0` ve `exp_heun_2_x0_sde` dahil olmak üzere çeşitli belirli örnekleyiciler gibi davranacak şekilde yapılandırabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `solver_type` | Örnekleyici için temel çözücü algoritmasını seçer. | COMBO | Evet | `"phi_1"`<br>`"phi_2"` |
| `eta` | Stokastik güç (varsayılan: 1,0). | FLOAT | Hayır | 0,0 - 100,0 |
| `s_noise` | SDE gürültü çarpanı (varsayılan: 1,0). | FLOAT | Hayır | 0,0 - 100,0 |
| `r` | Ara aşama (c2 düğümü) için göreceli adım boyutu (varsayılan: 0,5). | FLOAT | Hayır | 0,01 - 1,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Diğer örnekleme düğümlerine aktarılabilen yapılandırılmış bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/tr.md)

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
