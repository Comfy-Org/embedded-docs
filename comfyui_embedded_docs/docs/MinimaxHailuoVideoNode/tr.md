# MiniMax Hailuo Video

MiniMax Hailuo-02 modelini kullanarak metin istemlerinden videolar oluşturur. İlk kare olarak kullanılacak bir başlangıç görseli isteğe bağlı olarak sağlayabilirsiniz; bu, o görselden devam eden bir video oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_metni` | Video oluşturmayı yönlendirmek için metin istemi (varsayılan: boş). | STRING | Evet | - |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 |
| `ilk_kare_görüntüsü` | Video oluşturmak için ilk kare olarak kullanılacak isteğe bağlı görsel. | IMAGE | Hayır | - |
| `prompt_optimize_edici` | İstemi, gerektiğinde oluşturma kalitesini iyileştirmek için optimize edin (varsayılan: True). | BOOLEAN | Hayır | True<br>False |
| `süre` | Çıktı videosunun saniye cinsinden uzunluğu (varsayılan: 6). | COMBO | Hayır | 6<br>10 |
| `çözünürlük` | Video görüntüsünün boyutları. 1080p 1920x1080, 768p 1366x768'dir (varsayılan: "768P"). | COMBO | Hayır | "768P"<br>"1080P" |

**Not:** `resolution` "1080P" olarak ayarlandığında, `duration` 6 saniye ile sınırlıdır. `first_frame_image` sağlanmadığında, `prompt_text` boş olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
