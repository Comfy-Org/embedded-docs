# Uyarlanabilir Projeksiyonlu Kılavuzluk

The APG (Adaptive Projected Guidance) node modifies the sampling process by adjusting how guidance is applied during diffusion. It separates the guidance vector into parallel and orthogonal components relative to the conditional output, allowing for more controlled image generation. The node provides parameters to scale the guidance, normalize its magnitude, and apply momentum for smoother transitions between diffusion steps.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Uyarlanabilir yansıtmalı rehberliğin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `eta` | Paralel rehberlik vektörünün ölçeğini kontrol eder. 1 ayarında varsayılan CFG davranışı (varsayılan: 1.0). | FLOAT | Evet | -10.0 ila 10.0 |
| `norm_threshold` | Rehberlik vektörünü bu değere normalize eder, 0 ayarında normalizasyon devre dışıdır (varsayılan: 5.0). | FLOAT | Evet | 0.0 ila 50.0 |
| `momentum` | Difüzyon sırasında rehberliğin hareketli ortalamasını kontrol eder, 0 ayarında devre dışıdır (varsayılan: 0.0). | FLOAT | Evet | -5.0 ila 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine uyarlanabilir yansıtmalı rehberlik uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/tr.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
