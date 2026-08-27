# PaintMesh

PaintMesh, bir 3B ağı (mesh) ve bir voxel renk alanını kapsar. Her tepe noktasına, alandaki en yakın voxel'in rengini atar ve sonucu çıktı ağında tepe noktası renkleri olarak yazar. Voxel alanı boşsa, ağ varsayılan sıfır (siyah) tepe noktası renkleriyle boyanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Boyanacak ağ (mesh). | MESH | Evet | N/A |
| `voxel_colors` | Boyama için renk verilerini içeren voxel alanı. Alanın yalnızca temel renk RGB kanalları kullanılır. | VOXEL | Evet | N/A |

Not: Voxel alanı koordinatları bir grup (batch) indeks kanalı içerdiğinde ve girdi ağı birden fazla ağ öğesi içerdiğinde, düğüm renkleri gruptaki her ağ öğesine ayrı ayrı uygular. Örneklenen renkler, çıktı ağı için sRGB'den doğrusal RGB'ye dönüştürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Tepe noktası renkleri uygulanmış boyanmış ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/tr.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
