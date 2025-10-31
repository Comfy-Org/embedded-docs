> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/tr.md)

ResizeAndPadImage düğümü, bir görüntüyü orijinal en-boy oranını koruyarak belirtilen boyutlara sığacak şekilde yeniden boyutlandırır. Görüntüyü hedef genişlik ve yüksekliğe sığdırmak için orantılı olarak küçültür, ardından kalan boşluğu doldurmak için kenarlara dolgu ekler. Dolgu rengi ve enterpolasyon yöntemi, dolgulu alanların görünümünü ve yeniden boyutlandırma kalitesini kontrol etmek için özelleştirilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yeniden boyutlandırılacak ve dolgu eklenecek giriş görüntüsü |
| `target_width` | INT | Evet | 1 - MAX_RESOLUTION | Çıktı görüntüsünün istenen genişliği (varsayılan: 512) |
| `target_height` | INT | Evet | 1 - MAX_RESOLUTION | Çıktı görüntüsünün istenen yüksekliği (varsayılan: 512) |
| `padding_color` | COMBO | Evet | "white"<br>"black" | Yeniden boyutlandırılmış görüntünün etrafındaki dolgu alanları için kullanılacak renk |
| `interpolation` | COMBO | Evet | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | Görüntüyü yeniden boyutlandırmak için kullanılan enterpolasyon yöntemi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Yeniden boyutlandırılmış ve dolgu eklenmiş çıktı görüntüsü |