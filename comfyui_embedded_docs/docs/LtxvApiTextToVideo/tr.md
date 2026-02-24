> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/tr.md)

LTXV Metinden Videoya düğümü, metin açıklamasından profesyonel kalitede videolar oluşturur. Özelleştirilebilir süre, çözünürlük ve kare hızına sahip videolar oluşturmak için harici bir API'ye bağlanır. Ayrıca videoya AI tarafından oluşturulmuş ses eklenmesini de seçebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"LTX-2 (Hızlı)"`<br>`"LTX-2 (Kalite)"`<br>`"LTX-2 (Turbo)"` | Video oluşturma için kullanılacak AI modeli. Mevcut modeller kaynak kodundaki `MODELS_MAP`'ten eşlenir. |
| `prompt` | STRING | Evet | - | AI'nın video oluşturmak için kullanacağı metin açıklaması. Bu alan birden fazla satır metni destekler. |
| `duration` | COMBO | Evet | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 8). |
| `resolution` | COMBO | Evet | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | Çıktı videosunun piksel boyutları (genişlik x yükseklik). |
| `fps` | COMBO | Evet | `25`<br>`50` | Video için saniyedeki kare sayısı (varsayılan: 25). |
| `generate_audio` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, oluşturulan video sahneye uyan AI tarafından oluşturulmuş ses içerecektir (varsayılan: False). |

**Önemli Kısıtlamalar:**

* `prompt` 1 ile 10.000 karakter arasında olmalıdır.
* 10 saniyeden uzun bir `duration` seçerseniz, aynı zamanda `"LTX-2 (Hızlı)"` modelini, `"1920x1080"` çözünürlüğünü ve `25` `fps` değerini kullanmalısınız. Bu kombinasyon daha uzun videolar için gereklidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
