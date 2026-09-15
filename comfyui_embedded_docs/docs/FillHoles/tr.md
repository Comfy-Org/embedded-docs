# Delikleri Doldur

Bu düğüm, açık sınır kenarlarını algılayıp bunları kapatacak yeni yüzler oluşturarak bir 3B mesh'teki delikleri doldurur. GPU'da çalışır, mevcut geometriyi ve UV'leri korur ve tek meshleri, mesh listelerini veya toplu meshleri işleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İşlenecek 3B mesh. Tek bir mesh, mesh listesi veya toplu mesh kabul eder. | MESH | Evet | - |
| `max_perimeter` | Doldurulacak maksimum delik çevresi. 0 devre dışı bırakır. (varsayılan: 0.03) | FLOAT | Evet | 0.0 ile üst sınır yok (adım 0.0001) |
| `weld_epsilon_rel` | Ön kaynaklama toleransı (sınırlayıcı kutu köşegeninin kesri); sınır algılama, kaynaklanmış köşeler gerektirir. 0 atlar. (varsayılan: 1e-5) | FLOAT | Evet | 0.0 ile üst sınır yok (adım 1e-6) |
| `max_vertices` | Döngü başına sınır köşelerine üst sınır koy; ağırlık merkezi yelpazesi yalnızca küçük, neredeyse düzlemsel delikler için çalışır. ≤16 tutun. (varsayılan: 16) | INT | Evet | 3 ile 1024 |
| `fill_chains` | Açık zincirleri de doldur (yalnızca döngüleri değil). Gürültülü; OFF cumesh ile eşleşir. (varsayılan: False) | BOOLEAN | Evet | True veya False |

Not: `max_perimeter` 0'dan büyük olduğunda düğüm delikleri doldurur; 0 olduğunda delik doldurma tamamen atlanır. `weld_epsilon_rel` 0'dan büyük olduğunda düğüm, delikleri algılamadan önce yinelenen köşeleri önceden kaynaklar. Kaynaklama toleransı, sınırlayıcı kutu köşegeninin verilen kesriyle başlar ve mesh kaynaklanmış kabul edilene kadar veya tolerans 1e-2 sınırına ulaşana kadar otomatik olarak ikiye katlanarak artar. 8'den fazla sınır köşesine sahip delikler bir ağırlık merkezi yelpazesi dolgusu kullanır (yeni bir ağırlık merkezi köşesi ekler); daha küçük delikler ise mevcut bir sınır köşesini yeniden kullanan bir köşe yelpazesi dolgusu kullanır. Varsayılan olarak yalnızca kapalı sınır döngüleri doldurulur; açık zincirleri de kapatmak için `fill_chains` değerini True yapın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `mesh` | Delikleri doldurulmuş mesh; girdi toplu formatıyla eşleşir. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/tr.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
