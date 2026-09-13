# GelişmişÖzelÖrnekleyici

SamplerCustomAdvanced düğümü, özel gürültü, yönlendirme ve örnekleme yapılandırmalarını kullanarak gelişmiş latent uzay örneklemesi gerçekleştirir. Özelleştirilebilir bir gürültü üreteci ve sigma çizelgesiyle yönlendirilmiş bir örnekleme süreci boyunca bir latent görüntüyü işler; mevcut olduğunda hem nihai örneklenmiş çıktıyı hem de gürültüden arındırılmış bir sürümü üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `noise` | Örnekleme süreci için başlangıç gürültü desenini ve tohumu sağlayan gürültü üreteci | NOISE | Evet | - |
| `guider` | Örnekleme sürecini istenen çıktıya doğru yönlendiren yönlendirme modeli | GUIDER | Evet | - |
| `sampler` | Üretim sırasında latent uzayda nasıl ilerleneceğini tanımlayan örnekleme algoritması | SAMPLER | Evet | - |
| `sigmas` | Örnekleme adımları boyunca gürültü seviyelerini kontrol eden sigma çizelgesi | SIGMAS | Evet | - |
| `latent_image` | Örnekleme için başlangıç noktası olarak hizmet eden başlangıç latent temsili. Seçmeli gürültüden arındırma için isteğe bağlı bir `noise_mask` anahtarını ve gelişmiş latent işleme için isteğe bağlı `downscale_ratio_spacial` ve `downscale_ratio_temporal` anahtarlarını destekler | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Örnekleme süreci tamamlandıktan sonra nihai örneklenmiş latent temsil. Girdi latent temsilindeki tüm `downscale_ratio_spacial` veya `downscale_ratio_temporal` anahtarları bu çıktıdan kaldırılır | LATENT |
| `denoised_output` | Örnekleme süreci bir ara temiz tahmin (x0) ürettiğinde çıktının gürültüden arındırılmış bir sürümü; aksi takdirde `output` ile aynısını döndürür. Mevcut olduğunda bu, modelin temiz latent hakkındaki en iyi tahminini temsil eder | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
