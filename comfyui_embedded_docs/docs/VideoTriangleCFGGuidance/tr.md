> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

VideoTriangleCFGGuidance düğümü, video modellerine üçgen şeklinde bir sınıflandırıcısız rehberlik ölçekleme deseni uygular. Minimum CFG değeri ile orijinal koşullandırma ölçeği arasında salınım yapan bir üçgen dalga fonksiyonu kullanarak koşullandırma ölçeğini zaman içinde değiştirir. Bu, video üretim tutarlılığını ve kalitesini iyileştirmeye yardımcı olabilecek dinamik bir rehberlik deseni oluşturur.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | MODEL | Evet | - | Üçgen CFG rehberliğinin uygulanacağı video modeli |
| `min_cfg` | FLOAT | Evet | 0.0 - 100.0 | Üçgen deseni için minimum CFG ölçek değeri (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Üçgen CFG rehberliği uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
