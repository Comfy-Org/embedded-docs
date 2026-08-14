# ModelAttentionBackend

Bu düğüm, bir modelin dikkat hesaplamaları için hangi dikkat arka ucunu (backend) kullanacağını seçmenizi sağlar. Modelin bir kopyasını oluşturur ve seçtiğiniz dikkat işlevini değiştirir; bu, performansı veya davranışı etkileyebilir. Seçilen arka uç mevcut değilse, otomatik olarak PyTorch dikkatine geri döner ve bir uyarı günlüğü kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Seçilen dikkat arka ucunun uygulanacağı model. | MODEL | Evet |  |
| `attention` | Kullanılacak dikkat arka ucu (varsayılan: "pytorch attention"). Seçilen arka uç kullanılamıyorsa, PyTorch dikkati yedek olarak kullanılır. | STRING | Evet | "pytorch attention"<br>"comfy kitchen attention" |

Not: "comfy kitchen attention" seçeneği yalnızca comfy kitchen int8 dikkat modülü mevcut ortamda kullanılabilir olduğunda listelenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Seçilen dikkat arka ucu uygulanmış giriş modelinin bir kopyası. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/tr.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
