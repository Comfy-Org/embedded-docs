# MoGe Çıkarımı

Derinlik ve geometriyi tahmin etmek için MoGe'yi görüntüler üzerinde çalıştırın. Bu düğüm, bir girdi görüntüsünü MoGe modeli üzerinden işleyerek 3B nokta bulutu, derinlik haritası, kamera iç parametreleri, maske ve yüzey normalleri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet | N/A |
| `image` | Derinlik ve geometri tahmini için girdi görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır. | IMAGE | Evet | N/A |
| `resolution_level` | İşleme çözünürlüğünü kontrol eder. 0 = en hızlı, 9 = en fazla ayrıntı. (varsayılan: 9) | INT | Evet | 0 - 9 |
| `fov_x_degrees` | (Gelişmiş) Kaynak kameranın yatay görüş alanı. Derinlik haritasını 3B uzaya geri izdüşümlemek için kullanılan odak uzaklığını ayarlar. 0 = tahmin edilen noktalardan otomatik olarak geri kazanılır. (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 170.0 (adım 0.1) |
| `batch_size` | Çıkarım çağrısı başına görüntü sayısı. Uzun bir video / görüntü kümesinde OOM hatası alırsanız düşürün. (varsayılan: 4) | INT | Evet | 1 - 64 |
| `force_projection` | (Gelişmiş) Tahmin edilen noktaların izdüşümünü zorlar. (varsayılan: True) | BOOLEAN | Evet | True/False |
| `apply_mask` | (Gelişmiş) Maskelenmiş (gökyüzü / geçersiz) pikselleri, mesh oluşturmanın onları elemesi için noktalar ve derinlikte inf değerine ayarlar. Ham tahmin edilen geometriyi her yerde korumak için devre dışı bırakın; maske yine de ayrı olarak döndürülür. (varsayılan: True) | BOOLEAN | Evet | True/False |
| `refine_steps` | (Gelişmiş) Yalnızca MoGe-3: tahmin edilen derinlik üzerinde seyrek hacimsel iyileştirme geçişleri. Daha fazla geçiş, ince ayrıntıları ve kenarları yaklaşık doğrusal bir maliyetle keskinleştirir. 0, iyileştirmeyi devre dışı bırakır. MoGe-1 / MoGe-2 tarafından yok sayılır. (varsayılan: 3) | INT | Evet | 0 - 8 |

Not: Girdi `image`, `batch_size` değerinden daha fazla kare içerdiğinde, düğüm bunları birden çok çıkarım çağrısında işler ve sonuçları tek bir çıktı geometrisinde birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük. Orijinal `image` öğesini içerir ve `points` (3B nokta bulutu), `depth` (derinlik haritası), `intrinsics` (kamera iç parametre matrisi), `mask` (geçerli pikselleri tanımlayan maske) ve `normal` (yüzey normalleri) öğelerini içerebilir. | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/tr.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
