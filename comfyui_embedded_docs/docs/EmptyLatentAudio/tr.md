# EmptyLatentAudio Düğümü

EmptyLatentAudio düğümü, ses işleme için boş bir latent tensör oluşturur. Belirtilen süre ve grup boyutuna sahip boş bir ses latent temsili üretir; bu temsil, ses üretimi veya işleme iş akışları için başlangıç noktası olarak kullanılabilir. Düğüm, ses süresi ve örnekleme hızına bağlı olarak uygun latent boyutlarını otomatik olarak hesaplar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `saniye` | Sesin saniye cinsinden süresi (varsayılan: 47.6) | FLOAT | Evet | 1.0 - 1000.0 |
| `toplu_boyut` | Gruptaki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Belirtilen süre ve grup boyutuna sahip, ses işleme için boş bir latent tensör döndürür. Tensör, [batch_size, 64, length] şeklindedir; burada length, ses süresi ve örnekleme hızından hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`
