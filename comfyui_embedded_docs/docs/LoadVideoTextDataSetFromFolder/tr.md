# Video-Metin Yükle (Klasörden)

Bu düğüm, ComfyUI girdi dizinindeki seçili bir alt klasörden video dosyalarını ve bunlarla ilişkili metin açıklamalarını yükler ve bunları iki liste olarak döndürür: videolar ve açıklamalar. Video girişleri tembel referanslardır; bu nedenle kareler yalnızca aşağı akıştaki bir düğüm onlara ihtiyaç duyduğunda çözülür. Desteklenen formatlar MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Tekrar sayısı önekine sahip iç içe klasörler (örneğin `5_classname/`, kohya-ss/sd-scripts gibi araçlar tarafından kullanılır) da desteklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını ve .txt açıklamalarını içeren klasör. | COMBO | Evet | Kullanılabilir birden fazla seçenek: ComfyUI girdi dizinindeki tüm alt klasörleri dinamik olarak listeler |

Seçilen klasör, ComfyUI girdi dizininin bir alt klasörü olmalıdır; bu dizinin dışına çözümlenen bir klasör adı hata verir. Seçilen klasörde desteklenen bir video uzantısına (MP4, AVI, MOV, WEBM, MKV, FLV) sahip dosya yoksa, düğüm hata verir. Adı bir sayı ve ardından alt çizgi ile başlayan iç içe klasörler için (örneğin `5_classname`), o klasördeki her video, bu önek tarafından belirtilen sayı kadar veri kümesine dahil edilir. Her videonun açıklaması, aynı temel ada sahip bir `.txt` dosyasından okunur; eşleşen bir `.txt` dosyası yoksa açıklama boş bir dizedir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `videos` | Tembel video referansları; kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür. Klasörde bulunan her video dosyası için bir giriş. | VIDEO (list) |
| `texts` | Metin açıklamalarının listesi. Video başına bir açıklama; bir videonun eşleşen `.txt` dosyası yoksa açıklaması boş bir dizedir. | STRING (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
