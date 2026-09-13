# MiniMax H3 Görüntüden Videoya

Bu düğüm, MiniMax H3 modeliyle bir video oluşturmak için gereken koşullandırmayı ve boş latent'i hazırlar. Bir metin istemi ve isteğe bağlı olarak videonun ilk ve/veya son karesi için görüntüler alır ve bunları model girdilerine dönüştürür. Anahtar kare görüntüleri yeniden boyutlandırılır, kodlanır ve videonun başında ve sonunda koşullandırmaya eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve anahtar kare görüntülerini koşullandırmaya kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `vae` | Anahtar kare görüntüleri sağlandığında bunları latent uzayına kodlamak için kullanılan VAE modeli. | VAE | Evet |  |
| `prompt` | Oluşturulacak videoyu tanımlayan metin istemi. Birden çok satırı ve dinamik istemleri destekler. | STRING | Evet |  |
| `width` | Videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 - MAX_RESOLUTION (adım 32) |
| `height` | Videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 - MAX_RESOLUTION (adım 32) |
| `length` | 24 fps'de kare sayısı; modelin 17k+5 ızgarasına yukarı yuvarlanır (124 = ~5 sn; eğitilmiş aralık ~124-362, daha uzunu test edilmemiştir) (varsayılan: 124). | INT | Evet | 5 - 3600 (adım 17) |
| `first_frame` | Videonun ilk karesi olarak kullanılan isteğe bağlı görüntü. Tam tuval boyutuna gerilir, bu nedenle en-boy oranı korunmaz. Girdi grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |
| `last_frame` | Videonun son karesi olarak kullanılan isteğe bağlı görüntü. En-boy oranı korunarak tuvali kaplayacak şekilde kırpılır. Girdi grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |

`first_frame` ve/veya `last_frame` sağlandığında, anahtar kare görüntüleri VAE ile kodlanır ve sırasıyla 0. karede ve son karede koşullandırmaya eklenir. İkisi de sağlanmadığında düğüm yalnızca istemden çalışır. İstenen `length`, en yakın geçerli kare sayısına (17k + 5) yukarı yuvarlanır; bu nedenle etkin kare sayısı istenenden biraz daha yüksek olabilir.

Ses-video latent'i, istenen `width`, `height` ve yuvarlanmış kare sayısıyla eşleşen boş bir çift olarak oluşturulur. Ses kısmı, aynı kare sayısından saniyede 40 ses karesi olacak şekilde boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kodlanmış istemi ve anahtar kare görüntüleri sağlandığında MiniMax H3 modeli için kodlanmış anahtar kareleri ve kare sayısını içeren koşullandırma. | CONDITIONING |
| `latent` | Oluşturulacak içeriği temsil eden, istenen genişlik, yükseklik ve kare sayısına sahip boş ses-video latent'i. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
