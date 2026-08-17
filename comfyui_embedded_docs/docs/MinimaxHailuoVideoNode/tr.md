# MiniMax Hailuo Video

MiniMax Hailuo-02 modelini kullanarak metin istemlerinden videolar oluşturur. İsteğe bağlı olarak, videonun devam edeceği ilk kare olarak bir başlangıç görseli sağlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | Video oluşturmayı yönlendiren metin istemi. | STRING | Evet | - |
| `seed` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 |
| `first_frame_image` | Video oluşturmak için ilk kare olarak kullanılacak isteğe bağlı görsel. | IMAGE | Hayır | - |
| `prompt_optimizer` | Gerekli olduğunda oluşturma kalitesini artırmak için istemi optimize eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `duration` | Çıktı videosunun saniye cinsinden uzunluğu (varsayılan: 6). | COMBO | Hayır | `6`<br>`10` |
| `resolution` | Video görüntüsünün boyutları. 1080p 1920x1080, 768p 1366x768'dir (varsayılan: "768P"). | COMBO | Hayır | `"768P"`<br>`"1080P"` |

**Notlar:**
- `first_frame_image` sağlanmadığında `prompt_text` boş olmayan bir dize olmalıdır.
- MiniMax-Hailuo-02 modelini 1080P çözünürlükte kullanırken süre 6 saniye ile sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
