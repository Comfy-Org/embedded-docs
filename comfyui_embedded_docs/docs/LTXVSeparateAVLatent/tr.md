# AV Latent Ayır

LTXVSeparateAVLatent düğümü, birleşik ses-görüntü latent temsilini alır ve iki ayrı latente böler: biri video, diğeri ses için. LTXV veya MiniMax H3 gibi herhangi bir ses-görüntü modeliyle çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `av_latent` | Ayrıştırılacak birleşik ses-görüntü latent temsili. | LATENT | Evet | N/A |

**Not:** Girdi latentinin `samples` tensörünün ilk boyutunda (batch boyutu) en az iki öğe bulunması beklenir. İlk öğe video latenti için, ikinci öğe ise ses latenti için kullanılır. Bir `noise_mask` mevcutsa, aynı şekilde bölünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_latent` | Ayrıştırılmış video verilerini içeren latent temsil. | LATENT |
| `audio_latent` | Ayrıştırılmış ses verilerini içeren latent temsil. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/tr.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
