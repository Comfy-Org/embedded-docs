# MoGe Çıkarımı

Run MoGe'yi tek bir görüntü üzerinde çalıştırarak derinlik ve geometri tahmini yapın. Bu düğüm, bir girdi görüntüsünü MoGe modelinden geçirerek bir 3B nokta bulutu, derinlik haritası, kamera iç parametreleri, bir maske ve yüzey normalleri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet | N/A |
| `image` | Derinlik ve geometri tahmini için girdi görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır. | IMAGE | Evet | N/A |
| `resolution_level` | İşleme çözünürlüğünü kontrol eder. 0 en hızlıdır, 9 en fazla ayrıntıyı sağlar. (varsayılan: 9) | INT | Evet | 0 ile 9 |
| `fov_x_degrees` | (Gelişmiş) Kaynak kameranın derece cinsinden yatay görüş alanı. Derinlik haritasını 3B uzaya geri yansıtmak için kullanılan odak uzaklığını belirler. Görüş alanını tahmin edilen noktalardan otomatik olarak elde etmek için 0.0 olarak ayarlayın. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 170.0 |
| `batch_size` | Çıkarım çağrısı başına görüntü sayısı. Uzun bir video veya geniş bir görüntü kümesinde bellek tükenirse bu değeri düşürün. (varsayılan: 4) | INT | Evet | 1 ile 64 |
| `force_projection` | (Gelişmiş) Tahmin edilen noktaların izdüşümünü zorlar. (varsayılan: True) | BOOLEAN | Evet | True/False |
| `apply_mask` | (Gelişmiş) Maskelenmiş (gökyüzü veya geçersiz) pikselleri, nokta ve derinlik çıktılarında sonsuza ayarlar; böylece örgüleme araçları bunları yok sayabilir. Devre dışı bırakıldığında, ham tahmin edilen geometri her yerde korunur; maske yine de ayrı olarak döndürülür. (varsayılan: True) | BOOLEAN | Evet | True/False |

Not: Girdi `image` öğesi `batch_size` değerinden daha fazla kare içerdiğinde, düğüm bunları birden çok çıkarım çağrısında işler ve sonuçları tek bir çıktı geometrisinde birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük. Orijinal `image` öğesini içerir; ayrıca `points` (3B nokta bulutu), `depth` (derinlik haritası), `intrinsics` (kamera iç parametre matrisi), `mask` (geçerli pikselleri tanımlayan maske) ve `normal` (yüzey normalleri) öğelerini içerebilir. | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/tr.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
