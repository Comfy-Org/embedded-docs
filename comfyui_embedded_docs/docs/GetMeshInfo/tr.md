# GetMeshInfo

Get Mesh Info, bir ağdaki (mesh) köşe ve yüzey sayısını, ayrıca içerdiği nitelikleri (UV'ler, köşe renkleri, normaller ve dokular gibi) raporlar. Rapor düğüm üzerinde görüntülenir ve metin çıktısı olarak döndürülür; ağın kendisi değişmeden geçer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Denetlenecek ağ. Düğüm, köşeleri ve yüzeyleri sayar, hangi niteliklerin mevcut olduğunu tespit eder ve ağı değiştirmeden geçirir. | MESH | Evet | — |

Not: Girdi birden fazla ağ içerdiğinde (bir grup), rapor tüm grup için toplam köşe ve yüzey sayılarını ve ayrıca ağ başına dökümü gösterir. Sıfır dolgulu gruplarda, ağ verilerinde saklanan öğe başına sayılar kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Orijinal ağ, hiçbir değişiklik yapılmadan geçirilir. | MESH |
| `info` | Çok satırlı bir metin raporu: köşe sayısı, yüzey sayısı ve tespit edilen nitelikler (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Büyük sayılar virgülle biçimlendirilir, örneğin "1,234,567 (1.23M)". Aynı metin düğüm üzerinde görüntülenir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/tr.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
