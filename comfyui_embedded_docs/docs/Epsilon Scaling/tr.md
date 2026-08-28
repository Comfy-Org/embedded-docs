# Epsilon Ölçeklendirme

Bu düğüm, "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6) adlı araştırma makalesindeki Epsilon Ölçekleme yöntemini uygular. Örnekleme süreci sırasında öngörülen gürültüyü ölçekleyerek çalışır ve böylece maruz kalma yanlılığını azaltmaya yardımcı olur; bu da üretilen görüntülerin kalitesini artırabilir. Bu uygulama, makalenin pratikliği ve etkinliği nedeniyle önerdiği "tekdüze zamanlama" yöntemini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Epsilon ölçekleme yamasının uygulanacağı model. | MODEL | Evet | - |
| `ölçeklendirme_faktörü` | Öngörülen gürültünün ölçeklendirildiği faktör. 1.0'den büyük bir değer gürültüyü azaltırken, 1.0'den küçük bir değer artırır (varsayılan: 1.005). Bu gelişmiş bir parametredir. | FLOAT | Hayır | 0.5 - 1.5 (step: 0.001) |

Not: `scaling_factor` 0 olarak ayarlanırsa, düğüm sıfıra bölmeyi önlemek için otomatik olarak onu çok küçük bir değerle (1e-9) değiştirir. Arayüzün minimum değeri olan 0.5 normalde bunun olmasını engeller.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine epsilon ölçekleme işlevi uygulanmış giriş modelinin yamalı sürümü. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/tr.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
