# DA3 Geometrisini Nokta Bulutuna Dönüştür

Bu düğüm, bir DA3_GEOMETRY nesnesinden alınan derinlik haritasını 3B nokta bulutuna dönüştürür. Güven ve gökyüzü maskelerine dayalı filtreleme uygular ve noktaları çoklu görünüm senaryolarına uygun ortak bir dünya koordinat sistemine dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `da3_geometry` | Derinlik verileri ve isteğe bağlı görüntü, güven ve gökyüzü haritalarını içeren DA3_GEOMETRY nesnesi | DA3_GEOMETRY | Evet | - |
| `batch_index` | Dönüştürülecek toplu işteki görüntü indeksi (varsayılan: 0) | INT | Evet | 0 ile 4096 |
| `confidence_threshold` | Görüntü başına normalleştirilmiş güven değeri bu değerin altında olan pikselleri hariç tut (0 = tümünü tut). Geometride güven haritası olduğunda kullanılır (Küçük/Temel modeller). (varsayılan: 0.1) | FLOAT | Evet | 0.0 ile 1.0 |
| `use_sky_mask` | Gökyüzü olasılığı olan pikselleri hariç tut (gökyüzü >= 0.5). Geometride gökyüzü haritası olduğunda kullanılır (Tek/Metrik modeller). (varsayılan: True) | BOOLEAN | Evet | True veya False |
| `downsample` | Her N. pikseli al (1 = tam çözünürlük). Daha yüksek değerler daha az nokta ve daha hızlı işleme sağlar. (varsayılan: 1) | INT | Evet | 1 ile 16 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `point_cloud` | Filtrelenmiş 3B noktalar, isteğe bağlı renkler ve isteğe bağlı güven değerleri içeren nokta bulutu nesnesi | DA3_POINT_CLOUD |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
