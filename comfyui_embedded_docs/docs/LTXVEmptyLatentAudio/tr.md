# LTXV Boş Latent Ses

The LTXV Empty Latent Audio düğümü, bir grup boş (sıfırlarla doldurulmuş) latent ses tensörü oluşturur. Bağlı bir Audio VAE modelinin yapılandırmasını okuyarak kanal sayısı ve frekans kutuları gibi doğru latent boyutlarını belirler ve kare sayısı ile kare hızından kaç ses latentinin gerektiğini hesaplar. Ortaya çıkan boş latent, ses üretimi veya düzenleme iş akışları için başlangıç noktası olarak kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `frames_number` | Kare sayısı. Varsayılan değer 97'dir. | INT | Evet | 1 ila 1000 |
| `frame_rate` | Saniyedeki kare sayısı. Varsayılan değer 25.0'dır. Bu girdi FLOAT veya INT değerlerini kabul eder. | FLOAT | Evet | 1.0 ila 1000.0 |
| `batch_size` | Toplu işteki latent ses örneği sayısı. Varsayılan değer 1'dir. | INT | Evet | 1 ila 4096 |
| `audio_vae` | Yapılandırmasının alınacağı Audio VAE modeli. "Audio VAE" olarak görüntülenir. | VAE | Evet | N/A |

**Not:** `audio_vae` girdisi zorunludur. Sağlanmazsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Latent` | (batch_size, z_channels, num_audio_latents, audio_freq) şeklinde boş bir latent ses tensörü; burada kanal sayısı ve frekans kutuları Audio VAE'den gelir ve ses latentlerinin sayısı `frames_number` ile `frame_rate` değerlerinden türetilir. Çıktı ayrıca "audio" olarak ayarlanmış bir `type` alanı içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
