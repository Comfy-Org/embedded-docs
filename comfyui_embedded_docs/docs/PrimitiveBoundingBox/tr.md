# Sınır Kutusu

PrimitiveBoundingBox düğümü, konumu ve boyutuyla tanımlanan basit bir dikdörtgen alan oluşturur. Sol üst köşe için X ve Y koordinatlarını genişlik ve yükseklik değerleriyle birlikte alır ve bir iş akışındaki diğer düğümler tarafından kullanılabilen bir sınırlayıcı kutu veri yapısı çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `x` | Sınırlayıcı kutunun sol üst köşesinin X koordinatı (varsayılan: 0). | INT | Evet | 0 to 8192 |
| `y` | Sınırlayıcı kutunun sol üst köşesinin Y koordinatı (varsayılan: 0). | INT | Evet | 0 to 8192 |
| `width` | Sınırlayıcı kutunun genişliği (varsayılan: 512). | INT | Evet | 1 to 8192 |
| `height` | Sınırlayıcı kutunun yüksekliği (varsayılan: 512). | INT | Evet | 1 to 8192 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bounding_box` | Tanımlanan dikdörtgenin `x`, `y`, `width` ve `height` özelliklerini içeren bir veri yapısı. | BOUNDING_BOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/tr.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
