VideoTriangleCFGGuidance düğümü, video modellerine üçgen şeklinde bir sınıflandırıcısız rehberlik ölçekleme deseni uygular. Minimum CFG değeri ile orijinal koşullandırma ölçeği arasında salınım yapan bir üçgen dalga fonksiyonu kullanarak koşullandırma ölçeğini zaman içinde değiştirir. Bu, video üretim tutarlılığını ve kalitesini iyileştirmeye yardımcı olabilecek dinamik bir rehberlik deseni oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üçgen CFG rehberliğinin uygulanacağı video modeli | MODEL | Evet | - |
| `min_cfg` | Üçgen deseni için minimum CFG ölçek değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Üçgen CFG rehberliği uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
