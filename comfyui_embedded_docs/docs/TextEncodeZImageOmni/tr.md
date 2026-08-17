# TextEncodeZImageOmni

TextEncodeZImageOmni düğümü, bir metin istemini, isteğe bağlı referans görüntülerle birlikte, görüntü üretim modelleri için uygun bir koşullandırma formatına kodlayan gelişmiş bir koşullandırma düğümüdür. En fazla üç görüntüyü işleyebilir; bu görüntüleri isteğe bağlı olarak bir görüntü kodlayıcı ve/veya bir VAE ile kodlayarak referans latentleri üretebilir ve bu görsel referansları belirli bir şablon yapısı kullanarak metin istemiyle bütünleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin istemini tokenize etmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `image_encoder` | İsteğe bağlı görüntü kodlayıcı modeli. Sağlanırsa, giriş görüntülerini kodlamak için kullanılır ve elde edilen yerleştirmeler koşullandırmaya eklenir. | CLIPVision | Hayır |  |
| `prompt` | Kodlanacak metin istemi. Bu alan çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet |  |
| `auto_resize_images` | Etkinleştirildiğinde (varsayılan: True), giriş görüntüleri VAE'ye kodlanmadan önce piksel alanlarına göre otomatik olarak yeniden boyutlandırılır. Bu gelişmiş bir ayardır. | BOOLEAN | Hayır |  |
| `vae` | İsteğe bağlı VAE modeli. Sağlanırsa, giriş görüntülerini latent temsillere kodlamak için kullanılır ve bu temsiller referans latentleri olarak koşullandırmaya eklenir. | VAE | Hayır |  |
| `image1` | İlk isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |
| `image2` | İkinci isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |
| `image3` | Üçüncü isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |

**Not:** Düğüm en fazla üç görüntü kabul edebilir (`image1`, `image2`, `image3`). `image_encoder` ve `vae` girdileri yalnızca en az bir görüntü sağlandığında kullanılır. `auto_resize_images` True olduğunda ve bir `vae` bağlandığında, görüntüler kodlamadan önce toplam piksel alanı 1024x1024 piksele yakın olacak şekilde ve boyutları 8'in katlarına yuvarlanarak yeniden boyutlandırılır. Hiçbir görüntü sağlanmazsa, düğüm metin istemini görsel referans olmadan kodlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Nihai koşullandırma çıktısı; kodlanmış metin istemini içerir ve görüntü sağlandıysa kodlanmış görüntü yerleştirmelerini ve/veya referans latentlerini de içerebilir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/tr.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
