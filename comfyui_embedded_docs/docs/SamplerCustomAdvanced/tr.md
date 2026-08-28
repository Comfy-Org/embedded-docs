# GelişmişÖzelÖrnekleyici

SamplerCustomAdvanced düğümü, özel gürültü, rehberlik ve örnekleme yapılandırmaları kullanarak gelişmiş latent uzay örneklemesi gerçekleştirir. Özelleştirilebilir gürültü üretimi ve sigma zamanlamalarıyla yönlendirilmiş bir örnekleme süreci aracılığıyla bir latent görüntüyü işler ve hem nihai örneklenmiş çıktıyı hem de mevcut olduğunda gürültüden arındırılmış bir sürümü üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `gürültü` | Örnekleme süreci için başlangıç gürültü desenini ve tohumunu sağlayan gürültü üreteci | NOISE | Evet | - |
| `rehber` | Örnekleme sürecini istenen çıktılara yönlendiren rehberlik modeli | GUIDER | Evet | - |
| `örnekleyici` | Üretim sırasında latent uzayın nasıl tarandığını tanımlayan örnekleme algoritması | SAMPLER | Evet | - |
| `sigmalar` | Örnekleme adımları boyunca gürültü seviyelerini kontrol eden sigma zamanlaması | SIGMAS | Evet | - |
| `gizli_görüntü` | Örnekleme için başlangıç noktası olarak hizmet eden başlangıç latent temsili. Seçici gürültü giderme için isteğe bağlı `noise_mask` ve gelişmiş latent işleme için isteğe bağlı `downscale_ratio_spacial` ve `downscale_ratio_temporal` anahtarlarını destekler | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `çıktı` | Örnekleme sürecini tamamladıktan sonra elde edilen nihai örneklenmiş latent temsil. Girdi latentindeki `downscale_ratio_spacial` veya `downscale_ratio_temporal` anahtarları bu çıktıdan kaldırılır | LATENT |
| `gürültüsüz_çıktı` | Örnekleme süreci ara bir temiz tahmin (x0) ürettiğinde çıktının gürültüden arındırılmış bir sürümü; aksi takdirde çıktıyla aynısını döndürür. Mevcut olduğunda, bu, modelin her adımda temiz latente ilişkin en iyi tahminini temsil eder | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
