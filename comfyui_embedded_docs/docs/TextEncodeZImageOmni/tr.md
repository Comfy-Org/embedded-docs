> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/tr.md)

TextEncodeZImageOmni düğümü, bir metin istemini ve isteğe bağlı referans görüntülerini, görüntü oluşturma modelleri için uygun bir koşullandırma formatına kodlayan gelişmiş bir koşullandırma düğümüdür. En fazla üç görüntüyü işleyebilir, bunları isteğe bağlı olarak bir görüntü kodlayıcı ve/veya VAE ile kodlayarak referans gizil değişkenler üretebilir ve bu görsel referansları belirli bir şablon yapısı kullanarak metin istemiyle bütünleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | | Metin istemini tokenleştirmek ve kodlamak için kullanılan CLIP modeli. |
| `görüntü_kodlayıcı` | CLIPVision | Hayır | | İsteğe bağlı bir görüntü kodlayıcı modeli. Sağlanırsa, giriş görüntülerini kodlamak için kullanılır ve elde edilen gömme vektörleri koşullandırmaya eklenir. |
| `istem` | STRING | Evet | | Kodlanacak metin istemi. Bu alan çok satırlı girişi ve dinamik istemleri destekler. |
| `görüntüleri_otomatik_yeniden_boyutlandır` | BOOLEAN | Hayır | | Etkinleştirildiğinde (varsayılan: True), giriş görüntüleri VAE'ye kodlanmak üzere gönderilmeden önce piksel alanlarına göre otomatik olarak yeniden boyutlandırılır. |
| `vae` | VAE | Hayır | | İsteğe bağlı bir VAE modeli. Sağlanırsa, giriş görüntülerini gizil temsillere kodlamak için kullanılır ve bu temsiller referans gizil değişkenler olarak koşullandırmaya eklenir. |
| `görüntü1` | IMAGE | Hayır | | İlk isteğe bağlı referans görüntüsü. |
| `görüntü2` | IMAGE | Hayır | | İkinci isteğe bağlı referans görüntüsü. |
| `görüntü3` | IMAGE | Hayır | | Üçüncü isteğe bağlı referans görüntüsü. |

**Not:** Düğüm en fazla üç görüntü kabul edebilir (`image1`, `image2`, `image3`). `image_encoder` ve `vae` girişleri yalnızca en az bir görüntü sağlanmışsa kullanılır. `auto_resize_images` True olduğunda ve bir `vae` bağlıyken, görüntüler kodlamadan önce toplam piksel alanı 1024x1024'e yakın olacak şekilde yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Kodlanmış metin istemini içeren ve görüntü sağlanmışsa kodlanmış görüntü gömme vektörlerini ve/veya referans gizil değişkenlerini içerebilen nihai koşullandırma çıktısı. |

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
