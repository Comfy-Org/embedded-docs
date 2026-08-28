# MoGe Panorama Çıkarımı

## Genel Bakış

Bu düğüm, ekvirektangular panoramik görüntüler üzerinde derinlik tahmini gerçekleştirir. Panaromayı 12 perspektif görünüme böler, her görünümde MoGe derinlik tahmin modelini çalıştırır ve görünüm bazlı sonuçları tüm panoramayı kapsayan tek bir derinlik haritasında birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet |  |
| `image` | Ekvirektangular panorama (herhangi bir en-boy oranı). Düğüm yalnızca tek bir görüntü kabul eder; bir görüntü grubu (batch) iletilmesi hata verir. Yalnızca ilk 3 renk kanalı (RGB) kullanılır. | IMAGE | Evet |  |
| `resolution_level` | Görünüm başına ayrıntı düzeyi (0 = en hızlı, 9 = en ayrıntılı) (varsayılan: 9). | INT | Evet | 0 ile 9 |
| `split_resolution` | Her perspektif parçasının çözünürlüğü (varsayılan: 512). | INT | Evet | 256 ile 1024 |
| `merge_resolution` | Birleştirilmiş ekvirektangular uzaklık haritasının uzun kenar çözünürlüğü (varsayılan: 1920). | INT | Evet | 256 ile 8192 |
| `batch_size` | Çıkarım grubu başına görünüm sayısı (toplam 12 parça) (varsayılan: 4). | INT | Evet | 1 ile 12 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük: `points` (3B nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (girdi görüntüsü). | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
