# Trellis2ShapeStage

Bu düğüm, Trellis2 hattının ilk şekil üretimi örnekleme geçişini ayarlar. VaeDecodeStructureTrellis2 tarafından üretilen yoğun yapı voxel'ini alır, doldurulmuş voxel'lerin seyrek koordinatlarını çıkarır, boş bir seyrek latent oluşturur ve örnekleme sırasında modelin okuyabilmesi için örnekleme meta verilerini conditioning'e ekler. Yükseltme sonrası ikinci şekil geçişi için bunun yerine, kademeli (cascade) ve ikinci geçiş aşaması kurulumunu birleştiren Trellis2UpsampleStage kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Şekil aşaması için hazırlanacak pozitif conditioning. Standart bir Trellis2 conditioning veya bir projeksiyon özellik paketi sağlayan bir Pixal3D conditioning olabilir; projeksiyon özellikleri mevcut olduğunda, seçilen aşama için hesaplanır ve çıktı conditioning'ine eklenir. | CONDITIONING | Evet | Any Trellis2 or Pixal3D conditioning |
| `negative` | Şekil aşaması için hazırlanacak negatif conditioning. Aynı şekil aşaması meta verileri, pozitif conditioning'e olduğu gibi buna da eklenir. | CONDITIONING | Evet | Any Trellis2 or Pixal3D conditioning |
| `voxel` | VaeDecodeStructureTrellis2'den gelen yoğun yapı voxel'i. | VOXEL | Evet | Any voxel grid; the grid resolution (voxels per axis) selects the pipeline stage |

### Notlar

- Voxel grid çözünürlüğü hat aşamasını seçer: 32 veya daha düşük bir çözünürlük, `shape_512` aşamasıyla `shape_generation_512` modunu kullanır; 32'den büyük bir çözünürlük ise `shape_1024` aşamasıyla `shape_generation` modunu kullanır.
- Voxel en az bir dolu voxel içermelidir; boş bir voxel hata verir. Voxel'den türetilen batch indeksleri negatif olmamalı ve bitişik olmalıdır.
- `positive` conditioning bir `proj_feat_pack` içerdiğinde (Pixal3D conditioning tarafından sağlandığı gibi), projeksiyon özellikleri seçilen aşama için hesaplanır ve çıktı latent'inin model çerçevesi `y_up` olarak ayarlanır. Aksi takdirde, hiçbir projeksiyon özelliği eklenmez ve model çerçevesi `z_up` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Şekil aşaması meta verileri eklenmiş pozitif conditioning: üretim modu, seyrek koordinatlar, batch başına koordinat sayıları ve kaynak conditioning sağladığında projeksiyon özellikleri. | CONDITIONING |
| `negative` | Aynı şekil aşaması meta verileri eklenmiş negatif conditioning. | CONDITIONING |
| `latent` | Ayıklanan seyrek koordinatlar, batch başına koordinat sayıları, koordinat çözünürlüğü, `trellis2` tür işareti ve model çerçevesi yönelimiyle birlikte boş bir seyrek latent tensörü (şekil: batch size, 32, token count, 1). | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/tr.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
