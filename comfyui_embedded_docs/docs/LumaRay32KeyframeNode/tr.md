# Luma Ray 3.2 Ana Kare

Bu düğüm, bir kılavuz görüntüyü Luma Ray 3.2 çıktı videosu zaman çizelgesinde belirli bir konuma sabitler. Bu düğümü Luma Ray 3.2 Keyframes to Video düğümünün "keyframes" girişine bağlayın ve isteğe bağlı "keyframes" girişini bağlayarak birden fazla anahtar kareyi zincirleyin.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Çıktı videosunun seçilen anına yerleştirilecek kılavuz görüntü. | IMAGE | Evet | - |
| `position` | Bu görüntünün çıktı videosunun zaman çizelgesine nasıl yerleştirileceği. | DYNAMIC_COMBO | Evet | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Bu anahtar kareyle zincirlenecek isteğe bağlı önceki anahtar kareler. | LUMA_RAY32_KEYFRAME | Hayır | - |

`position` parametresi için "Fraction of duration (0.0-1.0)" seçildiğinde, bu görüntünün çıktı videosunda nerede uygulanacağını belirleyen bir `fraction` değeri (varsayılan: 0.0, aralık: 0.0 ila 1.0, adım: 0.01) belirtebilirsiniz (0.0 = başlangıç, 1.0 = bitiş).

`position` parametresi için "Absolute time (seconds)" seçildiğinde, bu görüntünün uygulanacağı çıktı videosunun başlangıcından itibaren saniye cinsinden süreyi belirleyen bir `seconds` değeri (varsayılan: 0.0, aralık: 0.0 ila 10.0, adım: 0.1) belirtebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `keyframes` | Yeni anahtar kare ile isteğe bağlı önceki anahtar karelerin birleşimini içeren bir anahtar kare zinciri. | LUMA_RAY32_KEYFRAME |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
