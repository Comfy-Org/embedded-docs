Grok Görsel düğümü, Grok AI modelini kullanarak bir metin açıklamasına dayalı olarak bir veya daha fazla görsel oluşturur. İsteminizi harici bir servise gönderir ve oluşturulan görselleri iş akışınızda kullanabileceğiniz tensörler olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Görsel oluşturma için kullanılacak belirli Grok modeli. Farklı modeller farklı kalite, hız veya özellikler sunabilir. | COMBO | Evet | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `istem` | Görseli oluşturmak için kullanılan metin istemi. Bu açıklama, yapay zekaya ne oluşturacağı konusunda rehberlik eder. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | Yok |
| `en boy oranı` | Oluşturulan görsel için istenen genişlik-yükseklik oranı. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `görüntü sayısı` | Oluşturulacak görsel sayısı (varsayılan: 1). | INT | Hayır | 1 ila 10 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen bir tohum değeri. Gerçek görsel sonuçları belirleyici değildir ve aynı tohumla bile farklılık gösterecektir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `çözünürlük` | Oluşturulan görseller için istenen çıktı çözünürlüğü (varsayılan: "1K"). | COMBO | Hayır | `"1K"`<br>`"2K"` |

**Not:** `seed` parametresi öncelikle düğümün bir iş akışı içinde ne zaman yeniden yürütüleceğini kontrol etmek için kullanılır. Harici AI servisinin doğası gereği, oluşturulan görseller aynı tohumla bile çalıştırmalar arasında tekrarlanabilir veya aynı olmayacaktır.

**Fiyatlandırma notu:** Görsel oluşturma maliyeti seçilen `model`, `resolution` ve `number_of_images` değerlerine bağlıdır. Örneğin, "grok-imagine-image-quality" modeli "1K" çözünürlükte görsel başına 0,05 ABD doları, "2K" çözünürlükte ise görsel başına 0,07 ABD dolarıdır. "grok-imagine-image-pro" modeli görsel başına 0,07 ABD doları, diğer modeller ise görsel başına 0,02 ABD dolarıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan görsel veya bir grup görsel. `görüntü sayısı` değeri 1 ise tek bir görsel tensörü döndürülür. 1'den büyükse bir grup görsel tensörü döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `5c8a76d3636dea8bcc6ade0d8adb6e6d1610b518a31e15fc7fce3f107fe63953`
