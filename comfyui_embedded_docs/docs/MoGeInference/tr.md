# MoGe Çıkarımı

Tek bir görüntüde MoGe çalıştırarak derinlik ve geometri tahmini yapın. Bu düğüm, girdi görüntüsünü MoGe modeli aracılığıyla işleyerek bir 3B nokta bulutu, derinlik haritası, kamera iç parametreleri, bir maske ve yüzey normalleri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet | N/A |
| `image` | Derinlik ve geometri tahmini için girdi görüntüsü. Yalnızca RGB kanalları kullanılır; alfa kanalı yok sayılır. | IMAGE | Evet | N/A |
| `resolution_level` | İşleme çözünürlüğünü kontrol eder. 0 en hızlı, 9 en ayrıntılı sonucu sağlar. (varsayılan: 9) | INT | Evet | 0 to 9 |
| `fov_x_degrees` | (Gelişmiş) Kaynak kameranın yatay görüş alanı (derece cinsinden). Derinlik haritasını 3B'ye izdüşürmek için kullanılan odak uzaklığını belirler. Tahmin edilen noktalardan görüş alanını otomatik olarak kurtarmak için 0.0 olarak ayarlayın. (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 170.0 |
| `batch_size` | Her çıkarım çağrısında işlenen görüntü sayısı. Uzun videoları veya büyük görüntü kümelerini işlerken bellek yetersizliği yaşarsanız bu değeri düşürün. (varsayılan: 4) | INT | Evet | 1 to 64 |
| `force_projection` | (Gelişmiş) Tahmin edilen noktaların izdüşümünü zorlar. (varsayılan: True) | BOOLEAN | Evet | True/False |
| `apply_mask` | (Gelişmiş) Etkinleştirildiğinde, maskelenmiş (gökyüzü veya geçersiz) pikselleri nokta ve derinlik çıktılarında sonsuza ayarlar. Bu, mesh oluşturma araçlarının bu alanları yok saymasına yardımcı olur. Kapatıldığında ham tahmin edilen geometri her yerde korunur; maske yine de ayrı olarak döndürülür. (varsayılan: True) | BOOLEAN | Evet | True/False |

Not: `image` girdisi birden çok görüntü içerebilir. Düğüm bunları `batch_size` grupları halinde işler ve sonuçları tek bir çıktıda birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük. Her zaman girdi `image` görüntüsünü (yalnızca RGB kanalları) içerir ve `points` (3B nokta bulutu), `depth` (derinlik haritası), `intrinsics` (kamera iç parametre matrisi), `mask` (geçerli pikselleri tanımlayan maske) ve `normal` (yüzey normalleri) alanlarını içerebilir. | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/tr.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
