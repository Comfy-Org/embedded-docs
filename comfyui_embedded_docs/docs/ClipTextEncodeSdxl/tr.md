> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/tr.md)

Bu düğüm, SDXL mimarisi için özelleştirilmiş bir CLIP modeli kullanarak metin girişini kodlamak üzere tasarlanmıştır. Metin açıklamalarını işlemek için çift kodlayıcılı bir sistem (CLIP-L ve CLIP-G) kullanarak daha doğru görüntü oluşturma sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `clip` | CLIP | Metin kodlama için kullanılan CLIP model örneği. |
| `width` | INT | Görüntü genişliğini piksel cinsinden belirtir, varsayılan 1024. |
| `height` | INT | Görüntü yüksekliğini piksel cinsinden belirtir, varsayılan 1024. |
| `crop_w` | INT | Kırpma alanının genişliği (piksel), varsayılan 0. |
| `crop_h` | INT | Kırpma alanının yüksekliği (piksel), varsayılan 0. |
| `target_width` | INT | Çıktı görüntüsü için hedef genişlik, varsayılan 1024. |
| `target_height` | INT | Çıktı görüntüsü için hedef yükseklik, varsayılan 1024. |
| `text_g` | STRING | Genel sahne açıklaması için global metin açıklaması. |
| `text_l` | STRING | Detay açıklaması için lokal metin açıklaması. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Görüntü oluşturma için gereken kodlanmış metin ve koşullu bilgileri içerir. |