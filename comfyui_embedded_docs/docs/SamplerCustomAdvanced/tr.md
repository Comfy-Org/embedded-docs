# GelişmişÖzelÖrnekleyici

SamplerCustomAdvanced düğümü, özel gürültü, rehberlik ve örnekleme yapılandırmaları kullanarak gelişmiş latent uzay örneklemesi gerçekleştirir. Latent görüntüyü, özelleştirilebilir gürültü üretimi ve sigma çizelgeleriyle yönlendirilmiş bir örnekleme sürecinden geçirir; mevcut olduğunda hem nihai örneklenmiş çıktıyı hem de gürültüden arındırılmış bir sürümü üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `noise` | Örnekleme süreci için başlangıç gürültü desenini ve tohum değerini sağlayan gürültü üreteci | NOISE | Evet | - |
| `guider` | Örnekleme sürecini istenen çıktılara yönlendiren rehberlik modeli | GUIDER | Evet | - |
| `sampler` | Üretim sırasında latent uzayın nasıl gezileceğini tanımlayan örnekleme algoritması | SAMPLER | Evet | - |
| `sigmas` | Örnekleme adımları boyunca gürültü seviyelerini kontrol eden sigma çizelgesi | SIGMAS | Evet | - |
| `latent_image` | Örnekleme için başlangıç noktası görevi gören başlangıç latent temsili. Seçmeli gürültüden arındırma için isteğe bağlı `noise_mask` ve gelişmiş latent işleme için isteğe bağlı `downscale_ratio_spacial` ve `downscale_ratio_temporal` anahtarlarını destekler | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Örnekleme süreci tamamlandıktan sonraki nihai örneklenmiş latent temsil. Girdi latentindeki `downscale_ratio_spacial` veya `downscale_ratio_temporal` anahtarları bu çıktıdan kaldırılır | LATENT |
| `denoised_output` | Örnekleme süreci ara bir temiz tahmin (x0) ürettiğinde çıktının gürültüden arındırılmış bir sürümü; aksi takdirde çıktıyla aynı değeri döndürür. Mevcut olduğunda, modelin her adımda temiz latente ilişkin en iyi tahminini temsil eder | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
