> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/tr.md)

ViduExtendVideoNode, mevcut bir videonun süresini uzatmak için ek kareler oluşturur. Kaynak videoya ve isteğe bağlı bir metin istemine dayanarak kesintisiz bir devam oluşturmak için belirtilen bir AI modelini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` | Video uzatma için kullanılacak AI modeli. Bir model seçmek, o modele özgü süre ve çözünürlük ayarlarını gösterir. |
| `model.duration` | INT | Evet | 1 ila 7 | Uzatılmış videonun saniye cinsinden süresi (varsayılan: 4). Bu ayar, bir model seçildikten sonra görünür. |
| `model.resolution` | COMBO | Evet | `"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. Bu ayar, bir model seçildikten sonra görünür. |
| `video` | VIDEO | Evet | - | Uzatılacak kaynak video. |
| `prompt` | STRING | Hayır | - | Uzatılmış videonun içeriğini yönlendirmek için isteğe bağlı bir metin istemi (maksimum 2000 karakter, varsayılan: boş). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). |
| `bitiş karesi` | IMAGE | Hayır | - | Uzatma için hedef bitiş karesi olarak kullanılacak isteğe bağlı bir görsel. Sağlanırsa, en boy oranı 1:4 ile 4:1 arasında olmalı ve boyutları en az 128x128 piksel olmalıdır. |

**Not:** Kaynak `video` 4 ila 55 saniye arasında bir süreye sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Uzatılmış görüntüyü içeren yeni oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
