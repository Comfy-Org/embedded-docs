LTXV Metinden Videoya düğümü, bir metin açıklamasından profesyonel kalitede videolar üretir. Harici bir API'ye bağlanarak özelleştirilebilir süre, çözünürlük ve kare hızına sahip videolar oluşturur. Ayrıca videoya yapay zeka tarafından oluşturulmuş ses eklemeyi de tercih edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak yapay zeka modeli. Mevcut modeller, kaynak koddaki `MODELS_MAP`'ten eşlenmiştir. | COMBO | Evet | `"LTX-2 (Hızlı)"`<br>`"LTX-2 (Kaliteli)"`<br>`"LTX-2 (Turbo)"` |
| `prompt` | Yapay zekanın videoyu oluşturmak için kullanacağı metin açıklaması. Bu alan birden çok satır metin destekler. | STRING | Evet | - |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 8). | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `çözünürlük` | Çıktı videosunun piksel cinsinden boyutları (genişlik x yükseklik). | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Video için saniyedeki kare sayısı (varsayılan: 25). | COMBO | Evet | `25`<br>`50` |
| `ses_oluştur` | Etkinleştirildiğinde, oluşturulan video sahneye uygun yapay zeka tarafından oluşturulmuş ses içerecektir (varsayılan: False). | BOOLEAN | Hayır | - |

**Önemli Kısıtlamalar:**

* `prompt` 1 ile 10.000 karakter arasında olmalıdır.
* 10 saniyeden uzun bir `duration` seçerseniz, ayrıca `"LTX-2 (Hızlı)"` modelini, `"1920x1080"` çözünürlüğünü ve 25 `fps` değerini kullanmalısınız. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a0c16995a07d879113bd3ca8fea64be414feee96bd8293a3e7737ede7d30e11d`
