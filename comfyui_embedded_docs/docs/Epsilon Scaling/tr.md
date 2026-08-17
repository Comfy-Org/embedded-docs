# Epsilon Ölçeklendirme

Bu düğüm, "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6) araştırma makalesindeki Epsilon Ölçekleme yöntemini uygular. Örnekleme süreci sırasında tahmin edilen gürültüyü ölçekleyerek maruziyet yanlılığını (exposure bias) azaltmaya yardımcı olur; bu da üretilen görüntülerde kalitenin artmasını sağlayabilir. Bu uygulama, pratikliği ve etkinliği nedeniyle makalenin önerdiği "uniform schedule" (tekdüzen çizelge) yöntemini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Epsilon ölçekleme yamasının uygulanacağı model. | MODEL | Evet | - |
| `scaling_factor` | Tahmin edilen gürültünün ölçeklendiği faktör. 1.0'dan büyük bir değer tahmin edilen gürültüyü azaltırken, 1.0'dan küçük bir değer artırır (varsayılan: 1.005). | FLOAT | Evet | 0.5 - 1.5 (adım: 0.001) |

Not: `scaling_factor`, sıfıra bölünmeyi önlemek için sıfır değerine karşı korunur. Arayüz minimum 0.5 uygular, bu nedenle normal kullanımda bu durum gerçekleşemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine epsilon ölçekleme işlevi uygulanmış girdi modelinin yamalı (patched) bir kopyası. Orijinal model değiştirilmeden bırakılır. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/tr.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
