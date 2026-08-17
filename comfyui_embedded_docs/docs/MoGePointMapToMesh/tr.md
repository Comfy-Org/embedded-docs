# MoGe Nokta Haritasından Mesh'e

Bu düğüm, bir MoGe nokta haritasını 3B bir ağa dönüştürür. Bir MoGe derinlik tahmin düğümü tarafından üretilen geometri verilerini alır ve bir görüntüyü UV koordinatlarına ve isteğe bağlı bir dokuya sahip bir ağ olarak üçgenler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Nokta haritaları, derinlik ve isteğe bağlı olarak kaynak görüntüyü içeren MoGe geometri verileri. | MOGE_GEOMETRY | Evet | N/A |
| `batch_index` | Bir yığın MoGe geometrisinin hangi görüntüsünün ağ haline getirileceği. Görüntü başına köşe sayıları farklı olduğundan, yığınlar tek bir MESH içinde istiflenemez (varsayılan: 0). | INT | Evet | 0 ile 4096 |
| `decimation` | Köşe adımı; 1 = tam çözünürlük (varsayılan: 1). | INT | Evet | 1 ile 8 |
| `discontinuity_threshold` | 3x3 derinlik aralığı bu oranı aşan pikselleri at. 0 = kapalı (varsayılan: 0.04). | FLOAT | Evet | 0.0 ile 1.0 |
| `texture` | Kaynak görüntüyü baseColor dokusu olarak taşı (varsayılan: True). | BOOLEAN | Evet | True/False |

Not: `batch_index`, sağlanan `moge_geometry` kümesinin yığın boyutundan küçük olmalıdır. Girdi geometrisi nokta verisi içermelidir ve oluşturulan ağ boşsa, düğüm `discontinuity_threshold = 0` öneren bir hata döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MESH` | Kaynak görüntüden köşeler, yüzler, UV koordinatları ve isteğe bağlı bir doku içeren bir 3B ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
