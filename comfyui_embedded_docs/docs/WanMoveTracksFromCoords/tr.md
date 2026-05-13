> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/tr.md)

WanMoveTracksFromCoords düğümü, JSON formatındaki bir koordinat dizisinden hareket izleri oluşturur. Koordinat verilerini, diğer video işleme düğümleri tarafından kullanılabilecek bir tensör formatına dönüştürür ve isteğe bağlı olarak izlerin zaman içindeki görünürlüğünü kontrol etmek için bir maske uygulayabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | Hayır | Yok | İzler için koordinat verilerini içeren JSON formatında bir dize. Varsayılan değer boş bir listedir (`"[]"`). |
| `track_mask` | MASK | Hayır | Yok | İsteğe bağlı bir maske. Sağlandığında, düğüm her bir izin kare başına görünürlüğünü belirlemek için bunu kullanır. |

**Not:** `track_coords` girişi belirli bir JSON yapısı bekler. Her bir izin bir kare listesi olduğu ve her bir karenin `x` ve `y` koordinatlarına sahip bir nesne olduğu bir iz listesi olmalıdır. Kare sayısı tüm izler arasında tutarlı olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Oluşturulan iz verileri, her bir iz için yol koordinatlarını ve görünürlük bilgilerini içerir. |
| `track_length` | INT | Oluşturulan izlerdeki toplam kare sayısı. |

---
**Source fingerprint (SHA-256):** `106b05b3bdb5ede6e31216b9f3c14160630df0eee1f4e8a645c2b6cf9fbecf8c`
