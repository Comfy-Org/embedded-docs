# TextEncodeZImageOmni

TextEncodeZImageOmni, bir metin istemini en fazla üç isteğe bağlı referans görüntüyle birlikte görüntü üretim modelleri için bir koşullandırma formatına kodlar. İstem, CLIP modeliyle tokenize edilir ve kodlanır; bağlanan her görüntü isteğe bağlı olarak bir görüntü kodlayıcı ve/veya VAE tarafından işlenebilir, böylece görsel referanslar metnin yanına gömülür. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin istemini tokenize etmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet |  |
| `görüntü_kodlayıcı` | İsteğe bağlı bir görüntü kodlayıcı modeli. Sağlanırsa, giriş görüntülerini kodlamak için kullanılır ve elde edilen gömme vektörleri koşullandırmaya eklenir. | CLIP_VISION | Hayır |  |
| `istem` | Kodlanacak metin istemi. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet |  |
| `görüntüleri_otomatik_yeniden_boyutlandır` | Etkinleştirildiğinde (varsayılan: True), giriş görüntüleri VAE kodlamasından önce otomatik olarak yeniden boyutlandırılır, böylece toplam piksel alanları 1024x1024'e yakın olur ve boyutlar 8'in katlarına yuvarlanır. | BOOLEAN | Evet | True<br>False |
| `vae` | İsteğe bağlı bir VAE modeli. Sağlanırsa, giriş görüntülerini latent temsillere kodlamak için kullanılır ve bunlar koşullandırmaya referans latentleri olarak eklenir. | VAE | Hayır |  |
| `görüntü1` | Birinci isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |
| `görüntü2` | İkinci isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |
| `görüntü3` | Üçüncü isteğe bağlı referans görüntüsü. | IMAGE | Hayır |  |

**Not:** Düğüm en fazla üç görüntü (`image1`, `image2`, `image3`) kabul eder. `image_encoder` ve `vae` girişleri yalnızca en az bir görüntü sağlandığında kullanılır; her ikisi de bağlandığında, her görüntü ikisi tarafından da işlenir. `auto_resize_images` True olduğunda ve bir `vae` bağlı olduğunda, görüntüler kodlamadan önce toplam piksel alanları 1024x1024'e yakın olacak şekilde yeniden boyutlandırılır. Hiç görüntü sağlanmazsa, yalnızca metin istemi kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Nihai koşullandırma çıktısı. Kodlanmış metin istemini içerir ve görüntüler sağlandığında kodlanmış görüntü gömme vektörlerini, referans latentlerini ve görüntü yer tutucu şablonundan türetilen ek metin gömme vektörlerini içerebilir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/tr.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
