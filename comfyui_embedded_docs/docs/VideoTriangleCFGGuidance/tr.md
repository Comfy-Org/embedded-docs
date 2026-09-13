# VideoÜçgenCFGRehberliği

VideoTriangleCFGGuidance düğümü, bir video modeline üçgensel sınıflandırıcısız kılavuzlama (CFG) ölçekleme deseni uygular. Koşullandırma ölçeğini, `min_cfg` ile modelin özgün koşullandırma ölçeği arasında salınan bir üçgensel dalga kullanarak değiştirir. Bu, video oluşturma tutarlılığını ve kalitesini iyileştirmeye yardımcı olabilecek dinamik bir kılavuzlama deseni oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üçgensel CFG kılavuzlamasının uygulanacağı video modeli. | MODEL | Evet | - |
| `min_cfg` | Üçgensel desen için minimum CFG ölçek değeri. Bu parametre, düğüm arayüzünün gelişmiş bölümünde gösterilir (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 100.0 (adım: 0.5, yuvarlama: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Üçgensel CFG kılavuzlaması uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
