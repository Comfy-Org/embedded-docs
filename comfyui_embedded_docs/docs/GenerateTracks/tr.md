# GenerateTracks

`GenerateTracks` düğümü, video oluşturma için birden fazla paralel hareket yolu (track) oluşturur. Ana yolu bir başlangıç konumundan bir bitiş konumuna tanımlar ve ardından bu yola paralel, eşit aralıklarla yerleştirilmiş bir dizi track üretir. Yolun şeklini (düz çizgi veya Bezier eğrisi), yol boyunca hareket hızını ve track'lerin hangi karelerde görünür olacağını kontrol edebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Video karesinin piksel cinsinden genişliği. Varsayılan değer 832'dir. | INT | Evet | 16 - 4096 |
| `yükseklik` | Video karesinin piksel cinsinden yüksekliği. Varsayılan değer 480'dir. | INT | Evet | 16 - 4096 |
| `başlangıç_x` | Başlangıç konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `başlangıç_y` | Başlangıç konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 0.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_x` | Bitiş konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_y` | Bitiş konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 1.0'dır. | FLOAT | Evet | 0.0 - 1.0 |
| `kare_sayısı` | Track konumlarının üretileceği toplam kare sayısı. Varsayılan değer 81'dir. | INT | Evet | 1 - 1024 |
| `iz_sayısı` | Üretilecek paralel track sayısı. Varsayılan değer 5'tir. | INT | Evet | 1 - 100 |
| `iz_aralığı` | Track'ler arasındaki normalleştirilmiş mesafe. Track'ler hareket yönüne dik olarak dağıtılır. Varsayılan değer 0.025'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `bezier` | Orta noktayı kontrol noktası olarak kullanarak Bezier eğrisi yolunu etkinleştirir. Varsayılan değer False'dir. | BOOLEAN | Evet | True / False |
| `orta_x` | Bezier eğrisi için normalleştirilmiş X kontrol noktası. Yalnızca 'bezier' etkinleştirildiğinde kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `orta_y` | Bezier eğrisi için normalleştirilmiş Y kontrol noktası. Yalnızca 'bezier' etkinleştirildiğinde kullanılır. Varsayılan değer 0.5'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `enterpolasyon` | Yol boyunca hareketin zamanlamasını/hızını kontrol eder (varsayılan: "linear"):<br>"linear" - sabit hız<br>"ease_in" - yavaş başlar ve hızlanır<br>"ease_out" - hızlı başlar ve yavaşlar<br>"ease_in_out" - yumuşak hızlanma ve yavaşlama<br>"constant" - tüm konumları başlangıç noktasında tutar | COMBO | Evet | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `iz_maskesi` | Görünür kareleri belirtmek için isteğe bağlı maske. Sağlandığında, maskenin sıfır olmayan herhangi bir piksele sahip olduğu kareler tüm track'ler için görünür olarak işaretlenir. | MASK | Hayır | - |

**Not:** `mid_x` ve `mid_y` parametreleri yalnızca `bezier` parametresi `True` olarak ayarlandığında kullanılır. `bezier` `False` olduğunda, yol başlangıç noktasından bitiş noktasına uzanan düz bir çizgidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `TRACKS` | Tüm karelerdeki tüm track'ler için üretilen yol koordinatlarını ve görünürlük bilgilerini içeren bir track nesnesi. | TRACKS |
| `iz_uzunluğu` | Track'lerin üretildiği kare sayısı; girdideki `num_frames` değeriyle eşleşir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/tr.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
