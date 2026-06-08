Görüntü Izgarası düğümü, birden fazla görüntüyü tek bir düzenli ızgarada veya kolajda birleştirir. Bir görüntü listesi alır ve bunları belirtilen sayıda sütuna yerleştirir, her görüntüyü tanımlanmış bir hücre boyutuna sığacak şekilde yeniden boyutlandırır ve aralarına isteğe bağlı boşluk ekler. Sonuç, tüm giriş görüntülerini bir ızgara düzeninde içeren tek bir yeni görüntüdür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görseller` | Izgaraya yerleştirilecek görüntülerin listesi. Düğümün çalışması için en az bir görüntü gereklidir. | IMAGE | Evet | - |
| `sütunlar` | Izgaradaki sütun sayısı (varsayılan: 4). | INT | Hayır | 1 - 20 |
| `hücre_genişliği` | Izgaradaki her hücrenin piksel cinsinden genişliği (varsayılan: 256). | INT | Hayır | 32 - 2048 |
| `hücre_yüksekliği` | Izgaradaki her hücrenin piksel cinsinden yüksekliği (varsayılan: 256). | INT | Hayır | 32 - 2048 |
| `boşluk` | Izgaradaki görüntüler arasına yerleştirilecek piksel cinsinden boşluk miktarı (varsayılan: 4). | INT | Hayır | 0 - 50 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Tüm giriş görüntülerinin bir ızgarada düzenlendiği tek çıkış görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/tr.md)

---
**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`
