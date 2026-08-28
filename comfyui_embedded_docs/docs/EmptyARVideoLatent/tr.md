# EmptyARVideoLatent

## Genel Bakış

EmptyARVideoLatent düğümü, video üretimi için boş bir latent temsili oluşturur. Belirtilen boyutlara, en-boy oranına ve uzunluğa sahip sıfırlardan oluşan bir tensör sağlayarak video üretim sürecini başlatmak için kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Video karelerinin piksel cinsinden genişliği (varsayılan: 832) | INT | Evet | 16 ile 8192 (step: 16) |
| `height` | Video karelerinin piksel cinsinden yüksekliği (varsayılan: 480) | INT | Evet | 16 ile 8192 (step: 16) |
| `length` | Videodaki kare sayısı (varsayılan: 81) | INT | Evet | 1 ile 1024 (step: 4) |
| `batch_size` | Tek bir yığında oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `LATENT` | Belirtilen boyutlara, uzunluğa ve yığın boyutuna sahip boş bir video latent alanını temsil eden sıfırlarla doldurulmuş bir latent tensörü. Tensör şekli [batch_size, 16, lat_t, height/8, width/8] biçimindedir; burada lat_t = ((length - 1) // 4) + 1, istenen uzunluktan türetilen latent zaman adımlarının sayısıdır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
