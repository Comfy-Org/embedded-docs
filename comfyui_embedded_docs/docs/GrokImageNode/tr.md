# Grok Görüntü

The Grok Image düğümü, Grok AI görüntü modellerini kullanarak bir metin istemine dayalı olarak bir veya daha fazla görüntü üretir. İstemi ve ayarları harici bir hizmete gönderir ve üretilen görüntüleri, iş akışında başka yerlerde kullanılabilen tensörler olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü üretimi için kullanılacak belirli Grok modeli. Farklı modeller farklı kalite, hız veya özellikler sunabilir. | COMBO | Evet | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | Görüntüyü üretmek için kullanılan metin istemi. Bu açıklama, yapay zekâya ne oluşturacağı konusunda rehberlik eder. En az 1 boşluk olmayan karakter içermelidir. | STRING | Evet | N/A |
| `aspect_ratio` | Üretilen görüntü için istenen genişlik-yükseklik oranı. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Üretilecek görüntü sayısı (varsayılan: 1). | INT | Evet | 1 to 10 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 to 2147483647 |
| `resolution` | Üretilen görüntüler için istenen çıktı çözünürlüğü (varsayılan: "1K"). | COMBO | Hayır | `"1K"`<br>`"2K"` |
| `quality` | Kalite düzeyi, yalnızca grok-imagine-image-2.0 modeli tarafından desteklenir (varsayılan: "medium"). | COMBO | Hayır | Birden fazla seçenek mevcut |

**Not:** `quality` parametresi yalnızca `model` "grok-imagine-image-2.0" olarak ayarlandığında uygulanır. Diğer tüm modellerde bu ayar yok sayılır.

**Not:** `seed` parametresi öncelikle düğümün bir iş akışında ne zaman yeniden yürütüleceğini kontrol etmek için kullanılır. Harici yapay zekâ hizmetinin doğası gereği, aynı tohum kullanılsa bile üretilen görüntüler çalıştırmalar arasında yeniden üretilemez.

**Fiyatlandırma notu:** Görüntü üretiminin maliyeti seçilen `model`, `resolution`, `quality` ve `number_of_images` değerlerine bağlıdır; toplam fiyat, görüntü başına ücretin `number_of_images` ile çarpılmasıyla elde edilir. "grok-imagine-image-2.0" modeli için görüntü başına ücret, "1K" çözünürlükte $0.04 ve "2K" çözünürlükte "low" kalite ile $0.06 veya "1K" için $0.06 ve diğer kalite düzeyleriyle "2K" için $0.08'dir. "grok-imagine-image-quality" modelinin maliyeti "1K"da görüntü başına $0.05 ve "2K"da görüntü başına $0.07'dir. "grok-imagine-image-pro" modelinin maliyeti görüntü başına $0.07'dir. Diğer modellerin maliyeti görüntü başına $0.02'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görüntü veya bir grup görüntü. `number_of_images` 1 ise, tek bir görüntü tensörü döndürülür. 1'den büyükse, bir grup görüntü tensörü döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
