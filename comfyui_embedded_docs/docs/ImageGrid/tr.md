> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/tr.md)

Image Grid düğümü, birden fazla görüntüyü tek bir düzenli ızgara veya kolaj halinde birleştirir. Bir görüntü listesi alır ve bunları belirtilen sütun sayısına göre düzenler, her görüntüyü tanımlanmış bir hücre boyutuna sığacak şekilde yeniden boyutlandırır ve aralarına isteğe bağlı dolgu ekler. Sonuç, tüm girdi görüntülerini bir ızgara düzeninde içeren tek bir yeni görüntüdür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Izgarada düzenlenecek görüntülerin listesi. Düğümün çalışması için en az bir görüntü gereklidir. |
| `columns` | INT | Hayır | 1 - 20 | Izgaradaki sütun sayısı (varsayılan: 4). |
| `cell_width` | INT | Hayır | 32 - 2048 | Izgaradaki her hücrenin piksel cinsinden genişliği (varsayılan: 256). |
| `cell_height` | INT | Hayır | 32 - 2048 | Izgaradaki her hücrenin piksel cinsinden yüksekliği (varsayılan: 256). |
| `padding` | INT | Hayır | 0 - 50 | Izgaradaki görüntüler arasına piksel cinsinden konulacak dolgu miktarı (varsayılan: 4). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Tüm girdi görüntülerinin bir ızgarada düzenlendiği tek çıktı görüntüsü. |
