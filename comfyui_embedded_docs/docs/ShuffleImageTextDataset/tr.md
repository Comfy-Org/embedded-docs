> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/tr.md)

Bu düğüm, bir görüntü listesini ve bir metin listesini birlikte karıştırır ve bunların eşleşmelerini bozmaz. Karıştırma sırasını belirlemek için rastgele bir tohum kullanır, böylece aynı girdi listeleri, tohum her yeniden kullanıldığında aynı şekilde karıştırılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Karıştırılacak görüntü listesi. |
| `texts` | STRING | Evet | - | Karıştırılacak metin listesi. |
| `seed` | INT | Hayır | 0 ila 18446744073709551615 | Rastgele tohum. Karıştırma sırası bu değer tarafından belirlenir (varsayılan: 0). |

**Not:** `images` ve `texts` girdileri aynı uzunlukta listeler olmalıdır. Düğüm, bu çiftleri birlikte karıştırmadan önce, ilk görüntüyü ilk metinle, ikinci görüntüyü ikinci metinle eşleştirecek ve bu şekilde devam edecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Karıştırılmış görüntü listesi. |
| `texts` | STRING | Görüntülerle olan orijinal eşleşmeleri korunarak karıştırılmış metin listesi. |
