Bu düğüm, bir görüntü listesi ile bir metin listesini birlikte karıştırarak eşleştirmelerinin bozulmadan kalmasını sağlar. Karıştırma sırasını belirlemek için rastgele bir tohum değeri kullanır; aynı tohum değeri tekrar kullanıldığında, aynı giriş listelerinin aynı şekilde karıştırılmasını garanti eder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Karıştırılacak görüntü listesi. | IMAGE | Evet | - |
| `texts` | Karıştırılacak metin listesi. | STRING | Evet | - |
| `seed` | Rastgele tohum değeri. Karıştırma sırası bu değere göre belirlenir (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 arası |

**Not:** `images` ve `texts` girişleri aynı uzunlukta listeler olmalıdır. Düğüm, bu çiftleri birlikte karıştırmadan önce ilk görüntüyü ilk metinle, ikinci görüntüyü ikinci metinle vb. eşleştirecektir.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Karıştırılmış görüntü listesi. | IMAGE |
| `texts` | Görüntülerle orijinal eşleştirmelerini koruyan, karıştırılmış metin listesi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/tr.md)

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
