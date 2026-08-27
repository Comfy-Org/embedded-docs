# LTXV Boş Latent Ses

LTXV Empty Latent Audio düğümü, sıfırlarla doldurulmuş boş bir latent ses tensör kümesi oluşturur. Sağlanan bir Audio VAE modelinden gelen yapılandırmayı kullanarak latent uzay için doğru boyutları (kanal sayısı ve frekans bölmeleri gibi) belirler ve kare sayısı ile kare hızından ses latentlerinin sayısını hesaplar. Bu boş latent, ComfyUI içindeki ses üretim veya işleme iş akışları için bir başlangıç noktası görevi görür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `frames_number` | Kare sayısı. Varsayılan değer 97'dir. | INT | Evet | 1 ila 1000 |
| `frame_rate` | Saniyedeki kare sayısı. Varsayılan değer 25.0'tır. FLOAT veya INT değerlerini kabul eder. | FLOAT | Evet | 1.0 ila 1000.0 |
| `batch_size` | Kümedeki latent ses örneklerinin sayısı. Varsayılan değer 1'dir. | INT | Evet | 1 ila 4096 |
| `audio_vae` | Yapılandırmanın alınacağı Audio VAE modeli. Bu parametre gereklidir. | VAE | Evet | YOK |

**Not:** `audio_vae` girdisi zorunludur. Sağlanmazsa düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Latent` | Girdi Audio VAE ile eşleşecek şekilde yapılandırılmış, (batch_size, z_channels, num_audio_latents, audio_freq) yapısında boş bir latent ses tensörü. Çıktı ayrıca "audio" olarak ayarlanmış bir `type` alanı da içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
