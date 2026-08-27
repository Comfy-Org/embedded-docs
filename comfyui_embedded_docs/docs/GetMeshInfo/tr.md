# GetMeshInfo

Get Mesh Info, bir ağdaki köşe ve yüz sayılarını, ayrıca içerdiği nitelikleri (UV'ler, köşe renkleri, normaller ve dokular gibi) raporlar. Rapor düğüm üzerinde görüntülenir ve metin çıktısı olarak döndürülür; ağın kendisi ise değiştirilmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İncelenecek ağ. Düğüm, köşe ve yüz sayılarını sayar, hangi niteliklerin mevcut olduğunu tespit eder ve ağı değiştirilmeden geçirir. | MESH | Evet | — |

Not: Girdi birden çok ağ içerdiğinde (bir grup), rapor tüm grup için toplam köşe ve yüz sayılarını ve ayrıca ağ başına dökümü gösterir. Sıfır dolgulu gruplar için, ağ verilerinde saklanan öğe başına sayılar kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Orijinal ağ, hiçbir değişiklik yapılmadan geçirilir. | MESH |
| `bilgi` | Köşe sayısı, yüz sayısı ve tespit edilen nitelikleri (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map) içeren çok satırlı metin raporu. Büyük sayılar virgülle biçimlendirilir, örneğin "1,234,567 (1.23M)". Aynı metin düğüm üzerinde görüntülenir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/tr.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
