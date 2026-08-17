# SamplerLCM

SamplerLCM düğümü, her adımda ayarlanabilir gürültü ayarlarına sahip bir LCM (Latent Consistency Model) örnekleyici sağlar. `s_noise` parametresi, modelin eğitim gürültü ölçeğinde bir çarpan görevi görür ve her örnekleme adımında uygulanan gürültü üzerinde ince ayar yapılmasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `s_noise` | İlk adımdaki adım başına gürültü çarpanı (1.0 = eğitimle eşleşme). Varsayılan: 1.0. | FLOAT | Evet | 0.0 - 64.0 (adım: 0.01) |
| `s_noise_end` | Son adımdaki adım başına gürültü çarpanı. Sabit bir program için `s_noise` ile aynı değere ayarlayın. Varsayılan: 1.0. | FLOAT | Evet | 0.0 - 64.0 (adım: 0.01) |
| `noise_clip_std` | Adım başına gürültüyü +/- N*std ile sınırlar. 0 devre dışı bırakır. Varsayılan: 0.0. | FLOAT | Evet | 0.0 - 10.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | Yapılandırılmış LCM örnekleyici nesnesi; bir örnekleme iş akışında kullanıma hazırdır. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/tr.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
