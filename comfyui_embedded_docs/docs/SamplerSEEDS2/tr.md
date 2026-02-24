> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/tr.md)

Bu düğüm, görüntü oluşturmak için yapılandırılabilir bir örnekleyici sağlar. SEEDS-2 algoritmasını uygular; bu, stokastik bir diferansiyel denklem (SDE) çözücüsüdür. Parametrelerini ayarlayarak, `seeds_2`, `exp_heun_2_x0` ve `exp_heun_2_x0_sde` dahil olmak üzere birkaç özel örnekleyici gibi davranacak şekilde yapılandırabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Evet | `"phi_1"`<br>`"phi_2"` | Örnekleyici için temel çözücü algoritmasını seçer. |
| `eta` | FLOAT | Hayır | 0.0 - 100.0 | Stokastik güç (varsayılan: 1.0). |
| `s_noise` | FLOAT | Hayır | 0.0 - 100.0 | SDE gürültü çarpanı (varsayılan: 1.0). |
| `r` | FLOAT | Hayır | 0.01 - 1.0 | Ara aşama (c2 düğümü) için göreli adım boyutu (varsayılan: 0.5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Diğer örnekleme düğümlerine aktarılabilen yapılandırılmış bir örnekleyici nesnesi. |
