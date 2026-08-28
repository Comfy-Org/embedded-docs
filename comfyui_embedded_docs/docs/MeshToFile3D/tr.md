# MeshToFile3D

Bu düğüm, bir ağı (mesh) Save 3D veya Preview 3D düğümlerine aktarılabilen bir GLB dosya nesnesine seri hale getirir. UV'ler, renkler, normaller, doku, normal/ortam/emissive haritaları ve malzeme ayarları dahil tüm ağ verilerini taşır. Çok öğeli bir grubun (batch) yalnızca ilk öğesi kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | GLB dosyasına dönüştürülecek ağ; UV'ler, renkler, normaller, doku, normal/ortam/emissive haritaları ve malzeme dahildir. Grup başına yalnızca bir öğe desteklenir; grup birden fazla öğe içeriyorsa ilki kullanılır. | MESH | Evet | Tek ağ |

Not: Düğüm, grup başına yalnızca bir öğeyi destekler. Girdi ağı, grubunda birden fazla öğe içeriyorsa bir uyarı günlüğe kaydedilir ve ilk öğe kullanılır. Ağ en az bir köşe noktası ve bir yüzey içermelidir; boş bir ağ hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Seri hale getirilmiş ağı içeren, diğer 3D düğümleri tarafından kaydedilmeye veya önizlenmeye hazır bir GLB (glTF Binary) dosya nesnesi. | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
