Bu düğüm, SDXL mimarisi için özel olarak uyarlanmış bir CLIP modeli kullanarak metin girdisini kodlamak üzere tasarlanmıştır. Metin açıklamalarını işlemek için ikili bir kodlayıcı sistemi (CLIP-L ve CLIP-G) kullanır ve bu sayede daha doğru görüntü üretimi sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP model örneği. | CLIP |
| `genişlik` | Görüntü genişliğini piksel cinsinden belirtir, varsayılan 1024. | INT |
| `yükseklik` | Görüntü yüksekliğini piksel cinsinden belirtir, varsayılan 1024. | INT |
| `kırpma_g` | Kırpma alanının piksel cinsinden genişliği, varsayılan 0. | INT |
| `kırpma_y` | Kırpma alanının piksel cinsinden yüksekliği, varsayılan 0. | INT |
| `hedef_genişlik` | Çıktı görüntüsü için hedef genişlik, varsayılan 1024. | INT |
| `hedef_yükseklik` | Çıktı görüntüsü için hedef yükseklik, varsayılan 1024. | INT |
| `metin_g` | Genel sahne tanımı için küresel metin açıklaması. | STRING |
| `metin_l` | Detay tanımı için yerel metin açıklaması. | STRING |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü üretimi için gereken kodlanmış metin ve koşul bilgilerini içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/tr.md)
