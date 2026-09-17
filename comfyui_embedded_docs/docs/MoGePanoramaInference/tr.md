# MoGe Panorama Çıkarımı

Bu düğüm, eşdikdörtgen (equirectangular) panorama görüntüleri üzerinde derinlik tahmini gerçekleştirir. Panoramayı 12 perspektif görünüme böler, her görünümde MoGe derinlik tahmini modelini çalıştırır ve görünüm başına sonuçları tam panoramayı kapsayan tek bir derinlik haritasında birleştirir. Görünüm başına tahmin edilen normaller ve metrik ölçek yok sayılır, çünkü görünüm başına ölçekler örtüşme dikişleri boyunca hizalanmaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet |  |
| `image` | Eşdikdörtgen panorama (herhangi bir en-boy oranı). Düğüm yalnızca tek bir görüntü kabul eder; bir görüntü yığını iletilmesi hata verir. Yalnızca ilk 3 renk kanalı (RGB) kullanılır. | IMAGE | Evet |  |
| `resolution_level` | Görünüm başına ayrıntı (0 = en hızlı, 9 = en ayrıntılı) (varsayılan: 9). | INT | Evet | 0 ile 9 arası |
| `split_resolution` | Her perspektif bölünmesinin çözünürlüğü (varsayılan: 512). | INT | Evet | 256 ile 1024 arası |
| `merge_resolution` | Birleştirilmiş eşdikdörtgen (equirectangular) mesafe haritasının uzun kenar çözünürlüğü (varsayılan: 1920). | INT | Evet | 256 ile 8192 arası |
| `batch_size` | Çıkarım yığını başına görünüm sayısı (toplam 12 bölünme) (varsayılan: 4). | INT | Evet | 1 ile 12 arası |
| `refine_steps` | Yalnızca MoGe-3: tahmin edilen derinlik üzerinde seyrek hacimsel iyileştirme geçişleri. Daha fazla geçiş, ince ayrıntıyı ve kenarları yaklaşık doğrusal bir maliyetle keskinleştirir. 0, iyileştirmeyi devre dışı bırakır. MoGe-1 / MoGe-2 tarafından yok sayılır (varsayılan: 3). | INT | Evet | 0 ile 8 arası |

**Notlar:**

- Girdi tek bir görüntü olmalıdır. Eğer `image` yığınında birden fazla görüntü varsa, düğüm hata verir.
- `merge_resolution` maksimum uzun kenar boyutu olarak ele alınır. Panorama bu değerden küçükse, birleştirilmiş harita büyütülmek yerine orijinal panorama boyutunda üretilir. Birleştirilmiş sonuç döndürülmeden önce orijinal panorama çözünürlüğüne yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük: `points` (3B nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (girdi görüntüsü). | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

---
**Source fingerprint (SHA-256):** `7f21452d035b2fe9d30b0cd15ddad10916439492b1d682a8b28f1a79e375df58`
