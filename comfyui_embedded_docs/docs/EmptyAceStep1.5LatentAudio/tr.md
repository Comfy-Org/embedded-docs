# EmptyAceStep1.5LatentAudio

Empty Ace Step 1.5 Latent Audio düğümü, ses üretimi iş akışları için boş (sessiz) bir ses latent tensörü oluşturur. Zamansal uzunluğu istenen süreden hesaplanan 64 kanallı bir latent oluşturur ve bunu aşağı akış ses düğümleri tarafından kullanılmak üzere ses verisi olarak etiketler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Üretilecek sesin saniye cinsinden süresi (varsayılan: 120.0). Latent uzunluğu `seconds * 48000 / 1920` olarak hesaplanır ve en yakın tam sayıya yuvarlanır. | FLOAT | Evet | 1.0 - 1000.0 (adım: 0.01) |
| `batch_size` | Toplu işteki latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Sessiz sesi temsil eden boş bir latent tensörü. Tensör [batch_size, 64, length] şeklindedir; burada length, `seconds` değerinden türetilir. Çıktı ayrıca "audio" tür tanımlayıcısını ve ses işlemede zamansal ölçek küçültme için kullanılan `downscale_ratio_temporal` değeri olan 1764'ü içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
