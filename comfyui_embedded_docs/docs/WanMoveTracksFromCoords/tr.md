# WanMoveTracksFromCoords

WanMoveTracksFromCoords düğümü, JSON biçimli bir koordinat dizesinden hareket izleri oluşturur. Koordinat verilerini, diğer video işleme düğümleri tarafından kullanılabilecek bir iz biçimine dönüştürür ve isteğe bağlı olarak izlerin zaman içindeki görünürlüğünü kontrol etmek için bir maske uygulayabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `track_coords` | İzlerin koordinat verilerini içeren JSON biçimli dize. Varsayılan değer boş bir listedir (`"[]"`). Bu girdi zorunlu bir girdidir, bu nedenle arayüzde bağlanmalıdır. | STRING | Hayır | N/A |
| `track_mask` | İsteğe bağlı maske. Sağlandığında düğüm, izlerin kare başına görünürlüğünü belirlemek için bunu kullanır: maskenin sıfır olmayan herhangi bir piksel içerdiği karelerde izler görünür olur. Sağlanmadığında, tüm izler tüm karelerde görünür olur. | MASK | Hayır | N/A |

**Not:** `track_coords` girdisi belirli bir JSON yapısı bekler. Bu, her izin bir kare listesi olduğu ve her karenin `x` ve `y` koordinatlarına sahip bir nesne olduğu bir iz listesi olmalıdır. Kare sayısı tüm izlerde tutarlı olmalıdır ve en az bir iz sağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `tracks` | Her iz için yol koordinatlarını ve görünürlük bilgilerini içeren oluşturulmuş iz verileri. | TRACKS |
| `track_length` | Oluşturulan izlerdeki toplam kare sayısı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/tr.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
