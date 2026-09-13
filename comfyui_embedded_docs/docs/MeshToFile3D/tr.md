# 3B Dosyası Oluştur (Mesh'ten)

Bu düğüm, bir mesh'i Save 3D veya Preview 3D düğümlerine aktarılabilecek bir GLB dosya nesnesine serileştirir. UV'ler, renkler, normaller, doku, normal/occlusion/emissive haritaları ve malzeme ayarları dahil olmak üzere tüm mesh verilerini taşır. Çok öğeli bir toplu işlemin yalnızca ilk öğesi kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | UV'ler, renkler, normaller, doku, normal/occlusion/emissive haritaları ve malzeme dahil olmak üzere GLB dosyasına dönüştürülecek mesh. Toplu işlem başına yalnızca bir öğe desteklenir; bir toplu işlem birden fazla öğe içeriyorsa ilk öğe kullanılır. | MESH | Evet | Tek mesh |

Not: Düğüm, toplu işlem başına yalnızca bir öğeyi destekler. Girdi mesh'inin toplu işleminde birden fazla öğe varsa bir uyarı günlüğe kaydedilir ve ilk öğe kullanılır. Mesh en az bir köşe noktası ve bir yüz içermelidir; boş bir mesh hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Diğer 3D düğümleri tarafından kaydedilmeye veya önizlenmeye hazır, serileştirilmiş mesh'i içeren bir GLB (glTF Binary) dosya nesnesi. | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
