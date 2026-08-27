# Grok Görüntü

Grok Image düğümü, Grok AI modelini kullanarak bir metin açıklamasına dayalı olarak bir veya daha fazla görüntü üretir. İsteminizi harici bir hizmete gönderir ve üretilen görüntüleri iş akışınızda kullanılabilecek tensörler olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü üretimi için kullanılacak belirli Grok modeli. Farklı modeller farklı kalite, hız veya özellikler sunabilir. | COMBO | Evet | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `istem` | Görüntüyü üretmek için kullanılan metin istemi. Bu açıklama, AI'nın ne oluşturacağına rehberlik eder. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | N/A |
| `en boy oranı` | Üretilen görüntü için istenen genişlik-yükseklik oranı. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `görüntü sayısı` | Üretilecek görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ile 10 |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `çözünürlük` | Üretilen görüntüler için istenen çıktı çözünürlüğü (varsayılan: "1K"). | COMBO | Hayır | `"1K"`<br>`"2K"` |
| `kalite` | Kalite seviyesi; yalnızca `grok-imagine-image-2.0` modeli tarafından desteklenir (varsayılan: "medium"; "low" mevcut seçeneklerden biridir). Diğer tüm modellerde bu ayar yok sayılır. | COMBO | Hayır | Birden fazla seçenek mevcut |

**Not:** `seed` parametresi öncelikli olarak düğümün bir iş akışında ne zaman yeniden çalıştırılacağını kontrol etmek için kullanılır. Harici AI hizmetinin doğası gereği, üretilen görüntüler aynı tohum değeriyle bile çalıştırmalar arasında yeniden üretilebilir veya aynı olmayacaktır.

**Fiyatlandırma notu:** Görüntü üretmenin maliyeti seçilen `model`, `resolution`, `quality` ve `number_of_images` değerlerine bağlıdır. `grok-imagine-image-2.0` modeli için "low" kalite, 1K çözünürlükte görüntü başına $0.04 ve 2K çözünürlükte görüntü başına $0.06 maliyete sahiptir; diğer kalite seviyeleri 1K'da görüntü başına $0.06 ve 2K'da görüntü başına $0.08 maliyete sahiptir. `grok-imagine-image-quality` modeli 1K çözünürlükte görüntü başına $0.05 ve 2K çözünürlükte görüntü başına $0.07 maliyete sahiptir. `grok-imagine-image-pro` modeli görüntü başına $0.07 maliyete sahiptir. `grok-imagine-image` modeli görüntü başına $0.02 maliyete sahiptir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görüntü veya bir grup görüntü. `number_of_images` değeri 1 ise tek bir görüntü tensörü döndürülür. 1'den büyükse bir grup görüntü tensörü döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
