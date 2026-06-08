ModelSamplingAuraFlow düğümü, difüzyon modellerine özel bir örnekleme yapılandırması uygular ve özellikle AuraFlow model mimarileri için tasarlanmıştır. Örnekleme dağılımını ayarlayan bir kaydırma parametresi uygulayarak modelin örnekleme davranışını değiştirir. Bu düğüm, SD3 model örnekleme çerçevesinden türetilmiştir ve örnekleme süreci üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | AuraFlow örnekleme yapılandırmasının uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `kaydırma` | Örnekleme dağılımına uygulanacak kaydırma değeri (varsayılan: 1.73) | FLOAT | Evet | 0.0 - 100.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | AuraFlow örnekleme yapılandırması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/tr.md)

---
**Source fingerprint (SHA-256):** `f49367534032fb2d697d16e8197c16dc761678a5e39990993bdc864bfccea314`
