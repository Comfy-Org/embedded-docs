# Görüntü ve Metin Veri Setini Klasöre Kaydet

Save Image-Text (to Folder), ComfyUI'nin çıktı dizini içindeki bir klasöre eşleştirilmiş görüntü ve metin açıklamalarından oluşan bir veri kümesi kaydeden bir çıktı düğümüdür. Her görüntü PNG dosyası olarak kaydedilir ve açıklamalar sağlandığında, her görüntü için aynı temel ada sahip eşleşen bir TXT dosyası oluşturulur. Bu, oluşturulan görüntülerin ve açıklamalarının organize veri kümelerini oluşturmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek görüntü listesi. | IMAGE | Evet | - |
| `texts` | Kaydedilecek metin açıklamaları listesi. Bu girdi isteğe bağlıdır. | STRING | Hayır | - |
| `folder_name` | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "dataset") | STRING | Evet | - |
| `filename_prefix` | Kaydedilen görüntü dosya adları için ön ek. (varsayılan: "image") | STRING | Evet | - |
| `mode` | Mevcut dosyaların üzerine yazılıp yazılmayacağı veya üzerine yazılmasını önlemek için dosya adlarının artırılıp artırılmayacağı. (varsayılan: "overwrite") | COMBO | Evet | "overwrite"<br>"increment" |

**Not:** `images` girdisi bir listedir. `texts` girdisi isteğe bağlıdır; sağlanırsa, bir metin açıklamaları listesi olmalıdır. Açıklamalar, görüntülerle sırayla eşleştirilir ve her açıklama, eşleştirildiği görüntüyle aynı temel ada sahip bir UTF-8 `.txt` dosyası olarak kaydedilir (örneğin, `image_00000.png` için `image_00000.txt`). Açıklama sayısı görüntü sayısından azsa, kalan görüntüler açıklama olmadan kaydedilir; fazladan açıklamalar yok sayılır.

Varsayılan değerlere sahip girdilerin (`folder_name`, `filename_prefix`, `mode`) bağlanması gerekmez; varsayılan değerleri otomatik olarak kullanılır.

`mode` `overwrite` olarak ayarlandığında (varsayılan), görüntüler `image_00000.png` gibi adlarla kaydedilir ve aynı ada sahip mevcut dosyaların üzerine yazılır. `mode` `increment` olarak ayarlandığında, dosya adlarına otomatik artan bir sayaç eklenir, böylece mevcut dosyaların üzerine yazılmaz.

`folder_name` değeri, ComfyUI'nin çıktı dizini içinde bir konuma çözümlenmelidir. Çıktı dizininin dışına çıkmaya çalışan klasör adları (örneğin, `..` kullanan) reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğümün çıktısı yoktur. Dosyaları doğrudan dosya sistemine kaydeder. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
