> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/tr.md)

PrimitiveBoundingBox düğümü, konumu ve boyutuyla tanımlanan basit bir dikdörtgen alan oluşturur. Sol üst köşe için X ve Y koordinatlarını, genişlik ve yükseklik değerlerini alır ve iş akışındaki diğer düğümler tarafından kullanılabilecek bir sınırlayıcı kutu veri yapısı çıktısı verir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `x` | INT | Evet | 0 ila 8192 | Sınırlayıcı kutunun sol üst köşesinin X koordinatı (varsayılan: 0). |
| `y` | INT | Evet | 0 ila 8192 | Sınırlayıcı kutunun sol üst köşesinin Y koordinatı (varsayılan: 0). |
| `genişlik` | INT | Evet | 1 ila 8192 | Sınırlayıcı kutunun genişliği (varsayılan: 512). |
| `yükseklik` | INT | Evet | 1 ila 8192 | Sınırlayıcı kutunun yüksekliği (varsayılan: 512). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `bounding_box` | BOUNDING_BOX | Tanımlanan dikdörtgenin `x`, `y`, `genişlik` ve `yükseklik` özelliklerini içeren bir veri yapısı. |

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
