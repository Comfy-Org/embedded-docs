> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/tr.md)

VoxelToMeshBasic düğümü, belirtilen bir eşik değerinde yüzey çıkararak 3B voxel verilerini ağ geometrisine dönüştürür. Girişteki her voxel ızgarasını işler ve 3B ağ temsili oluşturan köşeler ve yüzeyler üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `voksel` | VOXEL | Evet | - | Ağ geometrisine dönüştürülecek giriş voxel verisi |
| `eşik` | FLOAT | Evet | -1.0 ile 1.0 arası | Yüzey çıkarma için eşik değeri (varsayılan: 0.6) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `MESH` | MESH | Tüm giriş voxel ızgaralarından birleştirilmiş köşeler ve yüzeyler içeren oluşturulan 3B ağ |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
