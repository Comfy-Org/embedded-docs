# FillHoles

Bu düğüm, açık sınır kenarlarını algılayarak ve bunları kapatmak için yeni yüzeyler oluşturarak 3B bir mesh'teki delikleri doldurur. GPU üzerinde çalışır, mevcut geometriyi ve UV'leri korur ve tek mesh'leri, mesh listelerini veya mesh batch'lerini işleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `mesh` | İşlenecek 3B mesh. Tek bir mesh, mesh listesi veya batch mesh kabul eder. | MESH | Evet | - |
| `max_perimeter` | Doldurulacak maksimum delik çevresi. 0 devre dışı bırakır. (varsayılan: 0.03) | FLOAT | Evet | 0.0 to no upper limit |
| `weld_epsilon_rel` | Ön kaynak toleransı (sınırlayıcı kutu köşegeninin kesri); sınır algılama, kaynaklanmış köşeler gerektirir. 0 atlar. (varsayılan: 1e-5) | FLOAT | Evet | 0.0 to no upper limit |
| `max_vertices` | Döngü başına sınır köşe sayısını üst sınırlar; merkez-yelpaze (centroid-fan) yalnızca küçük, neredeyse düzlemsel delikler için çalışır. ≤16 tutun. (varsayılan: 16) | INT | Evet | 3 to 1024 |
| `fill_chains` | Ayrıca açık zincirleri de doldurur (yalnızca döngüleri değil). Gürültülüdür; OFF, cumesh ile eşleşir. (varsayılan: False) | BOOLEAN | Evet | True or False |

Not: `weld_epsilon_rel` 0'dan büyük olduğunda, düğüm delikleri algılamadan önce yinelenen köşeleri ön kaynaklar. Kaynak toleransı, sınırlayıcı kutu köşegeninin verilen kesrinde başlar ve mesh kaynaklanmış kabul edilene veya tolerans 1e-2 üst sınırına ulaşana kadar ikiye katlanarak otomatik olarak artar. 8'den fazla sınır köşesi olan delikler, merkez-yelpaze dolgusu kullanır (yeni bir merkez köşesi ekleyerek); daha küçük delikler ise mevcut bir sınır köşesini yeniden kullanan köşe-yelpaze (vertex-fan) dolgusu kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `mesh` | Deliklerin doldurulduğu, giriş batch formatıyla eşleşen mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/tr.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
