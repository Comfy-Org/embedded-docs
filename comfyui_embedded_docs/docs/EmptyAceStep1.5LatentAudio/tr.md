# EmptyAceStep1.5LatentAudio

Empty Ace Step 1.5 Latent Audio düğümü, ses işleme için tasarlanmış boş bir latent tensör oluşturur. Belirtilen süre ve parti boyutunda sessiz bir ses latentı üretir; bu, ComfyUI'de ses üretim iş akışları için bir başlangıç noktası olarak kullanılabilir. Düğüm, latent uzunluğunu girdi saniyelerine ve sabit bir örnekleme hızına göre hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Oluşturulacak sesin süresi, saniye cinsinden (varsayılan: 120.0). | FLOAT | Evet | 1.0 - 1000.0 |
| `batch_size` | Partideki latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Sessiz sesi temsil eden ve "audio" tür tanımlayıcısına sahip boş bir latent tensördür. Çıktı ayrıca, ses işlemede zamansal ölçek küçültme için kullanılan 1764 değerinde bir `downscale_ratio_temporal` içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
