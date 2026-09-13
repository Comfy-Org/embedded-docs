# MoGe Panorama Çıkarımı

Bu düğüm, equirectangular panorama görüntüleri üzerinde derinlik tahmini gerçekleştirir. Panoramayı 12 perspektif görünüme böler, her görünüm üzerinde MoGe derinlik tahmin modelini çalıştırır ve görünüm başına sonuçları tüm panoramayı kapsayan tek bir derinlik haritasında birleştirir. Görünüm başına tahmin edilen normaller ve metrik ölçek yok sayılır, çünkü görünüm başına ölçekler örtüşme dikişleri boyunca hizalanmaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet |  |
| `image` | Equirectangular panorama (her en-boy oranı). Düğüm yalnızca tek bir görüntü kabul eder; bir görüntü grubu geçirilmesi hata verir. Yalnızca ilk 3 renk kanalı (RGB) kullanılır. | IMAGE | Evet |  |
| `resolution_level` | Görünüm başına ayrıntı (0 = en hızlı, 9 = en ayrıntılı) (varsayılan: 9). | INT | Evet | 0 ile 9 |
| `split_resolution` | Her perspektif bölünmesinin çözünürlüğü (varsayılan: 512). | INT | Evet | 256 ile 1024 |
| `merge_resolution` | Birleştirilmiş equirect mesafe haritasının uzun kenar çözünürlüğü (varsayılan: 1920). | INT | Evet | 256 ile 8192 |
| `batch_size` | Çıkarım grubu başına görünüm sayısı (toplam 12 bölünme) (varsayılan: 4). | INT | Evet | 1 ile 12 |

**Notlar:**

- Girdi tek bir görüntü olmalıdır. Eğer `image` grubunda birden fazla görüntü varsa, düğüm hata verir.
- `merge_resolution` maksimum uzun kenar boyutu olarak ele alınır. Panorama bu değerden küçükse, birleştirilmiş harita büyütülmek yerine orijinal panorama boyutunda üretilir. Birleştirilmiş sonuç döndürülmeden önce orijinal panorama çözünürlüğüne yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük: `points` (3B nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (girdi görüntüsü). | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
