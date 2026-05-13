> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/tr.md)

Bu düğüm, görüntü oluşturmak için yapılandırılabilir bir örnekleyici sağlar. Stokastik diferansiyel denklem (SDE) çözücüsü olan SEEDS-2 algoritmasını uygular. Parametrelerini ayarlayarak, `seeds_2`, `exp_heun_2_x0` ve `exp_heun_2_x0_sde` dahil olmak üzere çeşitli belirli örnekleyiciler gibi davranacak şekilde yapılandırabilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Evet | `"phi_1"`<br>`"phi_2"` | Örnekleyici için temel çözücü algoritmasını seçer. |
| `eta` | FLOAT | Hayır | 0,0 - 100,0 | Stokastik güç (varsayılan: 1,0). |
| `s_noise` | FLOAT | Hayır | 0,0 - 100,0 | SDE gürültü çarpanı (varsayılan: 1,0). |
| `r` | FLOAT | Hayır | 0,01 - 1,0 | Ara aşama (c2 düğümü) için göreceli adım boyutu (varsayılan: 0,5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Diğer örnekleme düğümlerine aktarılabilen yapılandırılmış bir örnekleyici nesnesi. |

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
