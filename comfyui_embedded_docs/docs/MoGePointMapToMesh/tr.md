# MoGe Nokta Haritasından Mesh'e

Bu düğüm, bir MoGe nokta haritasını 3B mesh'e dönüştürür. Bir MoGe derinlik tahmini düğümü tarafından üretilen geometri verisini alır ve onu UV koordinatlarına ve isteğe bağlı bir dokuya sahip bir mesh'e üçgenleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Nokta haritalarını, derinliği ve isteğe bağlı olarak kaynak görüntüyü içeren MoGe geometri verisi. | MOGE_GEOMETRY | Evet | N/A |
| `batch_index` | Toplu MoGe geometrisinin hangi görüntüsünün mesh'e dönüştürüleceği. Görüntü başına vertex sayıları farklı olduğundan, toplu veriler tek bir MESH'te yığılamaz (varsayılan: 0). | INT | Evet | 0 ile 4096 |
| `decimation` | Vertex adımı; 1 = tam çözünürlük (varsayılan: 1). | INT | Evet | 1 ile 8 |
| `discontinuity_threshold` | 3x3 derinlik aralığı bu oranı aşan pikselleri dışla. 0 = kapalı (varsayılan: 0.04). | FLOAT | Evet | 0.0 ile 1.0 |
| `texture` | Kaynak görüntüyü baseColor dokusu olarak taşı (varsayılan: True). | BOOLEAN | Evet | True/False |

Not: `batch_index`, giriş `moge_geometry` toplu boyutundan küçük olmalıdır; aralık dışında bir dizin seçmek hata oluşturur. Giriş bir points çıktısı içermelidir, aksi halde düğüm hata verir. Üçgenleştirme boş bir mesh üretirse, düğüm hata verir — `discontinuity_threshold` değerini 0 yapmak derinlik süreksizliği filtresini devre dışı bırakır. Çıktı mesh'i glTF koordinatlarına dönüştürülür: perspektif MoGe verisi (X sağa, Y aşağı, Z ileri) glTF ile eşleşmesi için ters çevrilir (Y yukarı, Z geri) ve panoramik veri (içsel parametreleri olmayan geometri) düzeltilmiş sarma yönüyle buna göre döndürülür. `texture` etkinleştirildiğinde, `moge_geometry` içindeki kaynak görüntü baseColor dokusu olarak kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MESH` | Vertex'ler, yüzler, UV koordinatları ve kaynak görüntüden isteğe bağlı bir baseColor dokusu içeren 3B mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
