# QwenImageEditApi

Bu düğüm, Qwen-Image 3.0 modellerini kullanarak bir metin istemi rehberliğinde en fazla 3 referans görüntüsünü düzenler veya birleştirir. Metin istemini ve referans görüntülerini siz sağlarsınız; düğüm, oluşturulan sonucu bir veya daha fazla görüntü olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bu seçim ayrıca metin istemini, en fazla 3 referans görüntü girdisini ve isteğe bağlı bir negatif istemi de içerir. | COMBO | Evet | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Çıktı çözünürlüğü. "match input" ilk referans görüntüsünün boyutunu yeniden kullanır, "auto" modelin aynı en-boy oranına sahip bir boyut seçmesini sağlar, "custom" açık bir genişlik ve yükseklik belirler. | COMBO | Evet | "match input"<br>"auto"<br>"custom" |
| `n` | Oluşturulacak görüntü sayısı, bir küme (batch) olarak döndürülür. (varsayılan: 1) | INT | Hayır | 1 ile 6 arası |
| `seed` | Üretim için kullanılacak tohum (seed). (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |
| `prompt_extend` | İstem yapay zeka yardımıyla zenginleştirilsin mi. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulan filigran eklensin mi. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Kısıtlamalar

- Metin istemi zorunludur ve en az bir karakter içermelidir.
- En fazla 3 referans görüntüsü desteklenir; daha fazlası sağlanırsa bir hata oluşur (küme halindeki bir girdi, her görüntü için bir kez sayılır).
- `size` "custom" olarak ayarlandığında, açık genişlik ve yükseklik değerleri sağlanmalı ve doğrulanmalıdır.
- `size` "match input" olarak ayarlandığında, ilk referans görüntüsünün boyutları kullanıldığı için en az bir referans görüntüsü gereklidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| IMAGE | Oluşturulan görüntü veya görüntüler, bir küme olarak döndürülür. En fazla `n` görüntü döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
