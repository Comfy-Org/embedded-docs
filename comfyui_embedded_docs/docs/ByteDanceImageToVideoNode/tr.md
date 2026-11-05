# ByteDance Görüntüden Videoya

ByteDance Image to Video düğümü; bir girdi görüntüsü ve metin istemine dayalı olarak, ByteDance modellerini bir API aracılığıyla kullanarak videolar üretir. Bir başlangıç görüntü karesi alır ve sağlanan açıklamayı izleyen bir video dizisi oluşturur. Düğüm; video çözünürlüğü, en-boy oranı, süre ve diğer üretim parametreleri için çeşitli özelleştirme seçenekleri sunar.

**Not:** Bu düğüm kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

**Not:** BytePlus, Seedance 1.5 Pro modelini 11 Kasım 2026'da kapatıyor; bu nedenle bu düğüm artık onu sunmuyor ve onunla kaydedilen iş akışları çalışmayı durduruyor. Bunun yerine `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` veya [Seedance 2.5 iş ortağı düğümü](https://docs.comfy.org/tr/tutorials/partner-nodes/bytedance/seedance-2-5) kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmada kullanılacak ByteDance modeli (varsayılan: `"seedance-1-0-pro-fast-251015"`). | COMBO | Evet | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. Baştaki ve sondaki boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `görüntü` | Video için kullanılacak ilk kare. 300x300 ile 6000x6000 piksel arasında ve en-boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en-boy oranı` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 - 12 |
| `seed` | Üretimde kullanılacak tohum (varsayılan: 0). | INT | Hayır | 0 - 2147483647 |
| `sabit kamera` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitleme talimatını ekler ancak gerçek etkiyi garanti etmez (varsayılan: False). | BOOLEAN | Hayır | `False`<br>`True` |
| `filigran` | Videoya "AI generated" filigranı eklenip eklenmeyeceğini belirtir (varsayılan: False). | BOOLEAN | Hayır | `False`<br>`True` |
| `ses_oluştur` | Yapay zeka ile oluşturulmuş bir ses parçası ekler. Kalan modeller bu girdiyi yok sayar (varsayılan: False). | BOOLEAN | Hayır | `False`<br>`True` |

**Not:** İstem, aşağıdaki sözcükleri içermemelidir (büyük/küçük harf ayrımı gözetmeksizin): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Bu parametreler kendilerine ayrılmış girdiler aracılığıyla ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi görüntüsüne ve istem parametrelerine dayalı olarak oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a1841a368e625bd90583e0f0dbdc32369e6701a44cf985f01de8faa3d999b224`
