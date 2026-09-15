# Voxel'den Doku İşle

Bu düğüm, ağın mevcut UV düzenini kullanarak PBR dokularını bir 3B ağ üzerine pişirir. Ağı UV uzayında rasterleştirir ve her teksel için seyrek voksel hacminden renk ve malzeme özniteliklerini örnekler; temel renk görüntüsü ile metalik ve pürüzlülük haritalarını çıktı olarak verir. Ağı UV açılımına sokmaz, bu nedenle yukarı akışta bir UV unwrap düğümü bağlanmalıdır; elde edilen görüntülerin GLB olarak kaydedilmek üzere ApplyTextureToMesh içinde aynı ağ ile eşleştirilmesi amaçlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Dokuların üzerine pişirileceği 3B ağ. Halihazırda bir UV düzenine sahip olmalıdır; yukarı akışta bir UV unwrap düğümü bağlanmalıdır. | MESH | Evet | |
| `voxel_colors` | Voksel başına renkleri ve isteğe bağlı PBR özniteliklerini (metalik ve pürüzlülük kanalları) içeren seyrek voksel hacmi. | VOXEL | Evet | |
| `texture_size` | Kare UV atlas çözünürlüğü (görünen ad: "resolution", varsayılan: 2048). | INT | Evet | 64 - 8192 |
| `reference_mesh` | İsteğe bağlı yoğun, budama öncesi ağ; örneklemeden önce her tekseli gerçek yüzeyine geri yansıtarak kaba ağlarda yüzeyli pişirmeyi ortadan kaldırır. | MESH | Hayır | |

Notlar:

- Girdi ağı UV'lere sahip olmalıdır. UV yoksa düğüm bir hata verir. UV'ler köşe noktalarıyla 1:1 olmalıdır (her köşe noktası için bir UV).
- Ağ ve voksel koordinatları bir yığın boyutu içerdiğinde, her yığın öğesi ayrı ayrı pişirilir. Bir yığın öğesinde voksel veya yüz yoksa atlanır ve onun için siyah bir doku üretilir.
- Bir yığın için `reference_mesh` sağlandığında, yalnızca tek bir ağ içermediği sürece yığın dizinine göre eşleştirilir; tek bir ağ içeriyorsa bu ağ tüm öğeler için kullanılır.
- Herhangi bir UV üçgeni tarafından kapsanmayan tekseller, doku dikişlerinin siyahı çekmemesi için en yakın kapsanan tekselden doldurulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | RGB temel renk doku haritası. Değerler 0–1 aralığında float'tır. | IMAGE |
| `metallic` | Gri tonlamalı metalik harita (float, 0–1). Voksel renkleri metalik kanal içermediğinde siyahtır. | IMAGE |
| `roughness` | Gri tonlamalı pürüzlülük haritası (float, 0–1). Voksel renkleri pürüzlülük kanalı içermediğinde siyahtır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/tr.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
