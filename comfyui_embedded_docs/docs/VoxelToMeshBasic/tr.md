> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/tr.md)

VoxelToMeshBasic düğümü, 3B voksel verilerini mesh geometrisine dönüştürür. Voksel hacimlerini işleyerek, hacmin hangi kısımlarının ortaya çıkan mesh içinde katı yüzeyler haline geleceğini belirlemek için bir eşik değeri uygular. Düğüm, 3B renderlama ve modelleme için kullanılabilecek köşe ve yüzler içeren eksiksiz bir mesh yapısı çıktısını verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Evet | - | Mesh'e dönüştürülecek 3B voksel verisi |
| `threshold` | FLOAT | Evet | -1.0 - 1.0 | Hangi voksellerin mesh yüzeyinin parçası haline geleceğini belirlemek için kullanılan eşik değeri (varsayılan: 0.6) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MESH` | MESH | Köşe ve yüzler içeren oluşturulmuş 3B mesh |