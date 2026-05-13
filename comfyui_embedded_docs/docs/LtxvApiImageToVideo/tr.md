> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/tr.md)

LTXV Görüntüden Videoya düğümü, tek bir başlangıç görüntüsünden profesyonel kalitede bir video oluşturur. Metin isteminize dayalı olarak bir video dizisi oluşturmak için harici bir API kullanır; süreyi, çözünürlüğü ve kare hızını özelleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Video için kullanılacak ilk kare. |
| `model` | COMBO | Evet | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` | Video oluşturma için kullanılacak yapay zeka modeli. "Fast" modeli hız için optimize edilmiştir, "Quality" modeli ise görsel kaliteyi önceliklendirir. |
| `prompt` | STRING | Evet | - | Oluşturulan videonun içeriğini ve hareketini yönlendiren bir metin açıklaması. |
| `duration` | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | Videonun saniye cinsinden uzunluğu (varsayılan: 8). |
| `resolution` | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | Oluşturulan videonun çıktı çözünürlüğü. |
| `fps` | COMBO | Evet | `25`<br>`50` | Video için saniyedeki kare sayısı (varsayılan: 25). |
| `generate_audio` | BOOLEAN | Hayır | - | True olduğunda, oluşturulan video sahneye uygun yapay zeka tarafından oluşturulmuş ses içerecektir (varsayılan: False). |

**Önemli Kısıtlamalar:**

* `image` girişi tam olarak bir görüntü içermelidir.
* `prompt` 1 ile 10.000 karakter arasında olmalıdır.
* 10 saniyeden uzun bir `duration` seçerseniz, **"LTX-2 (Fast)"** modelini, **"1920x1080"** çözünürlüğü ve **25** FPS kullanmalısınız. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `af891b45997173c3210d3de4f7b6bd05b14e9d3bf8a94dcb2c1ce08038b7d99d`
