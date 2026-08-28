# AV Latent Ayır

LTXVSeparateAVLatent düğümü, birleşik bir görsel-işitsel latent'i iki ayrı latent'e böler: biri video verisini, diğeri ses verisini içerir. Bu, LTXV veya MiniMax H3 gibi herhangi bir görsel-işitsel modelle çalışır. Samples tensörü, ilk boyutu boyunca bölünür; ilk öğe video latent haline gelirken ikinci öğe ses latent haline gelir. Bir gürültü maskesi mevcutsa, aynı şekilde bölünür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `av_latent` | Video ve ses latentlerine ayrıştırılacak birleşik görsel-işitsel latent temsili. | LATENT | Evet | N/A |

**Not:** Girdi latent'inin `samples` tensörünün ilk boyutunda (batch boyutu) en az iki öğeye sahip olması beklenir. İlk öğe video latent'i için, ikinci öğe ise ses latent'i için kullanılır. Bir `noise_mask` mevcutsa, aynı şekilde bölünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_latent` | Ayrıştırılmış video verisini içeren latent temsili. | LATENT |
| `audio_latent` | Ayrıştırılmış ses verisini içeren latent temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/tr.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
