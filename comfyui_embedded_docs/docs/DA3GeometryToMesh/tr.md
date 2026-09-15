# DA3 Geometrisini Mesh'e Dönüştür

Bu düğüm, derinlik haritasının ters projeksiyonunu alarak ve elde edilen nokta bulutunu üçgenleştirerek bir DA3_GEOMETRY paketini 3B mesh'e dönüştürür. Bir toplu işteki tek bir görüntüyü işler ve 3B işleme için uygun, dokulu veya dokusuz bir mesh üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | Derinlik haritası, isteğe bağlı güven haritası, isteğe bağlı gökyüzü haritası ve kaynak görüntüyü içeren DA3_GEOMETRY paketi | DA3_GEOMETRY | Evet | - |
| `batch_index` | Bir toplu işin hangi görüntüsünün dönüştürüleceği. Görüntü başına tepe noktası sayıları farklı olduğundan toplu işler üst üste yığılamaz (varsayılan: 0). Girdi geometrisinin toplu iş boyutundan küçük olmalıdır; aksi takdirde hata verilir | INT | Evet | 0 ile 4096 |
| `decimation` | Tepe noktası adımı. 1 = tam çözünürlük, 2 = yarı, vb. (varsayılan: 1) | INT | Evet | 1 ile 8 |
| `discontinuity_threshold` | 3x3 derinlik açıklığı bu oranı aşan üçgenleri at. 0 = kapalı (varsayılan: 0.04) | FLOAT | Evet | 0.0 ile 1.0 |
| `confidence_threshold` | Görüntü başına normalleştirilmiş güveni bu değerin altında olan pikselleri hariç tut. 0 = tümünü koru, 1 = yalnızca en güvenilir tek pikseli koru. Geometride bir güven haritası olduğunda kullanılır (Small/Base modelleri) (varsayılan: 0.1) | FLOAT | Evet | 0.0 ile 1.0 |
| `use_sky_mask` | Gökyüzü olasılığı olan pikselleri (sky >= 0.5) mesh'ten hariç tut. Geometride bir gökyüzü haritası olduğunda kullanılır (Mono/Metric modelleri) (varsayılan: True) | BOOLEAN | Evet | True or False |
| `texture` | Kaynak görüntüyü temel renk dokusu olarak kullan (varsayılan: True) | BOOLEAN | Evet | True or False |

Sonlu olmayan, sıfır veya negatif derinlik değerine sahip pikseller her zaman mesh'ten hariç tutulur. Elde edilen mesh boşsa hata verilir; hata mesajı `discontinuity_threshold` değerini yükseltmeyi, `confidence_threshold` değerini düşürmeyi veya `use_sky_mask` seçeneğini devre dışı bırakmayı önerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MESH` | Tepe noktaları, yüzler, UV koordinatları ve isteğe bağlı doku içeren üçgenlenmiş bir 3B mesh | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
