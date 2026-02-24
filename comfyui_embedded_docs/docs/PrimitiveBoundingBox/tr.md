> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/tr.md)

PrimitiveBoundingBox düğümü, konumu ve boyutu ile tanımlanan basit bir dikdörtgen alan oluşturur. Sol üst köşe için X ve Y koordinatlarını, genişlik ve yükseklik değerlerini alır ve bir iş akışındaki diğer düğümler tarafından kullanılabilecek bir sınırlayıcı kutu veri yapısı çıktılar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | Hayır | 0 - 8192 | Sınırlayıcı kutunun sol üst köşesinin X koordinatı (varsayılan: 0). |
| `y` | INT | Hayır | 0 - 8192 | Sınırlayıcı kutunun sol üst köşesinin Y koordinatı (varsayılan: 0). |
| `width` | INT | Hayır | 1 - 8192 | Sınırlayıcı kutunun genişliği (varsayılan: 512). |
| `height` | INT | Hayır | 1 - 8192 | Sınırlayıcı kutunun yüksekliği (varsayılan: 512). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | Tanımlanan dikdörtgenin `x`, `y`, `width` ve `height` özelliklerini içeren bir veri yapısı. |