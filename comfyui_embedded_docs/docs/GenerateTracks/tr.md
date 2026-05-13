> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/tr.md)

`GenerateTracks` düğümü, video oluşturma için birden fazla paralel hareket yolu oluşturur. Bir başlangıç noktasından bitiş noktasına bir ana yol tanımlar, ardından bu yola paralel, eşit aralıklarla yerleştirilmiş bir dizi iz (track) üretir. Yolun şeklini (düz çizgi veya Bezier eğrisi), boyunca hareket hızını ve izlerin hangi karelerde görüneceğini kontrol edebilirsiniz.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16 - 4096 | Video karesinin piksel cinsinden genişliği. Varsayılan değer 832'dir. |
| `height` | INT | Evet | 16 - 4096 | Video karesinin piksel cinsinden yüksekliği. Varsayılan değer 480'dir. |
| `start_x` | FLOAT | Evet | 0.0 - 1.0 | Başlangıç konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 0.0'dır. |
| `start_y` | FLOAT | Evet | 0.0 - 1.0 | Başlangıç konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 0.0'dır. |
| `end_x` | FLOAT | Evet | 0.0 - 1.0 | Bitiş konumu için normalleştirilmiş X koordinatı (0-1). Varsayılan değer 1.0'dır. |
| `end_y` | FLOAT | Evet | 0.0 - 1.0 | Bitiş konumu için normalleştirilmiş Y koordinatı (0-1). Varsayılan değer 1.0'dır. |
| `num_frames` | INT | Evet | 1 - 1024 | İz konumlarının oluşturulacağı toplam kare sayısı. Varsayılan değer 81'dir. |
| `num_tracks` | INT | Evet | 1 - 100 | Oluşturulacak paralel iz sayısı. Varsayılan değer 5'tir. |
| `track_spread` | FLOAT | Evet | 0.0 - 1.0 | İzler arasındaki normalleştirilmiş mesafe. İzler, hareket yönüne dik olarak yayılır. Varsayılan değer 0.025'tir. |
| `bezier` | BOOLEAN | Evet | True / False | Orta noktayı kontrol noktası olarak kullanarak Bezier eğrisi yolunu etkinleştirir. Varsayılan değer False'dur. |
| `mid_x` | FLOAT | Evet | 0.0 - 1.0 | Bezier eğrisi için normalleştirilmiş X kontrol noktası. Yalnızca 'bezier' etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. |
| `mid_y` | FLOAT | Evet | 0.0 - 1.0 | Bezier eğrisi için normalleştirilmiş Y kontrol noktası. Yalnızca 'bezier' etkin olduğunda kullanılır. Varsayılan değer 0.5'tir. |
| `interpolation` | COMBO | Evet | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Yol boyunca hareketin zamanlamasını/hızını kontrol eder. Varsayılan değer "linear"dır. |
| `track_mask` | MASK | Hayır | - | Görünür kareleri belirtmek için isteğe bağlı maske. |

**Not:** `mid_x` ve `mid_y` parametreleri yalnızca `bezier` parametresi `True` olarak ayarlandığında kullanılır. `bezier` `False` olduğunda, yol başlangıç noktasından bitiş noktasına düz bir çizgidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | Oluşturulan yol koordinatlarını ve tüm karelerdeki tüm izler için görünürlük bilgilerini içeren bir izler nesnesi. |
| `track_length` | INT | İzlerin oluşturulduğu kare sayısı, girdi `num_frames` ile eşleşir. |

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
