# Video-Metin Yükle (Klasörden)

Bu düğüm, ComfyUI girdi dizinindeki seçili bir alt klasörden video-metin çiftlerinden oluşan bir veri kümesi yükler ve bunları iki liste olarak döndürür: videolar ve metin açıklamaları. Video kayıtları tembel referanslardır, bu nedenle kareler yalnızca aşağı akıştaki bir düğüm bunlara ihtiyaç duyduğunda çözülür. Desteklenen formatlar MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Açıklamalar, her video dosyasıyla aynı adı paylaşan `.txt` dosyalarından okunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını ve .txt açıklamalarını içeren klasör. | COMBO | Evet | ComfyUI girdi dizini içindeki tüm alt klasörler (dinamik liste) |

Notlar:
- Seçilen klasör, ComfyUI girdi dizininin bir alt klasörü olmalıdır; bu dizin dışına çözümlenen yollar reddedilir.
- Klasör, desteklenen bir video uzantısına sahip hiçbir dosya içermiyorsa, düğüm bir hata verir.
- Adı bir sayı ve ardından alt çizgi ile başlayan iç içe klasörler (örneğin `5_classname/`, kohya-ss/sd-scripts gibi araçlar tarafından kullanılır) de desteklenir: bu klasördeki her video, veri kümesine bu önek tarafından belirtilen sayıda dahil edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `videos` | Tembel video referansları; kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür. Klasörde bulunan her video dosyası için bir kayıt. | VIDEO (liste) |
| `texts` | Metin açıklamalarının listesi. Her video için bir açıklama; bir videonun eşleşen `.txt` dosyası yoksa açıklaması boş bir dizedir. | STRING (liste) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
