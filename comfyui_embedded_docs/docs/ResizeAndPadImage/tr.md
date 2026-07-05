# Yeniden Boyutlandır ve Doldur Görsel

ResizeAndPadImage düğümü, bir görüntüyü orijinal en-boy oranını koruyarak belirtilen boyutlara sığacak şekilde yeniden boyutlandırır. Görüntüyü hedef genişlik ve yüksekliğe sığacak şekilde orantılı olarak küçültür, ardından kalan boş alanı doldurmak için kenarlara dolgu ekler. Dolgu rengi ve enterpolasyon yöntemi, dolgu alanlarının görünümünü ve yeniden boyutlandırma kalitesini kontrol etmek için özelleştirilebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Yeniden boyutlandırılacak ve doldurulacak giriş görüntüsü | IMAGE | Evet | - |
| `hedef_genişlik` | Çıktı görüntüsünün istenen genişliği (varsayılan: 512) | INT | Evet | 1 ile MAX_RESOLUTION |
| `hedef_yükseklik` | Çıktı görüntüsünün istenen yüksekliği (varsayılan: 512) | INT | Evet | 1 ile MAX_RESOLUTION |
| `dolgu_rengi` | Yeniden boyutlandırılmış görüntünün etrafındaki dolgu alanları için kullanılacak renk (varsayılan: "white") | COMBO | Evet | "white"<br>"black" |
| `enterpolasyon` | Görüntüyü yeniden boyutlandırmak için kullanılan enterpolasyon yöntemi (varsayılan: "area") | COMBO | Evet | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Yeniden boyutlandırılmış ve doldurulmuş çıktı görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/tr.md)

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`
