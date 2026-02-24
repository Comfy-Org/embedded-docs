> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/tr.md)

`GenerateTracks` düğümü, video oluşturma için birden fazla paralel hareket yolu oluşturur. Bir başlangıç noktasından bir bitiş noktasına uzanan bir ana yol tanımlar ve ardından bu yola paralel, eşit aralıklarla yerleştirilmiş bir dizi yol oluşturur. Yolun şeklini (düz çizgi veya Bezier eğrisi), yol boyunca hareketin hızını ve yolların hangi karelerde görünür olduğunu kontrol edebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16 - 4096 | Video karesinin piksel cinsinden genişliği. Varsayılan değer 832'dir. |
| `height` | INT | Evet | 16 - 4096 | Video karesinin piksel cinsinden yüksekliği. Varsayılan değer 480'dir. |
| `start_x` | FLOAT | Evet | 0.0 - 1.0 | Başlangıç konumu için normalize edilmiş X koordinatı (0-1). Varsayılan değer 0.0'dır. |
| `start_y` | FLOAT | Evet | 0.0 - 1.0 | Başlangıç konumu için normalize edilmiş Y koordinatı (0-1). Varsayılan değer 0.0'dır. |
| `end_x` | FLOAT | Evet | 0.0 - 1.0 | Bitiş konumu için normalize edilmiş X koordinatı (0-1). Varsayılan değer 1.0'dır. |
| `end_y` | FLOAT | Evet | 0.0 - 1.0 | Bitiş konumu için normalize edilmiş Y koordinatı (0-1). Varsayılan değer 1.0'dır. |
| `num_frames` | INT | Evet | 1 - 1024 | Yol konumlarının oluşturulacağı toplam kare sayısı. Varsayılan değer 81'dir. |
| `num_tracks` | INT | Evet | 1 - 100 | Oluşturulacak paralel yol sayısı. Varsayılan değer 5'tir. |
| `track_spread` | FLOAT | Evet | 0.0 - 1.0 | Yollar arasındaki normalize edilmiş mesafe. Yollar, hareket yönüne dik olarak yayılır. Varsayılan değer 0.025'tir. |
| `bezier` | BOOLEAN | Evet | True / False | Orta noktayı kontrol noktası olarak kullanarak Bezier eğrisi yolunu etkinleştirir. Varsayılan değer False'dur. |
| `mid_x` | FLOAT | Evet | 0.0 - 1.0 | Bezier eğrisi için normalize edilmiş X kontrol noktası. Yalnızca 'bezier' etkinleştirildiğinde kullanılır. Varsayılan değer 0.5'tir. |
| `mid_y` | FLOAT | Evet | 0.0 - 1.0 | Bezier eğrisi için normalize edilmiş Y kontrol noktası. Yalnızca 'bezier' etkinleştirildiğinde kullanılır. Varsayılan değer 0.5'tir. |
| `interpolation` | COMBO | Evet | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Yol boyunca hareketin zamanlamasını/hızını kontrol eder. Varsayılan değer "linear"dır. |
| `track_mask` | MASK | Hayır | - | Görünür kareleri belirtmek için isteğe bağlı maske. |

**Not:** `mid_x` ve `mid_y` parametreleri yalnızca `bezier` parametresi `True` olarak ayarlandığında kullanılır. `bezier` `False` olduğunda, yol başlangıçtan bitiş noktasına düz bir çizgidir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | Tüm karelerdeki tüm yollar için oluşturulan yol koordinatlarını ve görünürlük bilgilerini içeren bir yollar nesnesi. |
| `track_length` | INT | Yolların oluşturulduğu kare sayısı, giriş `num_frames` değeriyle eşleşir. |
