# BakeNormalMapFromMesh

Bu düğüm, yüksek poligonlu (high-poly) bir ağdan, düşük poligonlu (low-poly) ağın UV yerleşimine teğet uzay normal haritası işleyerek sadeleştirme sırasında kaybolan yüzey detaylarını yakalar. UV açılmış düşük poligonlu ağı ve türetildiği yüksek poligonlu ağı bağlayın; düğüm, Apply Texture To Mesh'in `normal_map` girdisine hazır bir görüntü çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Pişirilen detayı alan, UV açılmış düşük poligonlu ağ. Mevcut UV koordinatlarına sahip olmalıdır; düğüm asla UV açmaz. | MESH | Evet | — |
| `high_poly` | Yüzey detayı, düşük poligonlu ağın UV yerleşimine pişirilen yüksek poligonlu ağ. | MESH | Evet | — |
| `resolution` | Kare çıktı normal haritasının piksel cinsinden kenar uzunluğu (varsayılan: 1024). | INT | Evet | 64 ile 8192 (step 64) |
| `cage_distance` | Sınırlayıcı kutu köşegeninin bir kesri olarak yüzey arama bandı. Yoğun sadeleştirme altında hatalı/eksik bölgeler için artırın; boşluklar arasından yakalıyorsa azaltın. Varsayılan: 0.05. | FLOAT | Evet | 0.001 ile 0.5 (step 0.001) |
| `ignore_backfaces` | Tekselden uzağa bakan yüksek poligonlu yüzeyleri atlar; böylece yarıklar/kapalı alanlar karşı duvarı yakalamaz. Yalnızca yüksek poligonlu ağın sarım yönü tutarsızsa devre dışı bırakın. Varsayılan: true. | BOOLEAN | Evet | true / false |

Not: `low_poly`, UV koordinatlarına sahip olmalıdır. Eğer hiç yoksa, düğüm bir hata verir; çünkü mevcut UV yerleşimine pişirir ve ağı UV açmaz. `low_poly` bir batch olduğunda, her öğe sırayla pişirilir; `high_poly` yalnızca bir öğe içeriyorsa, bu öğe batch'teki her öğe için yeniden kullanılır. Batch'teki boş ağlar bir uyarıyla atlanır ve düz orta gri (0.5) normal haritası üretirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `normal_map` | Pişirilmiş teğet uzay normal haritası (glTF/OpenGL +Y kuralı), resolution × resolution boyutlarında kare RGB görüntü olarak, değerleri [0,1] aralığındadır. Apply Texture To Mesh'in `normal_map` girdisine bağlayın. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/tr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
