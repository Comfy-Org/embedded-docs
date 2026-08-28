# VideoÜçgenCFGRehberliği

VideoTriangleCFGGuidance düğümü, bir video modeline üçgen sınıflandırıcısız yönlendirme (CFG) ölçekleme deseni uygular. `min_cfg` ile modelin orijinal koşullandırma ölçeği arasında salınan üçgen bir dalga kullanarak koşullandırma ölçeğini zaman içinde değiştirir. Bu, video üretim tutarlılığını ve kalitesini artırmaya yardımcı olabilecek dinamik bir yönlendirme deseni oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üçgen CFG yönlendirmesinin uygulanacağı video modeli | MODEL | Evet | - |
| `min_cfg` | Üçgen desen için minimum CFG ölçek değeri (varsayılan: 1.0). Bu parametre, düğüm arayüzünün gelişmiş bölümünde gösterilir. | FLOAT | Evet | 0.0 - 100.0 (step: 0.5, round: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Üçgen CFG yönlendirmesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
