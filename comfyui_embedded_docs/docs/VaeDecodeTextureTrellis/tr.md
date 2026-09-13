# VaeDecodeTextureTrellis

Bu düğüm, bir Trellis2 doku latentini bir VAE kullanarak voksel renklerine çözer. Girdi latent, koordinatları olan seyrek özellik örnekleri içerir; düğüm her voksel için rengi yeniden oluşturur ve sonucu, PaintMesh gibi aşağı akış düğümlerinin 3B bir ağı renklendirmek için kullanabileceği bir voksel ızgarası olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Çözülecek doku latentini. Örnek özelliklerini ve seyrek koordinatları içerir; ayrıca koordinat sayıları (`coord_counts`), model çerçevesi (`model_frame`, varsayılan: "y_up") ve koordinat çözünürlüğü (`coord_resolution`) gibi isteğe bağlı üst verileri içerebilir. | LATENT | Evet | — |
| `vae` | Doku latentini voksel renklerine çözmek için kullanılan Trellis2 VAE'si. | VAE | Evet | — |
| `shape_subdivides` | Çözme sırasında daha yüksek ayrıntılı yeniden oluşturmayı yönlendirmek için kullanılan şekil bilgisi. Daha yüksek çözünürlüklerde yapı tutarlılığının korunmasına yardımcı olur. | SHAPE_SUBDIVIDES | Evet | — |

Not: `samples` latentinde `coord_counts` varsa, sayılar negatif olmamalı, toplamları koordinat satırlarının sayısıyla eşleşmeli ve her grup tam olarak beklenen satır sayısını içermelidir; aksi halde düğüm bir hata verir. Latentin `model_frame` değeri "z_up" ise, çözülen voksel koordinatları ağ köşeleriyle hizalanmaları için Y-up olarak yeniden eşlenir. `coord_resolution` sağlandığında, çıktı doku çözünürlüğü bu değerin 16 ile çarpımıdır. Aksi halde en büyük voksel koordinatının bir fazlasından tahmin edilir ve 256, 512, 1024, 1536 veya 2048 değerlerinden birine yukarı yuvarlanır; gereken değer 2048'i aşarsa bu daha büyük değer kullanılır. Kullanılabilir koordinat yoksa çözünürlük varsayılan olarak 1024 olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voxel_colors` | Koordinatları, renk özelliklerini ve doku çözünürlüğünü içeren çözülmüş voksel verisi. Her vokselde 6 renk kanalı vardır: temel renk (RGB), metalik, pürüzlülük ve alfa; tümü [0, 1] aralığındadır. PaintMesh gibi köşe rengi tüketicileri ilk 3 kanalı kullanır. | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
