# Video-Metin Yükle (Klasörden)

Bu düğüm, ComfyUI girdi dizini içindeki seçili bir alt klasörden video dosyalarını ve ilişkili metin açıklamalarını yükler ve bunları iki liste olarak döndürür: videolar ve açıklamalar. Video girdileri tembel referanslardır, bu nedenle kareler yalnızca aşağı akış düğümü ihtiyaç duyduğunda çözülür. Desteklenen biçimler MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Tekrar sayısı önekine sahip iç içe klasörler (örneğin kohya-ss/sd-scripts gibi araçların kullandığı `5_classname/`) de desteklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını ve .txt açıklamalarını içeren klasör. | STRING | Evet | Combo: ComfyUI girdi dizini içindeki tüm alt klasörlerin dinamik listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
Seçilen klasörde desteklenen bir video uzantısına sahip dosya yoksa düğüm bir hata oluşturur. Adı bir sayı ve ardından alt çizgi ile başlayan iç içe klasörlerde (örneğin `5_classname`), o klasördeki her video, bu önekin belirttiği sayı kadar veri kümesine dahil edilir.
|-------------|-----------|-----------|
| `videos` | Tembel video referansları; kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür. Klasörde bulunan her video dosyası için bir girdi. | VIDEO (list) |
| `texts` | Metin açıklamaları listesi. Her video için bir açıklama; bir videoyla eşleşen `.txt` dosyası yoksa açıklaması boş bir dizedir. | STRING (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
