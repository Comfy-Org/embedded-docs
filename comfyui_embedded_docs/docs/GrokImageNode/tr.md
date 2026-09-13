# Grok Görüntü

Grok Image düğümü, Grok AI modelini kullanarak bir metin açıklamasından bir veya daha fazla görsel üretir. İstem metninizi harici bir hizmete gönderir ve üretilen görselleri iş akışınızda kullanılabilecek tensörler olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görsel üretimi için kullanılacak belirli Grok modeli. Farklı modeller değişen kalite, hız veya özellikler sunabilir. | COMBO | Evet | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | Görseli üretmek için kullanılan metin istemi. Bu açıklama, yapay zekâya ne oluşturacağı konusunda rehberlik eder. En az 1 karakter uzunluğunda olmalıdır (yalnızca boşluk içeren metin kabul edilmez). | STRING | Evet | N/A |
| `aspect_ratio` | Üretilen görsel için istenen genişlik-yükseklik oranı. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Üretilecek görsel sayısı (varsayılan: 1). | INT | Evet | 1 ile 10 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `resolution` | Üretilen görseller için istenen çıktı çözünürlüğü (varsayılan: "1K"). | COMBO | Hayır | `"1K"`<br>`"2K"` |
| `quality` | Kalite düzeyi; yalnızca `grok-imagine-image-2.0` modeli tarafından desteklenir (varsayılan: "medium"; "low" mevcut seçeneklerden biridir). Diğer tüm modeller için bu ayar yok sayılır. | COMBO | Hayır | Birden çok seçenek mevcut |

**Not:** `seed` parametresi öncelikle düğümün bir iş akışı içinde ne zaman yeniden yürütüleceğini kontrol etmek için kullanılır. Harici yapay zekâ hizmetinin doğası gereği, üretilen görseller aynı tohumla bile çalıştırmalar arasında yeniden üretilebilir veya aynı olmayacaktır.

**Fiyatlandırma notu:** Görsel üretmenin maliyeti seçilen `model`, `resolution`, `quality` ve `number_of_images` değerlerine bağlıdır. `grok-imagine-image-2.0` modeli için "low" kalitesi 1K çözünürlükte görsel başına $0.04 ve 2K çözünürlükte görsel başına $0.06 tutarındadır; diğer kalite düzeyleri 1K'da görsel başına $0.06 ve 2K'da görsel başına $0.08 tutarındadır. `grok-imagine-image-quality` modeli 1K çözünürlükte görsel başına $0.05 ve 2K çözünürlükte görsel başına $0.07 tutarındadır. `grok-imagine-image-pro` modeli görsel başına $0.07 tutarındadır. `grok-imagine-image` modeli görsel başına $0.02 tutarındadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görsel veya bir görsel grubu. `number_of_images` 1 ise, tek bir görsel tensörü döndürülür. 1'den büyükse, bir görsel tensörü grubu döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
