# PaintMesh

PaintMesh, bir 3B ağı ve bir voxel renk alanını girdi olarak alır. Her bir köşe noktasına, alandaki en yakın voxel'in rengini atar ve sonucu çıktı ağında köşe renkleri olarak yazar. Voxel alanı boşsa, ağ varsayılan sıfır (siyah) köşe renkleriyle boyanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Boyanacak ağ. | MESH | Evet | Yok |
| `voxel_colors` | Boyama için kullanılan renk verilerini içeren voxel alanı. Alandan yalnızca temel renk RGB kanalları kullanılır. | VOXEL | Evet | Yok |

Not: Voxel alanı koordinatları bir yığın (batch) dizin kanalı içerdiğinde ve girdi ağı birden çok ağ öğesi içerdiğinde, düğüm renkleri yığındaki her ağ öğesine ayrı ayrı uygular. Örneklenen renkler, çıktı ağı için sRGB'den doğrusal RGB'ye dönüştürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Köşe renkleri uygulanmış boyanmış ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/tr.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
