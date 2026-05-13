> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/tr.md)

Bu düğüm, bir görüntü listesi ile bir metin listesini birlikte karıştırarak eşleştirmelerinin bozulmadan kalmasını sağlar. Karıştırma sırasını belirlemek için rastgele bir tohum değeri kullanır; aynı tohum değeri tekrar kullanıldığında, aynı giriş listelerinin aynı şekilde karıştırılmasını garanti eder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Karıştırılacak görüntü listesi. |
| `texts` | STRING | Evet | - | Karıştırılacak metin listesi. |
| `seed` | INT | Hayır | 0 ile 18446744073709551615 arası | Rastgele tohum değeri. Karıştırma sırası bu değere göre belirlenir (varsayılan: 0). |

**Not:** `images` ve `texts` girişleri aynı uzunlukta listeler olmalıdır. Düğüm, bu çiftleri birlikte karıştırmadan önce ilk görüntüyü ilk metinle, ikinci görüntüyü ikinci metinle vb. eşleştirecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Karıştırılmış görüntü listesi. |
| `texts` | STRING | Görüntülerle orijinal eşleştirmelerini koruyan, karıştırılmış metin listesi. |

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
