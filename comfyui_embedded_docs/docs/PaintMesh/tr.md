# Mesh Boya

PaintMesh bir 3B mesh ve bir voksel renk alanı alır. Alandaki en yakın vokselin rengini her tepe noktasına atar ve bu tepe noktası renkleri uygulanmış mesh'i döndürür. Voksel alanı boşsa, mesh varsayılan sıfır (siyah) tepe noktası renkleriyle boyanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Boyanacak mesh. | MESH | Evet | N/A |
| `voxel_colors` | Boyama için kullanılan renk verilerini içeren voksel alanı. Alandan yalnızca temel renk RGB kanalları kullanılır. | VOXEL | Evet | N/A |

Not: Voksel alanı koordinatları bir batch indeks kanalı içerdiğinde ve giriş mesh'i birden fazla mesh öğesi içerdiğinde, düğüm renkleri batch'teki her mesh öğesine ayrı ayrı uygular. Belirli bir mesh öğesinin eşleşen vokseli yoksa, varsayılan sıfır (siyah) tepe noktası renklerini alır. Örneklenen renkler, voksel alanı tam PBR verisi taşıyabileceği ancak tepe noktası renkleri için yalnızca temel renk RGB'si kullanıldığı için çıkış mesh'i için sRGB'den doğrusal RGB'ye dönüştürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Tepe noktası renkleri uygulanmış, boyanmış mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/tr.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
