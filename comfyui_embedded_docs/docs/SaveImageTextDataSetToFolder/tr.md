# Görüntü ve Metin Veri Setini Klasöre Kaydet

Save Image-Text (to Folder), bir görüntü listesini ve bunlara karşılık gelen metin açıklamalarını ComfyUI'nin çıktı dizini içindeki belirtilen bir klasöre kaydeder. PNG dosyası olarak kaydedilen her görüntü için, açıklamasını saklamak amacıyla aynı temel ada sahip bir TXT dosyası oluşturulur. Bu özellik, üretilen görüntülerin açıklamalarıyla eşleştirildiği düzenli veri setleri oluşturmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kaydedilecek görüntülerin listesi. | IMAGE | Evet | - |
| `texts` | Kaydedilecek metin açıklamalarının listesi. Bu girdi isteğe bağlıdır. | STRING | Hayır | - |
| `folder_name` | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "dataset") | STRING | Evet | - |
| `filename_prefix` | Kaydedilen görüntü dosya adları için önek. (varsayılan: "image") | STRING | Evet | - |
| `mod` | Mevcut dosyaların üzerine yazılıp yazılmayacağını veya üzerine yazmayı önlemek için dosya adlarının artırılıp artırılmayacağını belirler. (varsayılan: "overwrite") | COMBO | Evet | "overwrite"<br>"increment" |

**Not:** `images` girdisi bir listedir. `texts` girdisi isteğe bağlıdır; sağlanırsa, bir metin açıklamaları listesi olmalı ve `images` ile aynı sayıda öğe içermelidir. Her açıklama, eşleştirildiği görüntüye karşılık gelen bir `.txt` dosyası olarak kaydedilir. `overwrite` modunda, dosyalar `{filename_prefix}_{index}.png` olarak adlandırılır ve aynı ada sahip mevcut dosyaların üzerine yazılır. `increment` modunda, dosya adlarına benzersiz bir sayaç eklenir, böylece mevcut dosyaların üzerine yazılmaz. `folder_name`, çıktı dizini içindeki bir yola çözümlenmelidir; bu dizinden kaçmaya çalışan klasör adları (örneğin `..` ile) reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| - | Bu düğüm veri döndürmez. Dosyaları doğrudan dosya sistemine kaydeder. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
