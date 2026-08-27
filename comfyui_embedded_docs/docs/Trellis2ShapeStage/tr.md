# Trellis2ShapeStage

Bu düğüm, Trellis2 hattının ilk şekil oluşturma örnekleme geçişini kurar. VaeDecodeStructureTrellis2 tarafından üretilen yoğun yapı voxelini alır, doldurulmuş voxellerin seyrek koordinatlarını çıkarır, boş bir seyrek latent oluşturur ve örnekleme sırasında modelin okuyabilmesi için örnekleme meta verilerini koşullandırmaya ekler. Yükseltmeden sonraki ikinci şekil geçişi için bunun yerine, kademeyi ve ikinci geçiş aşaması kurulumunu birleştiren Trellis2UpsampleStage kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Şekil aşaması için hazırlanacak pozitif koşullandırma. Standart bir Trellis2 koşullandırması veya bir projeksiyon özellik paketi sağlayan bir Pixal3D koşullandırması olabilir; projeksiyon özellikleri mevcut olduğunda, seçilen aşama için hesaplanır ve çıktı koşullandırmasına eklenir. | CONDITIONING | Evet | Herhangi bir Trellis2 veya Pixal3D koşullandırması |
| `negative` | Şekil aşaması için hazırlanacak negatif koşullandırma. Aynı şekil aşaması meta verileri, pozitif koşullandırmaya eklendiği gibi buna da eklenir. | CONDITIONING | Evet | Herhangi bir Trellis2 veya Pixal3D koşullandırması |
| `voxel` | VaeDecodeStructureTrellis2'den gelen yoğun yapı voxeli. | VOXEL | Evet | Herhangi bir voxel ızgarası; ızgara çözünürlüğü (eksen başına voxel) hat aşamasını seçer |

### Notlar

- Voxel ızgarası çözünürlüğü hat aşamasını seçer: 32 veya daha düşük bir çözünürlük, `shape_512` aşamasıyla `shape_generation_512` modunu kullanır; 32'den büyük bir çözünürlük ise `shape_1024` aşamasıyla `shape_generation` modunu kullanır.
- Voxel en az bir doldurulmuş voxel içermelidir; boş bir voxel hata verir. Voxelden türetilen batch indeksleri negatif olmayan ve bitişik olmalıdır.
- `positive` koşullandırması bir `proj_feat_pack` içerdiğinde (Pixal3D koşullandırması tarafından sağlandığı gibi), projeksiyon özellikleri seçilen aşama için hesaplanır ve çıktı latentinin model çerçevesi `y_up` olarak ayarlanır. Aksi takdirde, hiçbir projeksiyon özelliği eklenmez ve model çerçevesi `z_up` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Şekil aşaması meta verileri eklenmiş pozitif koşullandırma: oluşturma modu, seyrek koordinatlar, batch başına koordinat sayıları ve kaynak koşullandırma sağladığında projeksiyon özellikleri. | CONDITIONING |
| `negative` | Aynı şekil aşaması meta verileri eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Çıkarılan seyrek koordinatlar, batch başına koordinat sayıları, koordinat çözünürlüğü, `trellis2` tür işareti ve model çerçevesi yönü ile birlikte boş bir seyrek latent tensörü (şekil: batch boyutu, 32, token sayısı, 1). | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/tr.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
