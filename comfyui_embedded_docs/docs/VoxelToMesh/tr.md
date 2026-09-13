# VokseldenAğa

VoxelToMesh düğümü, 3B voksel verisini belirtilen bir eşik değerinde yüzey çıkararak bir mesh geometrisine dönüştürür. Yüzey çıkarma için iki algoritma sunar: basit kutu benzeri yüzler oluşturan temel bir yöntem ve daha pürüzsüz, daha ayrıntılı mesh'ler üreten bir "surface net" yöntemi. Düğüm, girdideki her voksel ızgarasını işler ve 3B mesh gösterimini oluşturan köşe noktaları ve yüzler üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voksel` | Mesh geometrisine dönüştürülecek girdi voksel verisi | VOXEL | Evet | - |
| `algoritma` | Yüzey çıkarma için kullanılan algoritma. "surface net" daha pürüzsüz mesh'ler üretirken, "basic" basit kutu benzeri yüzler oluşturur (varsayılan: "surface net") | COMBO | Evet | `"surface net"`<br>`"basic"` |
| `eşik` | Yüzey çıkarma için eşik değeri. Değerleri bu eşiğin üzerinde olan vokseller katı kabul edilir (varsayılan: 0.6) | FLOAT | Evet | -1.0 ile 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MESH` | Tüm girdi voksel ızgaralarından gelen köşe noktaları ve yüzleri içeren oluşturulan 3B mesh. Tüm voksel ızgaraları aynı şekle sahip mesh'ler üretirse, çıktı yığılmış bir tensördür; aksi takdirde değişken uzunlukta bir toplu iş döndürülür | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`
