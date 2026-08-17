# MiniMax H3 Görüntüden Videoya

MiniMax H3 Image to Video, MiniMax H3 modeli ile video oluşturmak için gereken koşullandırmayı ve boş latent'i hazırlar. Bir metin istemi ve isteğe bağlı olarak videonun ilk ve/veya son karesi için görüntüler alır ve bunları model girdilerine dönüştürür. Anahtar kare görüntüleri yeniden boyutlandırılır, kodlanır ve videonun başına ve sonuna koşullandırmaya eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve anahtar kare görüntülerini koşullandırmaya kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `vae` | Anahtar kare görüntüleri sağlandığında bunları latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet |  |
| `prompt` | Oluşturulacak videoyu tanımlayan metin istemi. Birden çok satırı ve dinamik istemleri destekler. | STRING | Evet |  |
| `width` | Videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ile MAX_RESOLUTION (adım 32) |
| `height` | Videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ile MAX_RESOLUTION (adım 32) |
| `length` | 24 fps'de kare sayısı; modelin 17k+5 ızgarasına yukarı yuvarlanır (124 ≈ ~5 sn; eğitim aralığı ~124-362'dir, daha uzun değerler test edilmemiştir) (varsayılan: 124). | INT | Evet | 5 ile 3600 (adım 17) |
| `first_frame` | Videonun ilk karesi olarak kullanılan isteğe bağlı görüntü. Tam tuval boyutuna genişletilir, bu nedenle en-boy oranı korunmaz. Giriş grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |
| `last_frame` | Videonun son karesi olarak kullanılan isteğe bağlı görüntü. En-boy oranını koruyarak tuvali kaplayacak şekilde kırpılır. Giriş grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |

`first_frame` ve/veya `last_frame` sağlandığında, anahtar kare görüntüleri VAE ile kodlanır ve sırasıyla 0. kareye ve son kareye koşullandırmaya eklenir. Hiçbiri sağlanmadığında, düğüm yalnızca istemle çalışır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kodlanmış istemi ve anahtar kare görüntüleri sağlandığında videonun ilk ve son karelerine yerleştirilmiş kodlanmış anahtar kareleri içeren MiniMax H3 modeli için koşullandırma. | CONDITIONING |
| `latent` | İstenen genişlik, yükseklik ve kare sayısıyla oluşturulacak videoyu ve ona eşlik eden ses parçasını temsil eden boş latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
