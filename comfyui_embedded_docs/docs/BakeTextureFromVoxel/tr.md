# BakeTextureFromVoxel

Bu düğüm, PBR dokularını, mesh'in mevcut UV yerleşimini kullanarak 3B bir mesh üzerine işler. Her tekselde, seyrek bir voksel hacminden renk ve malzeme özniteliklerini örnekler ve temel renk görüntüsü ile metalik ve pürüzlülük haritalarını çıktı olarak verir. Mesh'i UV açılımı yapmaz, bu nedenle yukarı akışta bir UV açılım düğümünün bağlı olması gerekir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Dokuların işleneceği 3B mesh. Önceden bir UV yerleşimine sahip olmalıdır; yukarı akışta bir UV açılım düğümü bağlı olmalıdır. | MESH | Evet | |
| `voxel_colors` | Voksel başına renkler ve isteğe bağlı PBR öznitelikleri (metalik ve pürüzlülük kanalları) içeren seyrek voksel hacmi. | VOXEL | Evet | |
| `texture_size` | Kare UV atlas çözünürlüğü (görünen ad: "resolution", varsayılan: 2048). | INT | Evet | 64 ila 8192 |
| `reference_mesh` | İsteğe bağlı yoğun, sadeleştirme öncesi mesh; örneklemeden önce her tekseli gerçek yüzeyine geri yansıtarak kaba meshlerde fasetli dokulama oluşmasını önler. | MESH | Hayır | |

Notlar:

- Girdi mesh UV'lere sahip olmalıdır. UV'ler yoksa düğüm bir hata verir. UV'ler, köşelerle birebir eşleşmelidir (her köşe için bir UV).
- Mesh ve voksel koordinatları bir batch boyutu içerdiğinde, her batch öğesi ayrı ayrı işlenir. Bir batch öğesinde voksel veya yüz yoksa, öğe atlanır ve onun için siyah bir doku üretilir.
- Bir batch için `reference_mesh` sağlandığında, tek bir mesh içermediği sürece batch diziniyle eşleştirilir; bu durumda bu mesh tüm öğeler için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | RGB temel renk doku haritası. Değerler 0–1 aralığında float'tır. | IMAGE |
| `metallic` | Gri tonlamalı metalik harita (float, 0–1). Voksel renkleri bir metalik kanal içermediğinde siyah. | IMAGE |
| `roughness` | Gri tonlamalı pürüzlülük haritası (float, 0–1). Voksel renkleri bir pürüzlülük kanalı içermediğinde siyah. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/tr.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
