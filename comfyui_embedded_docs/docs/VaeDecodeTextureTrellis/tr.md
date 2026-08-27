# VaeDecodeTextureTrellis

Bu düğüm, bir VAE kullanarak bir Trellis2 doku latentini voxel renklerine dönüştürür. Girdi latenti, koordinatlarla birlikte seyrek özellik örnekleri içerir; düğüm her voxel için rengi yeniden oluşturur ve sonucu, PaintMesh gibi alt düğümlerin bir 3D ağı renklendirmek için kullanabileceği bir voxel ızgarası olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Çözülecek doku latenti. Örnek özelliklerini ve seyrek koordinatları içerir; koordinat sayıları, model çerçevesi ve koordinat çözünürlüğü gibi isteğe bağlı meta verileri de içerebilir. | LATENT | Evet | — |
| `vae` | Doku latentini voxel renklerine çözmek için kullanılan Trellis2 VAE. | VAE | Evet | — |
| `shape_subdivides` | Çözme sırasında daha yüksek ayrıntılı yeniden yapılandırmayı yönlendirmek için kullanılan şekil bilgisi. Daha yüksek çözünürlüklerde yapı tutarlılığının korunmasına yardımcı olur. | SHAPE_SUBDIVIDES | Evet | — |

Not: `samples` latenti koordinat sayıları içerdiğinde, bu sayılar negatif olmamalıdır, toplamları koordinat satırı sayısına eşit olmalıdır ve her yığın tam olarak beklenen sayıda satıra sahip olmalıdır; aksi takdirde düğüm bir hata verir. Latentin model çerçevesi "z_up" ise, çözülen voxel koordinatları, ağ köşeleriyle hizalanmaları için Y-up olarak yeniden eşlenir. Bir koordinat çözünürlüğü sağlandığında, çıktı doku çözünürlüğü bu değerin 16 ile çarpılmasıdır; aksi takdirde en büyük voxel koordinatından çıkarılır ve 256, 512, 1024, 1536 veya 2048 değerlerinden birine yuvarlanır (koordinat yoksa 1024).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voxel_colors` | Koordinatlar, renk özellikleri ve doku çözünürlüğü içeren çözülmüş voxel verisi. Her voxel 6 renk kanalına sahiptir: temel renk (RGB), metaliklik, pürüzlülük ve alfa; tümü [0, 1] aralığındadır. PaintMesh gibi köşe rengi tüketicileri ilk 3 kanalı kullanır. | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `cfbe59efb18d2c3c7c597c5212900fea54d660aa98005817debf4711401a6967`
