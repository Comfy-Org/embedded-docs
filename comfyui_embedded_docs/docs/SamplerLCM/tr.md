# SamplerLCM

Bu düğüm, adım başına ayarlanabilir gürültüye sahip bir LCM (Gizli Tutarlılık Modeli) örnekleyicisi sunar. Örnekleme sırasında ne kadar gürültü uygulanacağını kontrol etmenizi sağlar: `s_noise`, modelin eğitim gürültüsü ölçeğinde bir çarpan görevi görür ve gürültü düzeyi ilk adımdan son adıma kadar değişebilir. Yapılandırılan örnekleyici daha sonra bir örnekleme iş akışına dahil edilebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `s_noise` | İlk adımdaki adım başına gürültü çarpanı (1.0 = eğitimle eşleşir). Varsayılan: 1.0. | FLOAT | Evet | 0.0 - 64.0 (adım: 0.01) |
| `s_noise_end` | Son adımdaki adım başına gürültü çarpanı. Sabit bir çizelge için `s_noise` değerine eşit ayarlayın. Varsayılan: 1.0. | FLOAT | Evet | 0.0 - 64.0 (adım: 0.01) |
| `noise_clip_std` | Adım başına gürültüyü +/- N*std değerine sınırlar. 0 devre dışı bırakır. Varsayılan: 0.0. | FLOAT | Evet | 0.0 - 10.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | Yapılandırılmış LCM örnekleyici nesnesi; bir örnekleme iş akışında kullanıma hazırdır. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/tr.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
