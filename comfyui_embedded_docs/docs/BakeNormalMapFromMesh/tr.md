# Mesh'ten Normal Haritası İşle

Bu düğüm, yüksek poligonlu bir ağdan düşük poligonlu bir ağın UV düzenine teğet uzayı normal haritası pişirir; decimation sırasında kaybolan yüzey ayrıntılarını yakalar. UV'si açılmış düşük poligonlu ağı ve onun türetildiği yüksek poligonlu ağı bağlayın; düğüm, Apply Texture To Mesh düğümünün `normal_map` girişine hazır bir görüntü çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Pişirilen ayrıntıyı alan UV'si açılmış düşük poligonlu ağ. Mevcut UV'lere sahip olmalıdır; düğüm asla UV açmaz. | MESH | Evet | — |
| `high_poly` | Yüzey ayrıntısı düşük poligonlu ağın UV düzenine pişirilen yüksek poligonlu ağ. | MESH | Evet | — |
| `resolution` | Kare çıktı normal haritasının piksel cinsinden kenar uzunluğu (varsayılan: 1024). | INT | Evet | 64 ile 8192 (adım 64) |
| `cage_distance` | Yüzey arama bandı, sınırlayıcı kutu köşegeninin bir kesri olarak. Ağır decimation altında yanlış/eksik yamalar için artırın; boşlukların karşısından yakalıyorsa azaltın. Varsayılan: 0.05. | FLOAT | Evet | 0.001 ile 0.5 (adım 0.001) |
| `ignore_backfaces` | Texel'den uzağa bakan yüksek poligonlu yüzeyleri atlayın, böylece yarıklar/kapalı alanlar karşı duvarı yakalamaz. Yalnızca yüksek poligonlu ağın sarım yönü tutarsızsa devre dışı bırakın. Varsayılan: true. | BOOLEAN | Evet | true / false |

Not: `low_poly` UV koordinatlarına sahip olmalıdır. Hiç yoksa, düğüm hata verir çünkü mevcut UV düzenine pişirir ve ağı UV açmaz. `low_poly` bir toplu (batch) olduğunda, her öğe sırayla pişirilir; `high_poly` yalnızca bir öğe içeriyorsa, bu öğe her toplu öğesi için yeniden kullanılır. Topludaki boş ağlar bir uyarıyla atlanır ve düz orta gri (0,5) normal haritası üretir. Düşük poligonlu UV'ler [0,1] aralığının dışına taşarsa, [0,1] içine eşit şekilde sığdırılır (düzen döşenmiş/UDIM göründüğünde bir uyarıyla), böylece pişirme ve Apply Texture To Mesh aynı UV'leri kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `normal_map` | Pişirilmiş teğet uzayı normal haritası (glTF/OpenGL +Y kuralı), değerleri [0,1] aralığında olan kare çözünürlük × çözünürlük RGB görüntüsü olarak. Apply Texture To Mesh düğümünün `normal_map` girişine bağlayın. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/tr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
