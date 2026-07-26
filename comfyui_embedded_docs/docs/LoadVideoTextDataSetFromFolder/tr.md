# Video-Metin Yükle (Klasörden)

Bu düğüm, ComfyUI girdi dizini içindeki belirtilen bir alt klasörden video dosyaları ve bunlara ait metin açıklamalarından oluşan bir veri kümesi yükler. İki liste döndürür: tembel video referansları (kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür) ve bunlarla ilişkili açıklamalar. Düğüm; MP4, AVI, MOV, WEBM, MKV ve FLV gibi yaygın video biçimlerini destekler ve kohya‑ss/sd‑scripts gibi araçlar tarafından kullanılan tekrarlı ön ek içeren iç içe klasör yapılarını da (ör. `5_classname/`) işleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını ve `.txt` açıklama dosyalarını içeren alt klasör. ComfyUI girdi dizinindeki mevcut alt klasörler arasından seçim yapın. | STRING | Evet | Combo: ComfyUI girdi klasörü içindeki tüm alt dizinlerin dinamik listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `videos` | Yüklenen video dosyalarına yönelik tembel referanslar. Kareler, yalnızca bunları işleyen bir aşağı akış düğümüne bağlandığında çözülür. Her öğe, girdi klasöründen bir videoya karşılık gelir. | VIDEO (liste) |
| `texts` | Her video için bir tane olmak üzere metin açıklamalarının listesi. Bir videoyla eşleşen `.txt` dosyası yoksa, açıklaması boş bir dizedir. | STRING (liste) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
