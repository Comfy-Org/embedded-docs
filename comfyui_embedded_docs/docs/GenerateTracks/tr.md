# GenerateTracks

`GenerateTracks` düğümü, video oluşturma için birden fazla paralel hareket yolu oluşturur. Başlangıç noktasından bitiş noktasına bir ana yol tanımlar ve bu yola paralel, eşit aralıklarla yerleştirilmiş bir dizi track üretir. Yolun şeklini (düz çizgi veya Bezier eğrisi), üzerindeki hareket hızını ve track'lerin hangi karelerde görünür olacağını kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Video karesinin piksel cinsinden genişliği. Varsayılan değer 832'dir. | INT | Evet | 16 - 4096 |
| `height` | Video karesinin piksel cinsinden yüksekliği. Varsayılan değer 480'dir. | INT | Evet | 16 - 4096 |
| `start_x` | Başlangıç konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `start_y` | Başlangıç konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `end_x` | Bitiş konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `end_y` | Bitiş konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `num_frames` | Track konumlarının oluşturulacağı toplam kare sayısı. Varsayılan değer 81'dir. | INT | Evet | 1 - 1024 |
| `num_tracks` | Oluşturulacak paralel track sayısı. Varsayılan değer 5'tir. | INT | Evet | 1 - 100 |
| `track_spread` | Track'ler arasındaki normalleştirilmiş mesafe. Track'ler hareket yönüne dik olarak yayılır. Varsayılan değer 0.025'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `bezier` | Orta noktayı kontrol noktası olarak kullanarak Bezier eğrisi yolunu etkinleştirir. Varsayılan değer False'tur. | BOOLEAN | Evet | True / False |
| `mid_x` | Bezier eğrisi için normalleştirilmiş X kontrol noktası. Yalnızca `bezier` etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `mid_y` | Bezier eğrisi için normalleştirilmiş Y kontrol noktası. Yalnızca `bezier` etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `interpolation` | Yol boyunca hareketin zamanlamasını/hızını kontrol eder. Varsayılan değer "linear"dır. "constant" ile tüm noktalar başlangıç konumunda kalır. | COMBO | Evet | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Görünür kareleri belirtmek için isteğe bağlı maske. | MASK | Hayır | - |

**Not:** `mid_x` ve `mid_y` parametreleri yalnızca `bezier` parametresi `True` olarak ayarlandığında kullanılır. `bezier` `False` olduğunda, yol başlangıç noktasından bitiş noktasına düz bir çizgidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `TRACKS` | Tüm karelerdeki tüm track'ler için oluşturulan yol koordinatlarını ve görünürlük bilgilerini içeren bir tracks nesnesi. | TRACKS |
| `track_length` | Track'lerin oluşturulduğu kare sayısıdır ve girişteki `num_frames` değeriyle eşleşir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/tr.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
