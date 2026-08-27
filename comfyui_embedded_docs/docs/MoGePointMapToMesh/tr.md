# MoGe Nokta Haritasından Mesh'e

Bu düğüm, bir MoGe nokta haritasını 3B bir ağa (mesh) dönüştürür. Bir MoGe derinlik tahmin düğümü tarafından üretilen geometri verilerini alır ve bunları UV koordinatları ve isteğe bağlı bir doku ile bir ağa üçgenler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Nokta haritaları, derinlik ve isteğe bağlı olarak kaynak görüntüyü içeren MoGe geometri verileri. | MOGE_GEOMETRY | Evet | Yok |
| `batch_index` | Bir MoGe geometri kümesindeki (batch) hangi görüntünün ağa dönüştürüleceğini belirtir. Görüntü başına köşe sayıları farklı olduğundan, kümeler tek bir MESH içinde birleştirilemez (varsayılan: 0). | INT | Evet | 0 ila 4096 |
| `decimation` | Köşe adımı; 1 = tam çözünürlük (varsayılan: 1). | INT | Evet | 1 ila 8 |
| `discontinuity_threshold` | 3x3 derinlik aralığı bu oranı aşan pikselleri atar. 0 = kapalı (varsayılan: 0,04). | FLOAT | Evet | 0,0 ila 1,0 |
| `texture` | Kaynak görüntüyü baseColor dokusu olarak taşır (varsayılan: True). | BOOLEAN | Evet | True/False |

Not: `batch_index`, girdi `moge_geometry` kümesinin boyutundan küçük olmalıdır; aralık dışı bir dizin seçilmesi hata oluşturur. Eğer üçgenleme boş bir ağ üretirse, düğüm bir hata verir — `discontinuity_threshold` değerini 0 yapmak derinlik süreksizliği filtresini devre dışı bırakır. Çıktı ağı glTF koordinatlarına dönüştürülür: perspektif MoGe verileri (X sağ, Y aşağı, Z ileri) glTF ile eşleşecek şekilde çevrilir (Y yukarı, Z geri) ve panoramik veriler buna göre döndürülür. `texture` etkinleştirildiğinde, `moge_geometry` içindeki kaynak görüntü baseColor dokusu olarak kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MESH` | Köşeler, yüzeyler, UV koordinatları ve kaynak görüntüden isteğe bağlı bir baseColor dokusu içeren 3B bir ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
