> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/tr.md)

LTXV Empty Latent Audio düğümü, boş (sıfırlarla doldurulmuş) gizli ses tensörlerinden oluşan bir toplu işlem oluşturur. Gizli uzay için doğru boyutları (örneğin kanal sayısı ve frekans bölmeleri) belirlemek üzere sağlanan bir Audio VAE modelinin yapılandırmasını kullanır. Bu boş gizli tensör, ComfyUI içindeki ses üretimi veya manipülasyon iş akışları için bir başlangıç noktası görevi görür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | Evet | 1 - 1000 | Kare sayısı. Varsayılan değer 97'dir. |
| `frame_rate` | INT | Evet | 1 - 1000 | Saniyedeki kare sayısı. Varsayılan değer 25'tir. |
| `batch_size` | INT | Evet | 1 - 4096 | Toplu işteki gizli ses örneklerinin sayısı. Varsayılan değer 1'dir. |
| `audio_vae` | VAE | Evet | Yok | Yapılandırma alınacak Audio VAE modeli. Bu parametre zorunludur. |

**Not:** `audio_vae` girdisi zorunludur. Sağlanmazsa düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `Latent` | LATENT | Girdi Audio VAE modeliyle eşleşecek şekilde yapılandırılmış, yapısı (samples, sample_rate, type) olan boş bir gizli ses tensörü. |
