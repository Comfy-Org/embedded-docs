# EmptyAceStep1.5LatentAudio

The Empty Ace Step 1.5 Latent Audio düğümü, ses işleme için tasarlanmış boş bir latent tensör oluşturur. Belirtilen süre ve parti boyutunda sessiz bir ses latent tensörü üretir; bu tensör, ComfyUI'de ses üretim iş akışları için başlangıç noktası olarak kullanılabilir. Düğüm, latent uzunluğunu giriş saniyelerine ve sabit bir örnekleme hızına göre hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Üretilecek sesin süresi (saniye cinsinden) (varsayılan: 120.0). | FLOAT | Evet | 1.0 - 1000.0 |
| `batch_size` | Partideki latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `LATENT` | Sessiz sesi temsil eden, "audio" tür tanımlayıcısına sahip boş bir latent tensör. Çıktı ayrıca, ses işlemede zamansal aşağı ölçekleme için kullanılan 1764 değerinde bir `downscale_ratio_temporal` içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
