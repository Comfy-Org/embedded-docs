# MeshSmoothNormals

Compute smooth per-vertex normals for a mesh and attach them. Meshes without normals are shaded flat (per-face) by glTF viewers; this node makes them shade smoothly. With a crease angle below 180, edges sharper than the threshold are kept hard by splitting vertices along them.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İşlenecek girdi ağı. | MESH | Evet | - |
| `crease_angle` | Dihedral açısı bu değeri (derece) aşan kenarlar sert kalır (köşeler bölünür). 180 = tamamen yumuşak; düşük değerler keskin kenarları korur (örn. sert yüzeyler için ~30-60). Varsayılan: 180.0. | FLOAT | Evet | 0.0 ila 180.0 (adım 1.0) |

`crease_angle` 180 veya daha yüksek olduğunda ağ topolojisi değişmez. 180'in altına ayarlandığında, köşeler sert kenarlar boyunca bölünür ve bu da köşe sayısını artırabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `mesh` | Yumuşak normal verisi eklenmiş girdi ağı veya bir katlama açısı ayarlandığında bölünmüş köşeler ve normaller içeren ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/tr.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
