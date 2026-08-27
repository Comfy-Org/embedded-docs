# MiniMax Hailuo Video

MiniMax Hailuo-02 modelini kullanarak metin istemlerinden videolar üretir. İsteğe bağlı olarak, videonun ilk karesi olarak bir başlangıç görüntüsü sağlayabilir ve bu görüntüden devam eden bir video oluşturabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_metni` | Video üretimini yönlendiren metin istemi. | STRING | Evet | - |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 arası |
| `ilk_kare_görüntüsü` | Video üretmek için ilk kare olarak kullanılabilecek isteğe bağlı görüntü. | IMAGE | Hayır | - |
| `prompt_optimize_edici` | Gerekirse üretim kalitesini artırmak için istemi optimize eder (varsayılan: True). | BOOLEAN | Hayır | True<br>False |
| `süre` | Çıktı videosunun saniye cinsinden uzunluğu (varsayılan: 6). | COMBO | Hayır | 6<br>10 |
| `çözünürlük` | Video görüntüsünün boyutları. 1080p, 1920x1080'dir; 768p, 1366x768'dir (varsayılan: "768P"). | COMBO | Hayır | "768P"<br>"1080P" |

**Not:** `resolution` "1080P" olarak ayarlandığında, `duration` 6 saniye ile sınırlıdır. `first_frame_image` sağlanmadığında, `prompt_text` boş olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
