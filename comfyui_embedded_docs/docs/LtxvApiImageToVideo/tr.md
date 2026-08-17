# LTXV Görüntüden Videoya

LTXV Image To Video düğümü, tek bir başlangıç görüntüsünden profesyonel kalitede bir video oluşturur. Metin isteminize dayalı bir video dizisi oluşturmak için harici bir API kullanır; böylece süreyi, çözünürlüğü ve kare hızını özelleştirebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Video için kullanılacak ilk kare. | IMAGE | Evet | - |
| `model` | Video oluşturma için kullanılacak AI modeli. "Pro" modeli kalite için optimize edilmiştir, "Fast" modeli ise hız için optimize edilmiştir. | COMBO | Evet | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Oluşturulan videonun içeriğini ve hareketini yönlendiren metin açıklaması. | STRING | Evet | - |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 8). | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | Oluşturulan videonun çıktı çözünürlüğü. | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Video için saniyedeki kare sayısı (varsayılan: 25). | COMBO | Evet | `25`<br>`50` |
| `generate_audio` | true olduğunda, oluşturulan video sahneye uygun AI tarafından üretilmiş ses içerir (varsayılan: False). | BOOLEAN | Hayır | - |

**Önemli Kısıtlamalar:**

* `image` girdisi tam olarak bir görüntü içermelidir.
* `prompt` 1 ile 10.000 karakter uzunluğunda olmalıdır.
* 10 saniyeden uzun bir `duration` seçerseniz, **"LTX-2 (Fast)"** modelini, **"1920x1080"** çözünürlüğünü ve **25** FPS kullanmanız gerekir. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
