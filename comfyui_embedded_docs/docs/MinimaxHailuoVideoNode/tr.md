# MiniMax Hailuo Video

MiniMax Hailuo-02 modelini kullanarak metin istemlerinden videolar oluşturur. İsteğe bağlı olarak, ilk kare olarak bir başlangıç görseli sağlayarak bu görselden devam eden bir video oluşturabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt_metni` | Video oluşturmayı yönlendiren metin istemi. | STRING | Evet | - |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 arası |
| `ilk_kare_görüntüsü` | Video oluşturmak için ilk kare olarak kullanılacak isteğe bağlı görsel. | IMAGE | Hayır | - |
| `prompt_optimize_edici` | Gerektiğinde oluşturma kalitesini artırmak için istemi optimize eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `süre` | Çıktı videosunun saniye cinsinden uzunluğu (varsayılan: 6). | COMBO | Hayır | `6`<br>`10` |
| `çözünürlük` | Video görüntüsünün boyutları. 1080p 1920x1080, 768p ise 1366x768'dir (varsayılan: "768P"). | COMBO | Hayır | `"768P"`<br>`"1080P"` |

**Not:** MiniMax-Hailuo-02 modelini 1080P çözünürlükte kullanırken süre 6 saniye ile sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
