SamplerLCM düğümü, her adımda ayarlanabilir gürültü parametrelerine sahip bir LCM (Gizli Tutarlılık Modeli) örnekleyicisi sağlar. Bu düğüm, her örnekleme adımında uygulanan gürültüyü kontrol etmenize olanak tanıyarak örnekleme sürecinin ince ayarlı bir şekilde düzenlenmesini sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `s_noise` | İlk adımdaki adım başına gürültü çarpanı. 1,0 değeri modelin eğitim gürültü ölçeğiyle eşleşir. (varsayılan: 1,0) | FLOAT | Evet | 0,0 ile 64,0 (adım: 0,01) |
| `s_noise_end` | Son adımdaki adım başına gürültü çarpanı. Sabit bir gürültü programı için `s_noise` ile aynı değere ayarlayın. (varsayılan: 1,0) | FLOAT | Evet | 0,0 ile 64,0 (adım: 0,01) |
| `noise_clip_std` | Adım başına gürültüyü +/- N standart sapma aralığına sıkıştırır. 0 değeri sıkıştırmayı devre dışı bırakır. (varsayılan: 0,0) | FLOAT | Evet | 0,0 ile 10,0 (adım: 0,01) |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | Yapılandırılmış LCM örnekleyici nesnesi, bir örnekleme iş akışında kullanılmaya hazırdır. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/tr.md)

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
