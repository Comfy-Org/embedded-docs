> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/tr.md)

Bu düğüm, SDXL mimarisi için özelleştirilmiş bir CLIP modeli kullanarak metin girişini kodlamak üzere tasarlanmıştır. Metin açıklamalarını işlemek için çift kodlayıcılı bir sistem (CLIP-L ve CLIP-G) kullanarak daha doğru görüntü oluşturma sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `clip` | CLIP | Metin kodlama için kullanılan CLIP model örneği. |
| `genişlik` | INT | Görüntü genişliğini piksel cinsinden belirtir, varsayılan 1024. |
| `yükseklik` | INT | Görüntü yüksekliğini piksel cinsinden belirtir, varsayılan 1024. |
| `kırpma_g` | INT | Kırpma alanının genişliği (piksel), varsayılan 0. |
| `kırpma_y` | INT | Kırpma alanının yüksekliği (piksel), varsayılan 0. |
| `hedef_genişlik` | INT | Çıktı görüntüsü için hedef genişlik, varsayılan 1024. |
| `hedef_yükseklik` | INT | Çıktı görüntüsü için hedef yükseklik, varsayılan 1024. |
| `metin_g` | STRING | Genel sahne açıklaması için global metin açıklaması. |
| `metin_l` | STRING | Detay açıklaması için lokal metin açıklaması. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Görüntü oluşturma için gereken kodlanmış metin ve koşullu bilgileri içerir. |