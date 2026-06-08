PrimitiveBoundingBox düğümü, konumu ve boyutuyla tanımlanan basit bir dikdörtgen alan oluşturur. Sol üst köşe için X ve Y koordinatlarını, genişlik ve yükseklik değerlerini alır ve iş akışındaki diğer düğümler tarafından kullanılabilecek bir sınırlayıcı kutu veri yapısı çıktısı verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `x` | Sınırlayıcı kutunun sol üst köşesinin X koordinatı (varsayılan: 0). | INT | Evet | 0 ila 8192 |
| `y` | Sınırlayıcı kutunun sol üst köşesinin Y koordinatı (varsayılan: 0). | INT | Evet | 0 ila 8192 |
| `genişlik` | Sınırlayıcı kutunun genişliği (varsayılan: 512). | INT | Evet | 1 ila 8192 |
| `yükseklik` | Sınırlayıcı kutunun yüksekliği (varsayılan: 512). | INT | Evet | 1 ila 8192 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bounding_box` | Tanımlanan dikdörtgenin `x`, `y`, `genişlik` ve `yükseklik` özelliklerini içeren bir veri yapısı. | BOUNDING_BOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/tr.md)

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
