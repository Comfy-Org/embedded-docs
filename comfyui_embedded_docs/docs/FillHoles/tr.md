# FillHoles

Bu düğüm, açık sınır kenarlarını algılayarak ve bunları kapatmak için yeni yüzeyler oluşturarak 3B bir ağdaki delikleri doldurur. GPU üzerinde çalışır, mevcut geometriyi ve UV'leri korur ve tek ağları, ağ listelerini veya toplu ağları işleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İşlenecek 3B ağ. Tek bir ağı, bir ağ listesini veya toplu bir ağı kabul eder. | MESH | Evet | - |
| `max_perimeter` | Doldurulacak maksimum delik çevresi. 0 devre dışı bırakır. (varsayılan: 0.03) | FLOAT | Evet | 0.0 - üst sınır yok |
| `weld_epsilon_rel` | Ön kaynak toleransı (sınırlayıcı kutu köşegeninin oranı); sınır tespiti kaynaklanmış köşeler gerektirir. 0 atlar. (varsayılan: 1e-5) | FLOAT | Evet | 0.0 - üst sınır yok |
| `max_vertices` | Döngü başına sınır köşelerini sınırlar; merkez-yelpaze yalnızca küçük, neredeyse düzlemsel deliklerde çalışır. ≤16 tutun. (varsayılan: 16) | INT | Evet | 3 - 1024 |
| `fill_chains` | Ayrıca açık zincirleri de doldurur (yalnızca döngüleri değil). Gürültülüdür; KAPALI cumesh ile eşleşir. (varsayılan: False) | BOOLEAN | Evet | True veya False |

Not: `weld_epsilon_rel` 0'dan büyük olduğunda, düğüm delikleri algılamadan önce yinelenen köşeleri önceden kaynaklar. Kaynak toleransı, sınırlayıcı kutu köşegeninin verilen oranında başlar ve ağ kaynaklanmış kabul edilene veya tolerans 1e-2'lik bir üst sınıra ulaşana kadar ikiye katlanarak otomatik olarak artar. 8'den fazla sınır köşesine sahip delikler, yeni bir merkez köşesi ekleyen bir merkez-yelpaze dolgusu kullanırken, daha küçük delikler mevcut bir sınır köşesini yeniden kullanan bir köşe-yelpaze dolgusu kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Girdi toplu biçimiyle eşleşen, delikleri doldurulmuş ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/tr.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
