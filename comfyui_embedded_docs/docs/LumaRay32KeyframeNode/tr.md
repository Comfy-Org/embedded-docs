# LumaRay32KeyframeNode

Bu düğüm, bir kılavuz görüntüyü Luma Ray 3.2 çıktı video zaman çizelgesinde belirli bir konuma sabitler. Bu düğümü Luma Ray 3.2 Ana Karelerden Videoya düğümünün "keyframes" girişine bağlayın ve isteğe bağlı "keyframes" girişini kullanarak birden fazla ana kareyi birbirine zincirleyin.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `image` | Çıktı videosunun seçilen anına yerleştirilecek kılavuz görüntü. | IMAGE | Evet | - |
| `position` | Bu görüntünün çıktı videosunun zaman çizelgesine nasıl yerleştirileceği. | COMBO | Evet | "Sürenin kesri (0.0-1.0)"<br>"Mutlak zaman (saniye)" |
| `keyframes` | Bununla zincirlenecek isteğe bağlı önceki ana kareler. | LUMA_RAY32_KEYFRAME | Hayır | - |

`position` parametresi için "Sürenin kesri (0.0-1.0)" seçildiğinde, bu görüntünün çıktı videosunda nerede uygulanacağını belirleyen bir `fraction` değeri (varsayılan: 0.0, aralık: 0.0 ile 1.0 arası, adım: 0.01) belirtebilirsiniz (0.0 = başlangıç, 1.0 = bitiş).

`position` parametresi için "Mutlak zaman (saniye)" seçildiğinde, bu görüntünün çıktı videosunun başlangıcından itibaren saniye cinsinden ne kadar süre sonra uygulanacağını belirleyen bir `seconds` değeri (varsayılan: 0.0, aralık: 0.0 ile 10.0 arası, adım: 0.1) belirtebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `keyframes` | Yeni ana kare ile isteğe bağlı önceki ana karelerin birleşimini içeren bir ana kare zinciri. | LUMA_RAY32_KEYFRAME |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
