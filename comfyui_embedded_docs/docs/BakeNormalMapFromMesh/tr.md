# BakeNormalMapFromMesh

Bu düğüm, yüksek poli bir ağdan düşük poli ağın UV düzenine teğet uzayı normal haritası pişirir; sadeleştirme sırasında kaybolan yüzey detayını yakalar. UV açılmış düşük poli ağı ve türetildiği yüksek poli ağı bağlayın; düğüm, Apply Texture To Mesh düğümünün `normal_map` girdisine hazır bir görüntü çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Pişirilen detayı alan UV açılmış düşük poli ağ. Mevcut UV koordinatları olmalıdır; düğüm asla açma işlemi yapmaz. | MESH | Evet | — |
| `high_poly` | Yüzey detayı düşük poli ağın UV düzenine pişirilen yüksek poli ağ. | MESH | Evet | — |
| `resolution` | Kare çıktı normal haritasının piksel cinsinden kenar uzunluğu (varsayılan: 1024). | INT | Evet | 64 to 8192 (step 64) |
| `cage_distance` | Yüzey arama bandı, sınırlayıcı kutu köşegeninin bir kesri olarak. Yoğun sadeleştirme altında hatalı/eksik bölgeler için artırın; boşluklar arasında yakalıyorsa azaltın. Varsayılan: 0.05. | FLOAT | Evet | 0.001 to 0.5 (step 0.001) |
| `ignore_backfaces` | Tekselden uzağa bakan yüksek poli yüzeyleri atla; böylece yarıklar/kapalı alanlar karşı duvarı yakalamaz. Yalnızca yüksek poli sargı yönü tutarsızsa devre dışı bırakın. Varsayılan: true. | BOOLEAN | Evet | true / false |

Not: `low_poly` UV koordinatlarına sahip olmalıdır. Yoksa düğüm hata verir çünkü mevcut UV düzenine pişirir ve ağı açmaz. `low_poly` bir küme (batch) olduğunda, her öğe sırayla pişirilir; `high_poly` yalnızca bir öğe içeriyorsa, bu öğe kümedeki her öğe için yeniden kullanılır. Kümedeki boş ağlar bir uyarıyla atlanır ve düz orta gri (0.5) normal harita üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `normal_map` | Pişirilmiş teğet uzayı normal haritası (glTF/OpenGL +Y kuralı), [0,1] değerlerine sahip kare çözünürlük × çözünürlük RGB görüntüsü. Apply Texture To Mesh düğümünün `normal_map` girdisine bağlayın. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/tr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
