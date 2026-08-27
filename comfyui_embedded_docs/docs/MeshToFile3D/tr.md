# MeshToFile3D

Bu düğüm, bir mesh'i GLB dosya nesnesine serileştirir ve bu nesne Save 3D veya Preview 3D düğümlerine aktarılabilir. UV'ler, renkler, normaller, doku, normal/occlusion/emissive haritaları ve malzeme ayarları dahil tüm mesh verilerini taşır. Çok öğeli bir grubun yalnızca ilk öğesi kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | GLB dosyasına dönüştürülecek mesh; UV'ler, renkler, normaller, doku, normal/occlusion/emissive haritaları ve malzemeyi içerir. Grup başına yalnızca bir öğe desteklenir; bir grupta birden fazla öğe varsa ilki kullanılır. | MESH | Evet | Single mesh |

Not: Bu düğüm yalnızca grup başına bir öğeyi destekler. Girdi mesh'i, grubunda birden fazla öğe içeriyorsa bir uyarı günlüğe kaydedilir ve ilk öğe kullanılır. Mesh en az bir köşe (vertex) ve bir yüz (face) içermelidir; boş bir mesh hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Serileştirilmiş meshi içeren, diğer 3D düğümleri tarafından kaydedilmeye veya önizlenmeye hazır bir GLB (glTF Binary) dosya nesnesi. | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
