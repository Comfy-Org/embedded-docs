# EmptyAceStep1.5LatentAudio

**Empty Ace Step 1.5 Latent Audio** düğümü, ses işleme için tasarlanmış boş bir latent tensör oluşturur. Belirtilen süre ve toplu iş boyutunda sessiz bir ses latent'i üretir; bu, ComfyUI'de ses üretim iş akışları için başlangıç noktası olarak kullanılabilir. Düğüm, girdi saniyelerine ve sabit bir örnekleme hızına dayanarak latent uzunluğunu hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Oluşturulacak sesin saniye cinsinden süresi (varsayılan: 120.0). | FLOAT | Evet | 1.0 - 1000.0 |
| `batch_size` | Toplu işteki latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | "audio" tür tanımlayıcısına sahip, sessiz sesi temsil eden boş bir latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `8d2b0b8ea110362d5e43a72a27df0ff2012a8577fbaa4fef2bd7905c9c64bd6a`
