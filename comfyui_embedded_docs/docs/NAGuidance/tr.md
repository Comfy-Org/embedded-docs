# Normalize Edilmiş Dikkat Yönlendirmesi

NAGuidance düğümü bir modele Normalleştirilmiş Dikkat Rehberliği uygular. Bu teknik, örnekleme işlemi sırasında modelin dikkat mekanizmasını değiştirerek üretimi istenmeyen kavramlardan uzaklaştırır ve damıtılmış veya schnell modellerle negatif istemlerin kullanılmasını mümkün kılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Normalleştirilmiş Dikkat Rehberliği uygulanacak model. | MODEL | Evet | - |
| `nag_scale` | Rehberlik ölçek faktörü. Daha yüksek değerler üretimi negatif istemden daha uzağa iter. (varsayılan: 5.0) | FLOAT | Evet | 0.0 - 50.0 |
| `nag_alpha` | Normalleştirilmiş dikkat için karıştırma faktörü. 1.0 değeri orijinal dikkatin yerini tamamen alır, 0.0 ise hiçbir etki yapmaz. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `nag_tau` | Normalleştirme oranını sınırlamak için kullanılan ölçek faktörü. (varsayılan: 1.5) | FLOAT | Evet | 1.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Normalleştirilmiş Dikkat Rehberliği etkinleştirilmiş yamalanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`
