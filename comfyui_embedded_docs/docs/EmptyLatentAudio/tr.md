# Boş Gizli Ses

Empty Latent Audio, ses işleme için boş bir latent tensör oluşturur. Belirtilen süre ve batch boyutu ile boş bir ses latent temsili üretir; bu, ses üretimi veya işleme iş akışları için bir başlangıç noktası olarak kullanılabilir. Düğüm, ses süresine ve örnekleme hızına bağlı olarak uygun latent boyutlarını otomatik olarak hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `saniye` | Sesin süresi saniye cinsinden (varsayılan: 47.6) | FLOAT | Evet | 1.0 - 1000.0 |
| `toplu_boyut` | Batch içindeki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Belirtilen süre ve batch boyutu ile ses işleme için boş bir latent tensör döndürür. Tensörün şekli [batch_size, 64, length] biçimindedir; burada length, ses süresi ve örnekleme hızından hesaplanır. Çıktı ayrıca türün "audio" olduğunu ve 2048'lik bir zamansal alt örnekleme oranını belirten meta veriler içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
