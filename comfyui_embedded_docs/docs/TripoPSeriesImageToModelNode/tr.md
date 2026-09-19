# Tripo P2: Görüntüden Modele

Tripo'nun P2 modelini kullanarak tek bir görüntüden temiz topolojili düşük poligonlu bir 3B model oluşturur. Sonuç, bir üçgen ağ (GLB) olarak veya `model.quad` etkinleştirildiğinde dörtgen ağırlıklı bir ağ (FBX) olarak döner.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Tripo P serisi modeli. Bir model seçmek, aşağıda kendi girdilerini gösterir. | DYNAMIC_COMBO | Evet | `"P2"` |

### P2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.image` | Modelin oluşturulduğu görüntü. | IMAGE | Evet | - |
| `quad` | GLB çıktısındaki üçgen ağ yerine FBX çıktısında dörtgen ağırlıklı bir ağ döndürür (varsayılan: False). | BOOLEAN | Evet | True/False |
| `face_limit` | Hedef yüz sayısı. `-1`, seçimi Tripo'ya bırakır. `model.quad` etkinleştirildiğinde sınır 48 ile 25.000 arası, aksi halde 48 ile 50.000 arasıdır (varsayılan: -1). | INT | Evet | -1 veya 48 ile 50000 arası |
| `texture` | Temel renk doku çözünürlüğü: standart 2K, ayrıntılı 4K ve ekstrem 8K'dır. `"none"` dokusuz bir ağ döndürür (varsayılan: `"standard"`). | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Temel renge metalik, pürüzlülük ve normal haritaları ekler. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: True). | BOOLEAN | Evet | True/False |
| `model_seed` | Geometri için rastgelelik tohumu (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `texture_alignment` | Girdi görüntüsünün renklerini eşleştirir veya dokuları oluşturulan geometriye uydurur. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: `"original_image"`). Gelişmiş ayar. | COMBO | Evet | `"original_image"`<br>`"geometry"` |
| `orientation` | `"align_image"`, modeli girdi görüntüsünün bakış açısına döndürür. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: `"default"`). Gelişmiş ayar. | COMBO | Evet | `"default"`<br>`"align_image"` |
| `enable_image_autofix` | Tripo'nun modellemeden önce düşük çözünürlüklü veya düşük kaliteli bir görüntüyü geliştirmesine izin verir (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `texture_seed` | Dokular için rastgelelik tohumu (varsayılan: 42). Gelişmiş ayar. | INT | Evet | 0 ile 2147483647 arası |
| `auto_size` | Modeli sahne dönüşümü aracılığıyla metre cinsinden gerçek dünya boyutuna ölçekler (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `export_uv` | Ağ dokusuz olduğunda UV açılımı uygular. Dokulu ağlara her zaman UV açılımı uygulanır (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `compress_geometry` | meshopt geometri sıkıştırmasını uygular: çok daha küçük dosyalar, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez. Dörtgen ağlar için yok sayılır (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |

**Notlar:**

- `model.image` gereklidir ve toplu işin yalnızca ilk görüntüsü kullanılır.
- `model.face_limit` katı bir üst sınır değil, bir hedeftir; bu nedenle sonuç istenenden daha fazla yüz içerebilir. `-1`, seçimi Tripo'ya bırakır.
- `model.quad`, ağı hangi çıktının taşıyacağını belirler. Etkinleştirildiğinde model FBX çıktısına gelir ve GLB çıktısı boş kalır; devre dışı bırakıldığında model GLB'ye gelir ve FBX boş kalır. Boş çıktı, bağladığınız çıktıysa düğüm hata verir.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` ve `model.orientation` yalnızca dokulu modeller için geçerlidir: `"none"` olduğunda düğüm hiçbir doku ayarı göndermez ve dokusuz geometri döndürür.
- `model.compress_geometry` dörtgen ağlar üzerinde etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model task_id` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | Oluşturulan 3B model GLB formatında. `model.quad` etkinleştirildiğinde boş. | FILE3DGLB |
| `FBX` | Oluşturulan 3B model FBX formatında. Yalnızca `model.quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
