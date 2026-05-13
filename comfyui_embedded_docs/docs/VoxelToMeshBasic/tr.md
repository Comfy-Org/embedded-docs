> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/tr.md)

VoxelToMeshBasic düğümü, 3B voxel verilerini ağ geometrisine dönüştürür. Voxel hacimlerini, hacmin hangi bölümlerinin sonuçtaki ağda katı yüzey haline geleceğini belirlemek için bir eşik değeri uygulayarak işler. Düğüm, 3B görüntüleme ve modellemede kullanılabilecek, köşe noktaları ve yüzler içeren eksiksiz bir ağ yapısı çıktısı verir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `voxel` | VOXEL | Evet | - | Ağa dönüştürülecek 3B voxel verisi |
| `threshold` | FLOAT | Evet | -1.0 ile 1.0 | Hangi voxellerin ağ yüzeyinin parçası olacağını belirlemek için kullanılan eşik değeri (varsayılan: 0.6) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `MESH` | MESH | Köşe noktaları ve yüzler içeren oluşturulmuş 3B ağ |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
