# ModelÖrneklemeAuraFlow

ModelSamplingAuraFlow düğümü, özellikle AuraFlow model mimarileri için tasarlanmış özel bir örnekleme yapılandırmasını difüzyon modellerine uygular. Örnekleme dağılımını ayarlayan bir `shift` parametresi uygulayarak modelin örnekleme davranışını değiştirir. Bu düğüm, SD3 model örnekleme çerçevesinden miras alır ve örnekleme süreci üzerinde ince ayar kontrolü sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | AuraFlow örnekleme yapılandırmasının uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `shift` | Örnekleme dağılımına uygulanacak kaydırma değeri. Varsayılan: 1.73. Adım: 0.01. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | AuraFlow örnekleme yapılandırması uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/tr.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
