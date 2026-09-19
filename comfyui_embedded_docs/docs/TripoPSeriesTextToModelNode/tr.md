# Tripo P2: Metinden Modele

Metinden bir istem kullanarak Tripo'nun P2 modeliyle temiz topolojiye sahip düşük poligonlu bir 3B model üretir. Sonuç, bir üçgen ağ (GLB) olarak veya `model.quad` etkinleştirildiğinde quad ağırlıklı bir ağ (FBX) olarak döner.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Tripo P serisi model. Bir model seçildiğinde aşağıda kendi girdileri görünür. | DYNAMIC_COMBO | Evet | `"P2"` |

### P2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Üretilecek 3B modelin metin açıklaması. Boş olmamalıdır, en fazla 1024 karakter (varsayılan: boş). | STRING | Evet | 1024 karaktere kadar |
| `negative_prompt` | Üretilen modelde kaçınılacak şeylerin metin açıklaması (varsayılan: boş). | STRING | Hayır | 255 karaktere kadar |
| `quad` | GLB çıktısındaki üçgen ağ yerine FBX çıktısında quad ağırlıklı bir ağ döndür (varsayılan: False). | BOOLEAN | Evet | True/False |
| `face_limit` | Hedef yüz sayısı. `-1`, Tripo'nun seçmesini sağlar. `model.quad` etkinleştirildiğinde sınır 48 ile 25.000 arasındadır, aksi halde 48 ile 50.000 arasındadır (varsayılan: -1). | INT | Evet | -1 veya 48 - 50000 |
| `texture` | Temel renk doku çözünürlüğü: standart 2K, ayrıntılı 4K ve ekstrem 8K. `"none"` dokusuz bir ağ döndürür (varsayılan: `"standard"`). | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Temel renge metalik, pürüzlülük ve normal haritaları ekler. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: True). | BOOLEAN | Evet | True/False |
| `model_seed` | Geometri için tohum (varsayılan: 42). | INT | Evet | 0 - 2147483647 |
| `image_seed` | Modellemeden önce Tripo'nun istemden çizdiği görüntü için tohum (varsayılan: 42). Gelişmiş ayar. | INT | Evet | 0 - 2147483647 |
| `texture_seed` | Dokular için tohum (varsayılan: 42). Gelişmiş ayar. | INT | Evet | 0 - 2147483647 |
| `auto_size` | Modeli sahne dönüşümü aracılığıyla metre cinsinden gerçek dünya boyutuna ölçekler. `model.texture` `"none"` olduğunda yok sayılır (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `export_uv` | Ağ dokusuz olduğunda UV açılımı uygular. Dokulu ağlara her zaman UV açılımı uygulanır (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `compress_geometry` | meshopt geometri sıkıştırması uygular: çok daha küçük dosyalar, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez. Quad ağlar için yok sayılır (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | True/False |

**Notlar:**

- `model.prompt` gereklidir; `model.negative_prompt` isteğe bağlıdır ve 255 karakterle sınırlıdır.
- `model.face_limit` katı bir üst sınır değil hedeftir, bu nedenle sonuç istenenden daha fazla yüz içerebilir. `-1` seçimi Tripo'ya bırakır.
- `model.quad` ağın hangi çıktıda taşınacağını belirler. Etkinleştirildiğinde model FBX çıktısına gelir ve GLB çıktısı boş kalır; devre dışı bırakıldığında model GLB'ye gelir ve FBX boş kalır. Bağladığınız çıktı boş olan çıktıysa düğüm hata verir.
- `model.texture`, `model.pbr`, `model.texture_seed` ve `model.auto_size` yalnızca dokulu modeller için geçerlidir: `"none"` ile düğüm hiçbir doku ayarı göndermez ve yalnızca geometri döndürür.
- `model.compress_geometry` quad ağlar üzerinde etkisizdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model task_id` | Model üretim isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | Üretilen 3B modelin GLB biçimindeki hali. `model.quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | Üretilen 3B modelin FBX biçimindeki hali. Yalnızca `model.quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`
