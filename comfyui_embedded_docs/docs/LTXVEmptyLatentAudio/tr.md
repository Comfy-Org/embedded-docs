# LTXV Boş Latent Ses

LTXV Empty Latent Audio düğümü, sıfırlarla dolu (boş) latent ses tensörlerinden oluşan bir grup oluşturur. Doğru latent uzay boyutlarını (kanal sayısı ve frekans bölmesi gibi) belirlemek için sağlanan Audio VAE modelindeki yapılandırmayı kullanır. Ses latentlerinin sayısı, Audio VAE modeli kullanılarak kare sayısından ve kare hızından hesaplanır. Bu boş latent, ComfyUI içinde ses üretimi veya manipülasyon iş akışları için bir başlangıç noktası görevi görür.

## Girişler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `frames_number` | Kare sayısı. Varsayılan: 97. | INT | Evet | 1 - 1000 |
| `frame_rate` | Saniyedeki kare sayısı. Ondalıklı veya tam sayı değerlerini kabul eder. Varsayılan: 25.0. | FLOAT (veya INT) | Evet | 1.0 - 1000.0 |
| `batch_size` | Gruptaki latent ses örneklerinin sayısı. Varsayılan: 1. | INT | Evet | 1 - 4096 |
| `audio_vae` | Yapılandırmanın alınacağı Audio VAE modeli. | VAE | Evet | N/A |

**Not:** `audio_vae` girişi zorunludur. Sağlanmazsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `Latent` | Giriş Audio VAE'siyle eşleşecek şekilde yapılandırılmış, (batch_size, z_channels, num_audio_latents, audio_freq) yapısında boş bir latent ses tensörü. Çıktı ayrıca "audio" olarak ayarlanmış bir `type` alanı içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
