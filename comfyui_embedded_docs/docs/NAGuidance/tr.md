# Normalize Edilmiş Dikkat Yönlendirmesi

NAGuidance düğümü, bir modele Normalleştirilmiş Dikkat Yönlendirmesi (Normalized Attention Guidance) uygular. Bu teknik, örnekleme süreci sırasında modelin dikkat mekanizmasını değiştirerek, damıtılmış veya hızlı (schnell) modellerle negatif istemlerin kullanılmasını sağlar ve üretimi istenmeyen kavramlardan uzaklaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Normalleştirilmiş Dikkat Yönlendirmesinin uygulanacağı model. | MODEL | Evet | - |
| `nag_scale` | Yönlendirme ölçek faktörü. Daha yüksek değerler, üretimi negatif istemden daha da uzaklaştırır. (varsayılan: 5.0) | FLOAT | Evet | 0.0 - 50.0 |
| `nag_alpha` | Normalleştirilmiş dikkat için harmanlama faktörü. 1.0 değeri orijinal dikkati tamamen değiştirirken, 0.0 değerinin hiçbir etkisi yoktur. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `nag_tau` | Normalleştirme oranını sınırlamak için kullanılan bir ölçekleme faktörü. (varsayılan: 1.5) | FLOAT | Evet | 1.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Normalleştirilmiş Dikkat Yönlendirmesi etkinleştirilmiş yamalı model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `ea3d7fea94e62c8a0784887f3df9d8a503c3dbaa552bf860bd4dde1ae576fa9c`
