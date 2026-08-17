# MoGe Panorama Çıkarımı

Bu düğüm, equirectangular panorama görüntülerinde derinlik tahmini gerçekleştirir. Panoramayı 12 perspektif görünüme bölerek çalışır, her görünümde MoGe derinlik tahmin modelini çalıştırır ve ardından sonuçları orijinal panorama için tek ve eksiksiz bir derinlik haritasında birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet |  |
| `image` | Equirectangular panorama (herhangi bir en-boy oranı). Yalnızca tek bir görüntü kabul eder. | IMAGE | Evet |  |
| `resolution_level` | Görünüm başına ayrıntı (0 = en hızlı, 9 = en ayrıntılı). Varsayılan: 9. | INT | Evet | 0 - 9 |
| `split_resolution` | Her perspektif bölümünün çözünürlüğü. Varsayılan: 512. | INT | Evet | 256 - 1024 |
| `merge_resolution` | Birleştirilmiş equirect mesafe haritasının uzun kenar çözünürlüğü. Varsayılan: 1920. | INT | Evet | 256 - 8192 |
| `batch_size` | Çıkarım grubu başına görünüm sayısı (toplam 12 bölüm). Varsayılan: 4. | INT | Evet | 1 - 12 |

Not: Bu düğüm yalnızca tek bir görüntü kabul eder. Bir grup görüntü iletilmesi hata oluşturur. Panorama her zaman 12 perspektif görünüme bölünür; `batch_size` yalnızca bu görünümlerden kaçının çıkarım grubu başına işleneceğini kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmini geometriyi içeren bir sözlük: `points` (3D nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (girdi görüntüsü). | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
