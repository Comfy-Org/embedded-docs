VoxelToMeshBasic düğümü, belirtilen bir eşik değerinde yüzey çıkararak 3B voxel verilerini ağ geometrisine dönüştürür. Girişteki her voxel ızgarasını işler ve 3B ağ temsili oluşturan köşeler ve yüzeyler üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `voksel` | Ağ geometrisine dönüştürülecek giriş voxel verisi | VOXEL | Evet | - |
| `eşik` | Yüzey çıkarma için eşik değeri (varsayılan: 0.6) | FLOAT | Evet | -1.0 ile 1.0 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MESH` | Tüm giriş voxel ızgaralarından birleştirilmiş köşeler ve yüzeyler içeren oluşturulan 3B ağ | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
