# Görüntü Veri Setini Klasöre Kaydet

Bu düğüm, bir görüntü listesini ComfyUI'nin çıktı dizini içindeki belirtilen bir klasöre kaydeder. Her görüntüyü yapılandırılabilir bir dosya adı öneki kullanarak diskte PNG dosyası olarak yazar. Bu düğüm kullanımdan kaldırılmıştır ve yerini, hedef klasörün dosya adı önekinde belirtilebildiği mevcut Save Image düğümleri almıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kaydedilecek görüntü listesi. | IMAGE | Evet | N/A |
| `folder_name` | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). Varsayılan: "dataset". | STRING | Hayır | N/A |
| `filename_prefix` | Kaydedilen görüntü dosya adları için önek. Varsayılan: "image". Gelişmiş parametre. | STRING | Hayır | N/A |
| `mod` | Mevcut dosyaların üzerine yazılıp yazılmayacağını veya üzerine yazmayı önlemek için dosya adlarının artırılıp artırılmayacağını belirtir. Varsayılan: "overwrite". | COMBO | Hayır | "overwrite"<br>"increment" |

**Notlar:**

- `images` girdisi bir listedir, böylece tek bir çalıştırmada birden fazla görüntü kaydedilebilir.
- `folder_name`, `filename_prefix` ve `mode` parametreleri skaler değerlerdir; bir liste bağlanırsa listedeki yalnızca ilk değer kullanılır.
- `folder_name`, ComfyUI'nin çıktı dizini içindeki bir konuma karşılık gelmelidir. Çıktı dizininin dışına çıkan değerler (örneğin, `..` içeren yollar veya mutlak yollar) bir hata ile reddedilir.
- "overwrite" modunda, dosyalar `{prefix}_00000.png`, `{prefix}_00001.png` vb. şeklinde kaydedilir ve mevcut dosyaların üzerine yazılır. "increment" modunda, dosya adına bir sayaç eklenir, böylece mevcut dosyaların üzerine yazılmaz.

## Çıktılar

Bu düğümün herhangi bir çıktısı yoktur. Dosya sistemine kaydetme işlemi gerçekleştiren bir çıktı düğümüdür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
