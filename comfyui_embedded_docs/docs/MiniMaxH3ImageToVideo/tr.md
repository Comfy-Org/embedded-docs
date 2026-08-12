# MiniMax H3 Görüntüden Videoya

Bu düğüm, MiniMax H3 modeli ile bir video oluşturmak için gereken conditioning'i ve boş latent'i hazırlar. Bir metin istemi ve isteğe bağlı olarak videonun ilk ve/veya son karesi için görseller alır ve bunları model girdilerine dönüştürür. Anahtar kare görüntüleri yeniden boyutlandırılır, kodlanır ve videonun başına ve sonuna conditioning'e eklenir.

## Girişler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve anahtar kare görüntülerini conditioning'e kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `vae` | Anahtar kare görüntüleri sağlandığında bunları latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet |  |
| `prompt` | Oluşturulacak videoyu tanımlayan metin istemi. Birden çok satırı ve dinamik istemleri destekler. | STRING | Evet |  |
| `genişlik` | Videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ile MAX_RESOLUTION (adım 32) |
| `yükseklik` | Videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ile MAX_RESOLUTION (adım 32) |
| `uzunluk` | 24 fps'de kare sayısı, modelin 17k+5 ızgarasına yukarı yuvarlanır (124 = ~5s; eğitim aralığı ~124-362'dir, daha uzunu test edilmemiştir) (varsayılan: 124). | INT | Evet | 5 ile 3600 (adım 17) |
| `ilk_kare` | Videonun ilk karesi olarak kullanılan isteğe bağlı görsel. Tam tuval boyutuna uzatılır, bu nedenle en-boy oranı korunmaz. Giriş grubunun yalnızca ilk görseli kullanılır. | IMAGE | Hayır |  |
| `son_kare` | Videonun son karesi olarak kullanılan isteğe bağlı görsel. En-boy oranı korunurken tuvali kaplayacak şekilde kırpılır. Giriş grubunun yalnızca ilk görseli kullanılır. | IMAGE | Hayır |  |

`first_frame` ve/veya `last_frame` sağlandığında, anahtar kare görüntüleri VAE ile kodlanır ve sırasıyla 0. kareye ve son kareye conditioning'e eklenir. Hiçbiri sağlanmadığında, düğüm yalnızca istemden çalışır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `pozitif` | Kodlanmış istemi ve anahtar kare görüntüleri sağlandığında, MiniMax H3 modeli için kodlanmış anahtar kareleri ve kare sayısını içeren conditioning. | CONDITIONING |
| `latent` | İstenen genişlik, yükseklik ve kare sayısıyla oluşturulacak videoyu temsil eden boş latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `46efc87bd46f4a86cb6df37c75f960419a2a98b34480e7dc0023c9d87903870b`
