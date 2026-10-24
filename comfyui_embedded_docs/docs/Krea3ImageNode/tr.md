# Krea 3 Image

Krea 3 Image, görüntüleri Krea 3 ile düzenler veya hiç görüntü bağlı olmadığında bir metin isteminden yeni bir görüntü oluşturur. En fazla 8 görüntü bağlayın ve nelerin değiştirileceğini ve nelerin korunacağını açıklayın; istemde bunlara @Image1, @Image2 ve benzeri şekilde atıfta bulunun. En boy oranı ve çözünürlük çıktı boyutunu belirler, düşünme modu ise daha ayrıntılı bir plan için hızdan ödün verir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Krea 3 modeli. Bir model seçildiğinde kabul ettiği parametreler görünür. | DYNAMIC_COMBO | Evet | `"Krea 3"` |

### Krea 3 Girdileri

Bu girdiler, `model` değeri `Krea 3` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Düzenlenecek görüntüler, bağlantı sırasına göre numaralandırılır. Bağlanan her görüntü 8'lik sınıra dahil edilir. Yalnızca metinden oluşturmak için boş bırakın. | IMAGE | Hayır | 0 - 8 görüntü |
| `model.prompt` | Neyin değiştirileceği ve neyin korunacağı. Görüntülere `@Image1`, `@Image2` vb. veya görüntü 1, görüntü 2, ... olarak atıfta bulunun. İstem boş olamaz. | STRING | Evet | - |
| `model.aspect_ratio` | Sonucun en boy oranı. `"auto"`, ilk görüntüyü veya hiç görüntü bağlı değilse istemi takip eder. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | Çıktı çözünürlüğü. `"2K"`, `"1K"` seçeneğine göre daha uzun sürer ve daha büyük bir görüntü üretir. (varsayılan: `"2K"`) | COMBO | Evet | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | Krea 3'ün düzenlemeyi planlamaya ne kadar emek harcadığı. `"fast"` önerilir; `"high"` ise karmaşık düzenlemeleri daha ayrıntılı planlar ve daha uzun sürer. `"ultra"` birkaç aday üretir ve en iyisini döndürür; en az bir görüntü gerektirir, her zaman 2K çıktı verir ve `precise_edit` desteklemez. (varsayılan: `"fast"`) | COMBO | Evet | `"fast"`<br>`"high"`<br>`"ultra"` |
| `model.precise_edit` | Düzenlenen alanın dışındaki her şeyi değişmeden korur. En az bir bağlı görüntü gerektirir. (varsayılan: False) | BOOLEAN | Evet | false<br>true |
| `model.seed` | İstek için tohum (varsayılan: 42). Krea, oluşturmadan önce istemi yeniden yazar; bu nedenle aynı tohum bir görüntüyü tekrar etmez. | INT | Evet | 0 - 2147483647 |

`@Image3` gibi bir referans yalnızca en az üç görüntü bağlı olduğunda kabul edilir; aksi halde düğüm bir hata verir. Referans görüntüleri, istek gönderilmeden önce yüklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan veya düzenlenen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `9e8d036f1ebca81b85e6ef42a015e7e2925bf467fa32e82180ee1b76dcc91c0b`
