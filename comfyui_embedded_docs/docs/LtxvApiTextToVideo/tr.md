# LTXV Metinden Videoya

LTXV Text To Video düğümü, bir metin açıklamasından profesyonel kalitede videolar oluşturur. Özelleştirilebilir süre, çözünürlük ve kare hızına sahip videolar oluşturmak için harici bir API'ye bağlanır. Ayrıca videoya AI tarafından oluşturulan ses eklenmesini de seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak AI modeli. "LTX-2 (Pro)" daha yüksek kalite sunarken, "LTX-2 (Fast)" hıza göre optimize edilmiştir. | COMBO | Evet | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | AI'nın videoyu oluşturmak için kullanacağı metin açıklaması. Bu alan birden çok satır metin destekler ve 1 ila 10.000 karakter içermelidir. | STRING | Evet | - |
| `süre` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 8). | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `çözünürlük` | Çıktı videosunun piksel boyutları (genişlik x yükseklik). | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Video için saniyedeki kare sayısı (varsayılan: 25). | COMBO | Evet | `25`<br>`50` |
| `ses_oluştur` | true olduğunda, oluşturulan video sahneye uygun AI tarafından üretilen ses içerir (varsayılan: False). Bu, gelişmiş isteğe bağlı bir ayardır. | BOOLEAN | Hayır | - |

**Önemli Kısıtlamalar:**

* `prompt` 1 ila 10.000 karakter arasında olmalıdır.
* 10 saniyeden büyük bir `duration` seçerseniz, ayrıca `"LTX-2 (Fast)"` modelini, `"1920x1080"` çözünürlüğünü ve `25` `fps` kullanmalısınız. Bu kombinasyon daha uzun videolar için gereklidir.

**Not:** Bu düğüm kullanımdan kaldırılmıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
