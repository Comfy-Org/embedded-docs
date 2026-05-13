> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/tr.md)

Görüntü Izgarası düğümü, birden fazla görüntüyü tek bir düzenli ızgarada veya kolajda birleştirir. Bir görüntü listesi alır ve bunları belirtilen sayıda sütuna yerleştirir, her görüntüyü tanımlanmış bir hücre boyutuna sığacak şekilde yeniden boyutlandırır ve aralarına isteğe bağlı boşluk ekler. Sonuç, tüm giriş görüntülerini bir ızgara düzeninde içeren tek bir yeni görüntüdür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görseller` | IMAGE | Evet | - | Izgaraya yerleştirilecek görüntülerin listesi. Düğümün çalışması için en az bir görüntü gereklidir. |
| `sütunlar` | INT | Hayır | 1 - 20 | Izgaradaki sütun sayısı (varsayılan: 4). |
| `hücre_genişliği` | INT | Hayır | 32 - 2048 | Izgaradaki her hücrenin piksel cinsinden genişliği (varsayılan: 256). |
| `hücre_yüksekliği` | INT | Hayır | 32 - 2048 | Izgaradaki her hücrenin piksel cinsinden yüksekliği (varsayılan: 256). |
| `boşluk` | INT | Hayır | 0 - 50 | Izgaradaki görüntüler arasına yerleştirilecek piksel cinsinden boşluk miktarı (varsayılan: 4). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Tüm giriş görüntülerinin bir ızgarada düzenlendiği tek çıkış görüntüsü. |

---
**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`
