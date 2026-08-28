# WanİlkSonKaredenVideoya

WanFirstLastFrameToVideo düğümü, bir başlangıç karesini ve bir bitiş karesini metin istemleriyle birleştirerek video üretimi için koşullandırma hazırlar. Kare görüntülerini latent uzaya kodlar, video modeline hangi karelerin zaten bilindiğini söyleyen bir maske oluşturur ve sağlandığında CLIP vision özelliklerini ekler. Düğüm, güncellenmiş pozitif ve negatif koşullandırma ile birlikte, üretilecek videonun boyutunu ve uzunluğunu tanımlayan boş bir latent çıktı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimini yönlendirmek için kullanılan pozitif metin koşullandırması. | CONDITIONING | Evet | - |
| `negatif` | Video üretimini yönlendirmek için kullanılan negatif metin koşullandırması. | CONDITIONING | Evet | - |
| `vae` | Birleştirilmiş kare görüntülerini latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Üretilen videonun piksel cinsinden genişliği (varsayılan: 832, adım: 16). | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Üretilen videonun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16). | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4). | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda üretilecek video sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 |
| `clip_görü_başlangıç_görüntüsü` | Başlangıç görüntüsünden çıkarılan CLIP vision özellikleri. Hem başlangıç hem bitiş CLIP vision girdileri sağlanırsa, özellikler birleştirilir. | CLIP_VISION_OUTPUT | Hayır | - |
| `clip_görü_bitiş_görüntüsü` | Bitiş görüntüsünden çıkarılan CLIP vision özellikleri. Hem başlangıç hem bitiş CLIP vision girdileri sağlanırsa, özellikler birleştirilir. | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video dizisi için başlangıç karesi görüntüsü. İlk `length` karesi kullanılır ve `width` × `height` boyutuna yeniden boyutlandırılır. | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video dizisi için bitiş karesi görüntüsü. Son `length` karesi kullanılır ve `width` × `height` boyutuna yeniden boyutlandırılır. | IMAGE | Hayır | - |

**Not:** `start_image` veya `end_image` girdilerinden en az biri sağlandığında, düğüm başlangıç ve bitiş karelerinin doldurulduğu ve kalan karelerin nötr gri bir yer tutucu (0.5) kullandığı birleşik bir kare dizisi oluşturur. Bir maske, doldurulan bölgeleri bilinen, yer tutucu bölgeleri ise bilinmeyen olarak işaretler ve video modelinin aradaki kareleri üretmesine olanak tanır. Bir başlangıç görüntüsü sağlandığında, bilinen bölge ayrıca görüntünün ötesine 3 ekstra kare daha uzanır. Aynı kodlanmış kare görüntüsü ve maske hem `positive` hem de `negative` koşullandırmasına eklenir. Her iki CLIP vision girdisi de sağlanırsa, gizli durumları birleştirilir; yalnızca biri sağlanırsa, tek başına kullanılır. Latent video uzunluğu, zamansal sıkıştırma sonrasında `length` değerinden türetilir: `((length - 1) // 4) + 1`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Kodlanmış kare görüntüsü, maske ve (sağlanmışsa) CLIP vision özellikleri eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | Kodlanmış kare görüntüsü, maske ve (sağlanmışsa) CLIP vision özellikleri eklenmiş negatif koşullandırma. | CONDITIONING |
| `gizli` | Belirtilen parti boyutu, video uzunluğu ve çözünürlük için şekillendirilmiş boş latent tensör (tümü sıfır). | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
