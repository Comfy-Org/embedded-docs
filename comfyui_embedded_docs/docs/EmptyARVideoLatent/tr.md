# Genel Bakış

EmptyARVideoLatent düğümü, video oluşturma için boş, temiz bir latent temsil oluşturur. Belirtilen boyutlar, en-boy oranı ve uzunlukta sıfırlardan oluşan bir tensör sağlayarak video oluşturma sürecini başlatmak için kullanılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Video karelerinin piksel cinsinden genişliği (varsayılan: 832) | INT | Evet | 16 ila 8192 (adım: 16) |
| `height` | Video karelerinin piksel cinsinden yüksekliği (varsayılan: 480) | INT | Evet | 16 ila 8192 (adım: 16) |
| `length` | Videodaki kare sayısı (varsayılan: 81) | INT | Evet | 1 ila 1024 (adım: 4) |
| `batch_size` | Tek bir grupta oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Belirtilen boyutlar, uzunluk ve grup boyutuyla boş bir video latent alanını temsil eden sıfırlarla doldurulmuş bir latent tensör. Tensör şekli [batch_size, 16, lat_t, height/8, width/8] şeklindedir; burada lat_t, uzunluktan hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
