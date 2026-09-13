# Video-Metin Yükle (Klasörden)

Bu düğüm, ComfyUI giriş dizini içindeki bir klasörden video dosyalarını ve bunlarla eşleşen metin başlıklarını yükler ve bunları iki liste olarak döndürür: videolar ve başlıklar. Video girdileri tembel referanslardır; bu nedenle kareler yalnızca aşağı akıştaki bir düğüm bunlara ihtiyaç duyduğunda çözülür. Desteklenen biçimler MP4, AVI, MOV, WEBM, MKV ve FLV'dir; ayrıca yineleme sayısı öneki içeren iç içe klasörler (örn. kohya-ss/sd-scripts gibi araçlarda kullanılan `5_classname/`) de desteklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını ve .txt başlıklarını içeren klasör. | COMBO | Evet | ComfyUI giriş dizini içindeki tüm alt klasörleri dinamik olarak listeler |

Seçilen klasör, ComfyUI giriş dizininin bir alt klasörü olmalıdır; o dizinin dışına çözümlenen bir klasör adı hata verir. Seçilen klasör desteklenen bir video uzantısına sahip (MP4, AVI, MOV, WEBM, MKV, FLV) hiçbir dosya içermiyorsa düğüm hata verir. Adı bir sayı ve ardından bir alt çizgi ile başlayan iç içe klasörlerde (örneğin `5_classname`), o klasördeki her video, veri kümesine bu önekte belirtilen sayı kadar dahil edilir. Her videonun başlığı, aynı temel ada sahip bir `.txt` dosyasından okunur; eşleşen bir `.txt` dosyası yoksa başlık boş dizedir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `videos` | Tembel video referansları; kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür. Klasörde bulunan her video dosyası için bir girdi. | VIDEO (list) |
| `texts` | Metin başlıkları listesi. Her video için bir başlık; bir videonun eşleşen `.txt` dosyası yoksa başlığı boş dizedir. | STRING (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
