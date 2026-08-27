# MiniMax H3 Görüntüden Videoya

Bu düğüm, MiniMax H3 modeli ile video oluşturmak için gereken koşullandırmayı ve boş latent hazırlar. Bir metin istemi alır ve isteğe bağlı olarak videonun ilk ve/veya son karesi için görüntüler alır; bunları model girdilerine dönüştürür. Ana kare görüntüleri yeniden boyutlandırılır, kodlanır ve videonun başına ve sonuna koşullandırmaya eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Prompt'u tokenize etmek ve ana kare görüntülerini koşullandırmaya kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `vae` | Ana kare görüntüleri sağlandığında bunları latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet |  |
| `prompt` | Üretilecek videoyu tanımlayan metin istemi. Çok satırlı ve dinamik istemleri destekler. | STRING | Evet |  |
| `genişlik` | Videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ila MAX_RESOLUTION (adım 32) |
| `yükseklik` | Videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ila MAX_RESOLUTION (adım 32) |
| `uzunluk` | 24 fps'de kare sayısı; modelin 17k+5 ızgarasına yukarı yuvarlanır (124 = ~5 sn; eğitim aralığı ~124-362, daha uzunları test edilmemiştir) (varsayılan: 124). | INT | Evet | 5 ila 3600 (adım 17) |
| `ilk_kare` | Videonun ilk karesi olarak kullanılan isteğe bağlı görüntü. Tam tuval boyutuna uzatılır, bu nedenle en-boy oranı korunmaz. Girdi grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |
| `son_kare` | Videonun son karesi olarak kullanılan isteğe bağlı görüntü. En-boy oranını koruyarak tuvali kaplayacak şekilde kırpılır. Girdi grubunun yalnızca ilk görüntüsü kullanılır. | IMAGE | Hayır |  |

`first_frame` ve/veya `last_frame` sağlandığında, ana kare görüntüleri VAE ile kodlanır ve sırasıyla 0. kareye ve son kareye koşullandırmaya eklenir. Hiçbiri sağlanmadığında düğüm yalnızca prompt ile çalışır. İstenen `length`, en yakın geçerli kare sayısına (17k + 5) yukarı yuvarlanır; bu nedenle etkin kare sayısı istenenden biraz daha yüksek olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | MiniMax H3 modeli için kodlanmış prompt ile, ana kare görüntüleri sağlandığında kodlanmış ana kareleri ve kare sayısını içeren koşullandırma. | CONDITIONING |
| `latent` | Üretilecek içeriği temsil eden, istenen genişlik, yükseklik ve kare sayısına sahip boş ses-video latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
