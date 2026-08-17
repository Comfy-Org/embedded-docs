# VideoÜçgenCFGRehberliği

VideoTriangleCFGGuidance düğümü, video modellerine üçgensel sınıflandırıcısız rehberlik (classifier-free guidance) ölçekleme deseni uygular. Minimum CFG değeri ile orijinal koşullandırma ölçeği arasında salınan üçgensel bir dalga fonksiyonu kullanarak koşullandırma ölçeğini zaman içinde değiştirir. Bu, video oluşturma tutarlılığını ve kalitesini artırmaya yardımcı olabilecek dinamik bir rehberlik deseni oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üçgensel CFG rehberliğinin uygulanacağı video modeli | MODEL | Evet | - |
| `min_cfg` | Üçgensel desen için minimum CFG ölçeği değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Üçgensel CFG rehberliği uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
