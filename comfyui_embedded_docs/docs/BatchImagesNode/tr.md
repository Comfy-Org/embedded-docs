# Toplu Görseller

**Batch Images (Görüntü Toplama) Düğümü**

Batch Images düğümü, birden fazla ayrı görüntüyü tek bir toplu iş halinde birleştirir. Değişken sayıda görüntü girişi alır ve bunları tek bir toplu görüntü tensörü olarak çıktılar, böylece sonraki düğümlerde birlikte işlenmelerine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görseller` | Dinamik bir görüntü giriş listesi. Bir toplu iş halinde birleştirilmek üzere 2 ila 50 arasında görüntü ekleyebilirsiniz. Düğüm arayüzü, gerektiğinde daha fazla görüntü giriş yuvası eklemenize olanak tanır. | IMAGE | Evet | 2 ila 50 giriş |

**Not:** Düğümün çalışması için en az iki görüntü bağlamanız gerekir. İlk giriş yuvası her zaman zorunludur ve düğüm arayüzünde görünen "+" düğmesini kullanarak daha fazla yuva ekleyebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm giriş görüntülerinin üst üste istiflenmiş halini içeren tek bir toplu görüntü tensörü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/tr.md)

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`
