# BakeTextureFromVoxel

Bu düğüm, mesh'in mevcut UV yerleşimini kullanarak PBR dokularını bir 3D mesh üzerine pişirir. Her texel'de seyrek bir voxel hacminden renk ve malzeme özniteliklerini örnekler ve bir temel renk (base color) görüntüsü ile metaliklik ve pürüzlülük haritaları çıktısı verir. Meshi unwrap yapmaz, bu nedenle yukarı akışta bir UV unwrap düğümünün bağlanması gerekir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Dokuların pişirileceği 3D mesh. Üzerinde zaten bir UV yerleşimi bulunmalıdır; yukarı akışta bir UV unwrap düğümü bağlanmış olmalıdır. | MESH | Evet | |
| `voxel_colors` | Voxel başına renkler ve isteğe bağlı PBR öznitelikleri (metaliklik ve pürüzlülük kanalları) içeren seyrek voxel hacmi. | VOXEL | Evet | |
| `texture_size` | Kare UV atlas çözünürlüğü (görünen adı: "resolution", varsayılan: 2048). | INT | Evet | 64 ila 8192 |
| `reference_mesh` | İsteğe bağlı yoğun, decimation öncesi mesh; örneklemeden önce her texel'i gerçek yüzeyine geri yansıtır ve kaba meshlerde fasetli pişirmeyi ortadan kaldırır. | MESH | Hayır | |

Notlar:

- Girdi mesh'inde UV'ler bulunmalıdır. UV'ler yoksa düğüm bir hata verir. UV'ler köşelerle (vertex) birebir eşleşmelidir (her köşe için bir UV).
- Mesh ve voxel koordinatları bir batch boyutu içerdiğinde, her batch öğesi ayrı ayrı pişirilir. Bir batch öğesinde voxel veya yüz yoksa, bu öğe atlanır ve onun için siyah bir doku üretilir.
- Bir batch için `reference_mesh` sağlandığında, yalnızca tek bir mesh içeriyorsa tüm öğeler için o mesh kullanılır; aksi halde batch indeksiyle eşleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | RGB temel renk doku haritası. Değerler 0-1 aralığında float'tır. | IMAGE |
| `metallic` | Gri tonlamalı metaliklik haritası (float, 0-1). Voxel renkleri metaliklik kanalı içermediğinde siyah olur. | IMAGE |
| `roughness` | Gri tonlamalı pürüzlülük haritası (float, 0-1). Voxel renkleri pürüzlülük kanalı içermediğinde siyah olur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/tr.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
