# DA3 Geometrisini Mesh'e Dönüştür

Bu düğüm, bir DA3_GEOMETRY paketini derinlik haritasını izdüşümden çıkararak ve elde edilen nokta bulutunu üçgenleyerek 3 boyutlu bir mesh'e dönüştürür. Bir yığındaki tek bir görüntüyü işler ve 3B işleme için uygun, dokulu veya dokusuz bir mesh üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `da3_geometry` | Derinlik haritası, isteğe bağlı güven haritası, isteğe bağlı gökyüzü haritası ve kaynak görüntü içeren DA3_GEOMETRY paketi | DA3_GEOMETRY | Evet | - |
| `batch_index` | Bir yığındaki hangi görüntünün dönüştürüleceği. Görüntü başına köşe sayıları farklılık gösterdiğinden yığınlar üst üste eklenemez (varsayılan: 0) | INT | Evet | 0 ile 4096 |
| `decimation` | Köşe adımı. 1 = tam çözünürlük, 2 = yarı çözünürlük, vb. (varsayılan: 1) | INT | Evet | 1 ile 8 |
| `discontinuity_threshold` | 3x3 derinlik aralığı bu oranı aşan üçgenleri at. 0 = kapalı (varsayılan: 0.04) | FLOAT | Evet | 0.0 ile 1.0 |
| `confidence_threshold` | Görüntü başına normalleştirilmiş güven değeri bu değerin altında olan pikselleri hariç tut. 0 = tümünü tut, 1 = yalnızca en yüksek güvenli tek pikseli tut. Geometrinin güven haritası olduğunda kullanılır (Küçük/Temel modeller) (varsayılan: 0.1) | FLOAT | Evet | 0.0 ile 1.0 |
| `use_sky_mask` | Gökyüzü olasılığı olan pikselleri (gökyüzü >= 0.5) mesh'ten hariç tut. Geometrinin gökyüzü haritası olduğunda kullanılır (Tek/Metrik modeller) (varsayılan: True) | BOOLEAN | Evet | True veya False |
| `texture` | Kaynak görüntüyü temel renk dokusu olarak kullan (varsayılan: True) | BOOLEAN | Evet | True veya False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MESH` | Köşeler, yüzeyler, UV koordinatları ve isteğe bağlı doku içeren üçgenlenmiş 3B mesh | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
