# Sampler AR Video

Sampler AR Video düğümü, Causal Forcing veya Self-Forcing tekniklerini kullanan otoregresif video modelleri için özel bir örnekleme yöntemi sağlar. Otoregresif (AR) döngüyle ilgili tüm parametreleri doğrudan iş akışı içinde yönetir; böylece modelin video karelerini adım adım nasıl üreteceğini yapılandırmak kolaylaşır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Otoregresif blok başına kare sayısı. 1 değeri, modelin her seferinde bir kare ürettiği anlamına gelir (kare kare), 3 değeri ise üç kareyi birlikte ürettiği anlamına gelir (parça parça). Bu ayar, kontrol noktasının eğitim moduyla eşleşmelidir. Varsayılan: 1. | INT | Evet | 1 ila 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SAMPLER` | Belirtilen otoregresif parametrelerle "ar_video" örnekleme işlevini kullanan yapılandırılmış bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/tr.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
