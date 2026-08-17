# WanMoveTracksFromCoords

WanMoveTracksFromCoords düğümü, JSON formatındaki bir koordinat dizisinden hareket izleri oluşturur. Koordinat verilerini, diğer video işleme düğümleri tarafından kullanılabilen bir tensör formatına dönüştürür ve isteğe bağlı olarak izlerin zaman içindeki görünürlüğünü kontrol etmek için bir maske uygulayabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `track_coords` | İzler için koordinat verilerini içeren JSON formatında bir dize. Varsayılan değer boş bir listedir (`"[]"`). | STRING | Hayır | N/A |
| `track_mask` | İsteğe bağlı bir maske. Sağlandığında, düğüm her karede her izin görünürlüğünü belirlemek için maskeyi kullanır. Sağlanmadığında, tüm izler her kare için görünür kabul edilir. | MASK | Hayır | N/A |

**Not:** `track_coords` girdisi belirli bir JSON yapısı bekler. Her bir izin bir kare listesi olduğu bir iz listesi olmalıdır ve her kare `x` ve `y` koordinatlarına sahip bir nesnedir. Kare sayısı tüm izlerde tutarlı olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `tracks` | Oluşturulan iz verileri; her iz için yol koordinatlarını ve görünürlük bilgisini içerir. | TRACKS |
| `track_length` | Oluşturulan izlerdeki toplam kare sayısı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/tr.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
