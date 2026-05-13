> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/tr.md)

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

LTXV Boş Latent Ses düğümü, boş (sıfır doldurulmuş) latent ses tensörlerinden oluşan bir grup oluşturur. Kanal sayısı ve frekans aralıkları gibi latent uzay için doğru boyutları belirlemek amacıyla sağlanan bir Ses VAE modelinin yapılandırmasını kullanır. Bu boş latent, ComfyUI içindeki ses oluşturma veya işleme iş akışları için bir başlangıç noktası görevi görür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | Evet | 1 ile 1000 arası | Kare sayısı. Varsayılan değer 97'dir. |
| `frame_rate` | INT | Evet | 1 ile 1000 arası | Saniyedeki kare sayısı. Varsayılan değer 25'tir. |
| `batch_size` | INT | Evet | 1 ile 4096 arası | Gruptaki latent ses örneklerinin sayısı. Varsayılan değer 1'dir. |
| `audio_vae` | VAE | Evet | Yok | Yapılandırmanın alınacağı Ses VAE modeli. Bu parametre zorunludur. |

**Not:** `audio_vae` girişi zorunludur. Sağlanmazsa düğüm bir hata verecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `Latent` | LATENT | Giriş Ses VAE'siyle eşleşecek şekilde yapılandırılmış, (batch_size, z_channels, num_audio_latents, audio_freq) yapısında boş bir latent ses tensörü. Çıkış ayrıca "audio" olarak ayarlanmış bir `type` alanı içerir. |

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`
