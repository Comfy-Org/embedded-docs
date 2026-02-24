> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/tr.md)

WanMoveTracksFromCoords düğümü, bir koordinat noktaları listesinden bir dizi hareket izi oluşturur. JSON formatlı bir koordinat dizgisini, diğer video işleme düğümleri tarafından kullanılabilecek bir tensör formatına dönüştürür ve isteğe bağlı olarak izlerin zaman içindeki görünürlüğünü kontrol etmek için bir maske uygulayabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | Evet | Yok | İzler için koordinat verilerini içeren JSON formatlı bir dizi. Varsayılan değer boş bir listedir (`"[]"`). |
| `track_mask` | MASK | Hayır | Yok | İsteğe bağlı bir maske. Sağlandığında, düğüm her bir izin kare başına görünürlüğünü belirlemek için bunu kullanır. |

**Not:** `track_coords` girişi belirli bir JSON yapısı bekler. Bu, bir iz listesi olmalıdır; her iz bir kare listesidir ve her kare `x` ve `y` koordinatlarına sahip bir nesnedir. Kare sayısı tüm izlerde tutarlı olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Oluşturulan iz verileri; her bir iz için yol koordinatlarını ve görünürlük bilgisini içerir. |
| `track_length` | INT | Oluşturulan izlerdeki toplam kare sayısı. |
