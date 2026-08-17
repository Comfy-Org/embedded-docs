# LTXV Metinden Videoya

LTXV Metinden Videoya düğümü, bir metin açıklamasından profesyonel kalitede videolar oluşturur. Özelleştirilebilir süre, çözünürlük ve kare hızına sahip videolar oluşturmak için harici bir API'ye bağlanır. Ayrıca videoya yapay zeka tarafından oluşturulan ses eklemeyi de seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak yapay zeka modeli. "LTX-2 (Pro)" daha yüksek kalite sunarken, "LTX-2 (Fast)" hız için optimize edilmiştir. | COMBO | Evet | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Yapay zekanın video oluşturmak için kullanacağı metin açıklaması. Bu alan birden çok satır metin destekler. | STRING | Evet | - |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 8). | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | Çıktı videosunun piksel boyutları (genişlik x yükseklik). | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Video için saniyedeki kare sayısı (varsayılan: 25). | COMBO | Evet | `25`<br>`50` |
| `generate_audio` | true olduğunda, oluşturulan video sahneye uygun yapay zeka tarafından oluşturulmuş ses içerir (varsayılan: False). | BOOLEAN | Hayır | `True`<br>`False` |

**Önemli Kısıtlamalar:**

* `prompt` 1 ile 10.000 karakter arasında olmalıdır.
* 10 saniyeden büyük bir `duration` seçerseniz, "LTX-2 (Fast)" modelini, `"1920x1080"` çözünürlüğünü ve 25 `fps` değerini de kullanmanız gerekir. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
