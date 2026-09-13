# Mesh Bilgisini Al

Get Mesh Info, bir mesh'teki vertex ve face sayısını, ayrıca içerdiği öznitelikleri (UV'ler, vertex renkleri, normaller ve dokular gibi) raporlar. Rapor düğümde görüntülenir ve bir metin çıktısı olarak döndürülür; mesh'in kendisi ise değişmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | İncelenecek mesh. Düğüm, vertex ve face'lerini sayar, hangi özniteliklerin mevcut olduğunu algılar ve mesh'i değişmeden geçirir. | MESH | Evet | — |

Not: Girdi birden çok mesh içerdiğinde (bir toplu işlem), rapor tüm toplu işlem için toplam vertex ve face sayılarını ve ayrıca mesh başına bir dökümü gösterir. Sıfırla doldurulmuş toplu işlemlerde, mesh verisinde saklanan öğe başına sayımlar kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Orijinal mesh, herhangi bir değişiklik yapılmadan geçirilir. | MESH |
| `info` | Vertex sayısı, face sayısı ve algılanan öznitelikleri (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map) içeren çok satırlı bir metin raporu. Doku benzeri öznitelikler, yükseklik × genişlik boyutlarıyla gösterilir. Büyük sayımlar virgülle biçimlendirilir; örneğin "1,234,567 (1.23M)" veya "12,345 (12.3K)". Aynı metin düğümde görüntülenir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/tr.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
