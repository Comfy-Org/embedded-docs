# Epsilon Ölçeklendirme

Bu belge, "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6) araştırma makalesindeki Epsilon Ölçekleme yöntemini uygular. Örnekleme işlemi sırasında tahmin edilen gürültüyü ölçekleyerek maruz kalma yanlılığını azaltmaya yardımcı olur; bu da oluşturulan görüntülerde kalite iyileşmesi sağlayabilir. Bu uygulama, pratikliği ve etkinliği nedeniyle makale tarafından önerilen "tekdüze program"ı kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Epsilon ölçekleme yamasının uygulanacağı model. | MODEL | Evet | - |
| `ölçeklendirme_faktörü` | Tahmin edilen gürültünün ölçeklendirildiği faktör. 1.0'dan büyük bir değer gürültüyü azaltırken, 1.0'dan küçük bir değer artırır (varsayılan: 1.005). | FLOAT | Hayır | 0.5 - 1.5 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme işlemine epsilon ölçekleme fonksiyonu uygulanmış, giriş modelinin yamalı bir sürümü. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/tr.md)

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
