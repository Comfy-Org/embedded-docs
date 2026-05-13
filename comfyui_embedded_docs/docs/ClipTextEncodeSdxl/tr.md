> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/tr.md)

Bu düğüm, SDXL mimarisi için özel olarak uyarlanmış bir CLIP modeli kullanarak metin girdisini kodlamak üzere tasarlanmıştır. Metin açıklamalarını işlemek için ikili bir kodlayıcı sistemi (CLIP-L ve CLIP-G) kullanır ve bu sayede daha doğru görüntü üretimi sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `clip` | CLIP | Metin kodlama için kullanılan CLIP model örneği. |
| `width` | INT | Görüntü genişliğini piksel cinsinden belirtir, varsayılan 1024. |
| `height` | INT | Görüntü yüksekliğini piksel cinsinden belirtir, varsayılan 1024. |
| `crop_w` | INT | Kırpma alanının piksel cinsinden genişliği, varsayılan 0. |
| `crop_h` | INT | Kırpma alanının piksel cinsinden yüksekliği, varsayılan 0. |
| `target_width` | INT | Çıktı görüntüsü için hedef genişlik, varsayılan 1024. |
| `target_height` | INT | Çıktı görüntüsü için hedef yükseklik, varsayılan 1024. |
| `text_g` | STRING | Genel sahne tanımı için küresel metin açıklaması. |
| `text_l` | STRING | Detay tanımı için yerel metin açıklaması. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `CONDITIONING` | CONDITIONING | Görüntü üretimi için gereken kodlanmış metin ve koşul bilgilerini içerir. |