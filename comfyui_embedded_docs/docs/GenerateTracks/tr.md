# GenerateTracks

`GenerateTracks` düğümü, video oluşturma için birden fazla paralel hareket yolu oluşturur. Bir başlangıç noktasından bitiş noktasına bir ana yol tanımlar, ardından bu yola paralel, eşit aralıklarla yerleştirilmiş bir dizi iz (track) üretir. Yolun şeklini (düz çizgi veya Bezier eğrisi), boyunca hareket hızını ve izlerin hangi karelerde görüneceğini kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Video karesinin piksel cinsinden genişliği. Varsayılan değer 832'dir. | INT | Evet | 16 - 4096 |
| `yükseklik` | Video karesinin piksel cinsinden yüksekliği. Varsayılan değer 480'dir. | INT | Evet | 16 - 4096 |
| `başlangıç_x` | Başlangıç konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `başlangıç_y` | Başlangıç konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_x` | Bitiş konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_y` | Bitiş konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `kare_sayısı` | İz konumlarının oluşturulacağı toplam kare sayısı. Varsayılan değer 81'dir. | INT | Evet | 1 - 1024 |
| `iz_sayısı` | Oluşturulacak paralel iz sayısı. Varsayılan değer 5'tir. | INT | Evet | 1 - 100 |
| `iz_aralığı` | İzler arasındaki normalleştirilmiş mesafe. İzler, hareket yönüne dik olarak yayılır. Varsayılan değer 0.025'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `bezier` | Orta noktayı kontrol noktası olarak kullanarak Bezier eğrisi yolunu etkinleştirir. Varsayılan değer False'dur. | BOOLEAN | Evet | True / False |
| `orta_x` | Bezier eğrisi için normalleştirilmiş X kontrol noktası. Yalnızca 'bezier' etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `orta_y` | Bezier eğrisi için normalleştirilmiş Y kontrol noktası. Yalnızca 'bezier' etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `enterpolasyon` | Yol boyunca hareketin zamanlamasını/hızını kontrol eder. Varsayılan değer "linear"dır. | COMBO | Evet | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `iz_maskesi` | Görünür kareleri belirtmek için isteğe bağlı maske. | MASK | Hayır | - |

**Not:** `mid_x` ve `mid_y` parametreleri yalnızca `bezier` parametresi `True` olarak ayarlandığında kullanılır. `bezier` `False` olduğunda, yol başlangıç noktasından bitiş noktasına düz bir çizgidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `iz_uzunluğu` | Oluşturulan yol koordinatlarını ve tüm karelerdeki tüm izler için görünürlük bilgilerini içeren bir izler nesnesi. | TRACKS |
| `iz_uzunluğu` | İzlerin oluşturulduğu kare sayısı, girdi `kare_sayısı` ile eşleşir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/tr.md)

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
