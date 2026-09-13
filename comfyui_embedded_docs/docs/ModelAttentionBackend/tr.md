# Model Dikkat Arka Ucu

Bu düğüm, bir model için yoğun attention uygulamasını seçer, modeli klonlar, seçilen arka ucu uygular ve yamalanmış klonu döndürür. Block Sparse Attention ile kullanıldığında, bu arka uç seyrek attention etkin olmadığında veya desteklenmediğinde kullanılır. Seçilen arka uç kullanılamıyorsa, düğüm otomatik olarak PyTorch attention'a geri döner.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamalanacak model. | MODEL | Evet |  |
| `dikkat` | Uygulanacak yoğun attention arka ucu. Comfy Kitchen attention, nicemlenmiş INT8 attention kullanır ve yalnızca Nvidia ve AMD GPU'larda kullanılabilir. Varsayılan: "pytorch attention". Seçilen arka uç kullanılamıyorsa, geri dönüş olarak PyTorch attention kullanılır. | COMBO | Evet | "pytorch attention"<br>"comfy kitchen attention" |

Not: "comfy kitchen attention" seçeneği yalnızca mevcut ortamda Comfy Kitchen INT8 attention modülü kullanılabilir olduğunda listelenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Seçilen attention arka ucu uygulanmış girdi modelinin bir klonu. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/tr.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
