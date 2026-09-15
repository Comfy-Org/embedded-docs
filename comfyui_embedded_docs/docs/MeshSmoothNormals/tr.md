# Mesh Normallerini Yumuşat

Bir mesh için düzgün köşe başına normalleri hesaplayın ve bunları ekleyin. Normalleri olmayan mesh'ler, glTF görüntüleyicileri tarafından düz (yüz başına) gölgelenir; bu düğüm onların düzgün gölgelenmesini sağlar. 180'in altında bir kırışma açısıyla, eşik değerinden daha keskin kenarlar, köşeler bu kenarlar boyunca bölünerek sert tutulur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `mesh` | İşlenecek giriş mesh'i. | MESH | Evet | - |
| `crease_angle` | Dihedral açısı bu değeri (derece) aşan kenarlar sert kalır (köşeler bölünür). 180 = tamamen düzgün; daha düşük değerler keskin kenarları korur (örn. sert yüzey için ~30-60). Varsayılan: 180.0. | FLOAT | Evet | 0.0 - 180.0 (adım 1.0) |

`crease_angle` 180 veya daha yüksek olduğunda, mesh topolojisi değişmez. 180'in altına ayarlandığında, köşeler sert kenarlar boyunca bölünür; bu, köşe sayısını artırabilir. Köşeler bölündüğünde, köşe başına veriler (renkler, UV'ler ve teğetler) yeni köşe düzenine uyacak şekilde çoğaltılır ve elde edilen mesh değişken boyutlu bir toplu iş olarak yeniden oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Düzgün normal verisi eklenmiş giriş mesh'i veya bir kırışma açısı ayarlandığında bölünmüş köşeler ve normaller içeren mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/tr.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
