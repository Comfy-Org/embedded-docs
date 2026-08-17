# Boş Gizli Ses

EmptyLatentAudio düğümü, ses işleme için boş bir latent tensör oluşturur. Belirtilen süre ve yığın boyutuyla boş bir ses latent temsili üretir; bu temsil, ses üretimi veya işleme akışları için bir başlangıç noktası olarak kullanılabilir. Düğüm, ses süresine ve örnekleme hızına göre uygun latent boyutlarını otomatik olarak hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Sesin saniye cinsinden süresi (varsayılan: 47.6) | FLOAT | Evet | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | Yığındaki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Belirtilen süre ve yığın boyutuna sahip, ses işleme için boş bir latent tensör döndürür. Tensör, [batch_size, 64, length] biçimindedir; burada length, ses süresi ve örnekleme hızından hesaplanır. Çıktı ayrıca, türün "audio" olduğunu ve zamansal ölçek küçültme oranının 2048 olduğunu belirten meta veriler içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
