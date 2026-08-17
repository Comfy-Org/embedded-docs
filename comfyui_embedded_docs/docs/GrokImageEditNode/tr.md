# Grok Görüntü Düzenle

Grok Image Edit düğümü, metin istemine dayalı olarak mevcut bir görüntüyü düzenler. Grok API'sini kullanarak, girdi görüntünüzün varyasyonları olan ve açıklamanız tarafından yönlendirilen bir veya daha fazla yeni görüntü oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü düzenleme için kullanılacak belirli yapay zeka modeli. | COMBO | Evet | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | Düzenlenecek girdi görüntüsü/görüntüleri. "pro" modeli yalnızca 1 görüntü desteklerken, en fazla 3 girdi görüntüsünü destekler. | IMAGE | Evet |  |
| `prompt` | Görüntüyü oluşturmak için kullanılan metin istemi. Boşluklar temizlendikten sonra en az 1 karakter olmalıdır. | STRING | Evet |  |
| `resolution` | Çıktı görüntüsünün çözünürlüğü. | COMBO | Evet | `"1K"`<br>`"2K"` |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 10 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 2147483647 |
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. Yalnızca görüntü girdisine birden fazla görüntü bağlandığında izin verilir. "auto" olarak ayarlanırsa, en-boy oranı otomatik olarak belirlenir (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Önemli kısıtlamalar:**
- `image` girdisi, yalnızca 1 girdi görüntüsünü destekleyen `grok-imagine-image-pro` modeli kullanılmadığı sürece en fazla 3 görüntüyü destekler.
- `aspect_ratio` parametresi yalnızca `image` girdisine birden fazla görüntü bağlandığında özel bir değere ("auto" dışında) ayarlanabilir. Tek bir girdi görüntüsüyle özel bir en-boy oranı ayarlamak hataya neden olur.

**Not:** Bu düğüm artık kullanımdan kaldırılmıştır (deprecated).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Düğüm tarafından oluşturulan düzenlenmiş görüntü(ler). `number_of_images` değeri 1'den büyükse, çıktılar bir yığın (batch) halinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
