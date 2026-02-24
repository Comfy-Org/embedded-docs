> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/tr.md)

LTXV Image To Video düğümü, tek bir başlangıç görselinden profesyonel kalitede bir video oluşturur. Metin isteminize dayalı bir video dizisi oluşturmak için harici bir API kullanır ve süre, çözünürlük ve kare hızını özelleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Video için kullanılacak ilk kare. |
| `model` | COMBO | Evet | `"LTX-2 (Hızlı)"`<br>`"LTX-2 (Kalite)"` | Video oluşturma için kullanılacak AI modeli. "Hızlı" model hız için optimize edilmiştir, "Kalite" modeli ise görsel sadakati önceliklendirir. |
| `prompt` | STRING | Evet | - | Oluşturulan videonun içeriğini ve hareketini yönlendiren bir metin açıklaması. |
| `duration` | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | Videoyun saniye cinsinden uzunluğu (varsayılan: 8). |
| `resolution` | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | Oluşturulan videonun çıktı çözünürlüğü. |
| `fps` | COMBO | Evet | `25`<br>`50` | Video için saniyedeki kare sayısı (varsayılan: 25). |
| `generate_audio` | BOOLEAN | Hayır | - | True olduğunda, oluşturulan video sahneye uyan AI tarafından üretilmiş sesi içerecektir (varsayılan: False). |

**Önemli Kısıtlamalar:**

* `image` girişi tam olarak bir görsel içermelidir.
* `prompt` 1 ile 10.000 karakter arasında bir uzunlukta olmalıdır.
* 10 saniyeden uzun bir `duration` seçerseniz, **"LTX-2 (Hızlı)"** modelini, **"1920x1080"** çözünürlüğünü ve **25** FPS değerini kullanmalısınız. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |
