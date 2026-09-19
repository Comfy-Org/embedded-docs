# Tripo P2: Çoklu Görünümden Modele

Tripo'nun P2 modelini kullanarak aynı öznenin birkaç görünümünden temiz topolojili düşük poligonlu bir 3D model oluşturur. Ön görünüm zorunludur ve sonucu iyileştirmek için sol, arka ve sağ görünümlerden bir ila üçü eklenebilir. Model, bir üçgen ağ (GLB) olarak veya `model.quad` etkinleştirildiğinde dörtgen ağırlıklı bir ağ (FBX) olarak döner.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Tripo P serisi model. Bir model seçmek, aşağıda kendi girdilerini gösterir. | DYNAMIC_COMBO | Evet | `"P2"` |

### P2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.image` | Öznenin ön görünümü (0°). | IMAGE | Evet | - |
| `model.image_left` | Sol görünüm (90°), öznenin kendi sol tarafı. | IMAGE | Hayır | - |
| `model.image_back` | Arka görünüm (180°). | IMAGE | Hayır | - |
| `model.image_right` | Sağ görünüm (270°), öznenin kendi sağ tarafı. | IMAGE | Hayır | - |
| `quad` | GLB çıktısındaki üçgen ağ yerine FBX çıktısında dörtgen ağırlıklı bir ağ döndürür (varsayılan: False). | BOOLEAN | Evet | True/False |
| `face_limit` | Hedef yüz sayısı. `-1` Tripo'nun seçmesine izin verir. `model.quad` etkinleştirildiğinde sınır 48 ile 25.000 arası, aksi takdirde 48 ile 50.000 arasıdır (varsayılan: -1). | INT | Evet | -1 veya 48 - 50000 |
| `texture` | Temel renk doku çözünürlüğü: standard 2K, detailed 4K ve extreme 8K'dır. `"none"` dokusuz bir ağ döndürür (varsayılan: `"standard"`). | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Temel renge metalik, pürüzlülük ve normal haritaları ekler. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: True). | BOOLEAN | Evet | True/False |
| `model_seed` | Geometri için tohum (varsayılan: 42). | INT | Evet | 0 - 2147483647 |
| `texture_alignment` | Girdi görüntülerinin renklerini eşleştirir veya dokuları oluşturulan geometriye uydurur. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: `"original_image"`). Gelişmiş ayar. | COMBO | Evet | `"original_image"`<br>`"geometry"` |
| `orientation` | `"align_image"` modeli girdi görüntülerinin bakış açısına döndürür. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: `"default"`). Gelişmiş ayar. | COMBO | Evet | `"default"`<br>`"align_image"` |
| `texture_seed` | Dokular için tohum (varsayılan: 42). Gelişmiş ayar. | INT | Evet | 0 - 2147483647 |
| `auto_size` | Modeli sahne dönüşümü aracılığıyla metre cinsinden gerçek dünya boyutuna ölçekler. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `export_uv` | Ağ dokusuz olduğunda UV açılımını uygular. Dokulu ağlar her zaman açılır (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `compress_geometry` | Meshopt geometri sıkıştırması uygular: çok daha küçük dosyalar, ancak ComfyUI'nin 3D önizlemesi bunları görüntüleyemez. Dörtgen ağlar için yok sayılır (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |

**Notlar:**

- `model.image` gereklidir ve ayrıca `model.image_left`, `model.image_back` veya `model.image_right` girdilerinden en az biri bağlanmalıdır; ön görünüm tek görüntüyse düğüm hata verir.
- Her partideki yalnızca ilk görüntü kullanılır.
- `model.face_limit` kesin bir üst sınır değil, bir hedeftir; bu nedenle sonuç istenenden daha fazla yüz içerebilir. `-1` seçimi Tripo'ya bırakır.
- `model.quad`, ağı hangi çıktının taşıyacağını belirler. Etkinleştirildiğinde model FBX çıktısına gelir ve GLB çıktısı boş kalır; devre dışı bırakıldığında model GLB çıktısına gelir ve FBX boş kalır. Boş çıktı, bağladığınız çıktıysa düğüm hata verir.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` ve `model.orientation` yalnızca dokulu modeller için geçerlidir: `"none"` olduğunda düğüm hiçbir doku ayarı göndermez ve çıplak geometri döndürür.
- `model.compress_geometry` dörtgen ağlar üzerinde etkili değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model task_id` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | Oluşturulan 3D modelin GLB biçimi. `model.quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | Oluşturulan 3D modelin FBX biçimi. Yalnızca `model.quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
