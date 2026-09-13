# EmptyARVideoLatent

EmptyARVideoLatent düğümü, video oluşturma için boş bir latent temsili oluşturur. İstenen genişlik, yükseklik, kare sayısı ve toplu iş boyutunu kullanarak sıfırlardan oluşan bir tensör oluşturur; bu tensör daha sonra bir video oluşturma sürecini başlatmak için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Video karelerinin piksel cinsinden genişliği (varsayılan: 832) | INT | Evet | 16 ile 8192 (step: 16) |
| `height` | Video karelerinin piksel cinsinden yüksekliği (varsayılan: 480) | INT | Evet | 16 ile 8192 (step: 16) |
| `length` | Videodaki kare sayısı (varsayılan: 81) | INT | Evet | 1 ile 1024 (step: 4) |
| `batch_size` | Tek bir toplu işlemde oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 64 |

Not: Dahili latent boyutu bu girdilerden türetilir. `width` ve `height` 8'e bölünür ve latent zaman adımı sayısı `((length - 1) // 4) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Belirtilen boyutlar, uzunluk ve toplu iş boyutuyla boş bir video latent uzayını temsil eden, sıfırlarla doldurulmuş bir latent tensör. Tensör şekli [batch_size, 16, lat_t, height/8, width/8] olup burada lat_t = ((length - 1) // 4) + 1, istenen uzunluktan türetilen latent zaman adımı sayısıdır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
