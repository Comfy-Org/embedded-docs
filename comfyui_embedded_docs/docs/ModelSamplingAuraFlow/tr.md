# ModelÖrneklemeAuraFlow

ModelSamplingAuraFlow düğümü, difüzyon modellerine özelleşmiş bir örnekleme yapılandırması uygular; bu yapılandırma özellikle AuraFlow model mimarileri için tasarlanmıştır. Modelin örnekleme davranışını, örnekleme dağılımını ayarlayan bir kaydırma değeri uygulayarak değiştirir. Bu düğüm, SD3 model örnekleme çerçevesinden devralır ve örnekleme süreci üzerinde ince kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | AuraFlow örnekleme yapılandırmasının uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `kaydırma` | Örnekleme dağılımına uygulanacak kaydırma değeri (varsayılan: 1.73, adım: 0.01) | FLOAT | Evet | 0.0 - 100.0 |
| `sampling` | Model yamalanırken kullanılan örnekleme modu (varsayılan: "flow"). Gelişmiş seçenek olarak işaretlenmiştir. | COMBO | Hayır | "flow"<br>"img_to_img_velocity" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | AuraFlow örnekleme yapılandırması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/tr.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
