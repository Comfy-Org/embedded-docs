# Luma Ray 3.2 Ana Kare

Bu düğüm, bir kılavuz görüntüyü Luma Ray 3.2 çıktı videosunun zaman çizelgesinde belirli bir konuma sabitler. Bu düğümü Luma Ray 3.2 Keyframes to Video düğümünün "keyframes" girişine bağlayın ve isteğe bağlı "keyframes" girişini bağlayarak birkaç anahtar kareyi birbirine zincirleyin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Çıktı videosunun seçilen anına yerleştirilecek kılavuz görüntü. | IMAGE | Evet | - |
| `position` | Bu görüntünün çıktı videosunun zaman çizelgesine nasıl yerleştirileceği. | DYNAMIC_COMBO | Evet | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Bu anahtar kareyle zincirlenecek isteğe bağlı önceki anahtar kareler. | LUMA_RAY32_KEYFRAME | Hayır | - |

### Sürenin Kesri (0.0-1.0) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `fraction` | Bu görüntünün çıktı videosunda nerede geçerli olacağı (0.0 = başlangıç, 1.0 = bitiş). Varsayılan: 0.0. | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

### Mutlak Zaman (saniye) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Bu görüntünün geçerli olduğu, çıktı videosunun başlangıcından itibaren saniye cinsinden zaman. Varsayılan: 0.0. | FLOAT | Evet | 0.0 ile 10.0 (step: 0.1) |

`position` parametresi, görüntünün zaman çizelgesine yerleştirilmesi için hangi değerin kullanılacağını belirler. Yalnızca seçilen seçeneğe ait alt parametre gösterilir ve kullanılır: "Fraction of duration (0.0-1.0)" için `fraction` ve "Absolute time (seconds)" için `seconds`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `keyframes` | Yeni anahtar kareyi isteğe bağlı önceki anahtar karelerle birleştiren bir anahtar kare zinciri. | LUMA_RAY32_KEYFRAME |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
