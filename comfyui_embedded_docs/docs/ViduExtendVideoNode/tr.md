ViduExtendVideoNode, mevcut bir videonun süresini uzatmak için ek kareler oluşturur. Kaynak videoya ve isteğe bağlı bir metin istemine dayanarak kesintisiz bir devam oluşturmak için belirtilen bir AI modelini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video uzatma için kullanılacak AI modeli. Bir model seçmek, o modele özgü süre ve çözünürlük ayarlarını gösterir. | COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `model.duration` | Uzatılmış videonun saniye cinsinden süresi (varsayılan: 4). Bu ayar, bir model seçildikten sonra görünür. | INT | Evet | 1 ila 7 |
| `model.resolution` | Çıktı videosunun çözünürlüğü. Bu ayar, bir model seçildikten sonra görünür. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `video` | Uzatılacak kaynak video. | VIDEO | Evet | - |
| `prompt` | Uzatılmış videonun içeriğini yönlendirmek için isteğe bağlı bir metin istemi (maksimum 2000 karakter, varsayılan: boş). | STRING | Hayır | - |
| `seed` | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). | INT | Hayır | 0 ila 2147483647 |
| `bitiş karesi` | Uzatma için hedef bitiş karesi olarak kullanılacak isteğe bağlı bir görsel. Sağlanırsa, en boy oranı 1:4 ile 4:1 arasında olmalı ve boyutları en az 128x128 piksel olmalıdır. | IMAGE | Hayır | - |

**Not:** Kaynak `video` 4 ila 55 saniye arasında bir süreye sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Uzatılmış görüntüyü içeren yeni oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
