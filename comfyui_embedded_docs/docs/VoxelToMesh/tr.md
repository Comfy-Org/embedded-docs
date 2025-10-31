> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/tr.md)

VoxelToMesh düğümü, 3B voksel verilerini farklı algoritmalar kullanarak mesh geometrisine dönüştürür. Voksel ızgaralarını işler ve 3B mesh temsilini oluşturan köşe noktaları ve yüzeyler üretir. Düğüm, birden fazla dönüştürme algoritmasını destekler ve yüzey çıkarımını kontrol etmek için eşik değerinin ayarlanmasına olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Evet | - | Mesh geometrisine dönüştürülecek giriş voksel verisi |
| `algorithm` | COMBO | Evet | "surface net"<br>"basic" | Voksel verisinden mesh dönüşümü için kullanılan algoritma |
| `threshold` | FLOAT | Evet | -1.0 - 1.0 | Yüzey çıkarımı için eşik değeri (varsayılan: 0.6) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MESH` | MESH | Köşe noktaları ve yüzeyler içeren oluşturulmuş 3B mesh |