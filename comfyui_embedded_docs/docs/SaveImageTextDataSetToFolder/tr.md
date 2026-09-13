# Görüntü ve Metin Veri Setini Klasöre Kaydet

Save Image-Text (to Folder), görüntü ve metin açıklaması çiftlerinden oluşan bir veri kümesini ComfyUI'nin çıktı dizini içindeki bir klasöre kaydeder. Her görüntü bir PNG dosyası olarak, eşleşen metin açıklaması ise aynı temel dosya adına sahip bir TXT dosyası olarak yazılır; böylece her görüntü açıklamasıyla eşleştirilmiş olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kaydedilecek görüntülerin listesi. | IMAGE | Evet | - |
| `texts` | Kaydedilecek metin açıklamalarının listesi. Bu girdi isteğe bağlıdır. | STRING | Hayır | - |
| `folder_name` | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "dataset") | STRING | Evet | - |
| `filename_prefix` | Kaydedilen görüntü dosya adları için ön ek. (varsayılan: "image") | STRING | Evet | - |
| `mode` | Mevcut dosyaların üzerine yazılıp yazılmayacağını veya üzerine yazmayı önlemek için dosya adlarının artırılıp artırılmayacağını belirler. (varsayılan: "overwrite") | COMBO | Evet | "overwrite"<br>"increment" |

**Not:** `images` girdisi bir listedir ve düğüm hem `images` hem de `texts` girdilerini liste olarak alır. `texts` girdisi isteğe bağlıdır; sağlanırsa, metin açıklamalarından oluşan bir liste olmalı ve `images` ile aynı sayıda öğe içermelidir. Her metin açıklaması, eşleştiği görüntüye karşılık gelen bir `.txt` dosyası olarak kaydedilir. `overwrite` modunda dosyalar `{filename_prefix}_{index}.png` olarak adlandırılır ve aynı ada sahip mevcut dosyaların yerini alır. `increment` modunda, mevcut dosyaların üzerine yazılmaması için dosya adlarına benzersiz bir sayaç eklenir. `folder_name`, çıktı dizini içinde bir yola çözümlenmelidir; çıktı dizininin dışına çıkmaya çalışan klasör adları (örneğin `..` ile) reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| - | Bu düğüm veri döndürmez. Dosyaları doğrudan dosya sistemine kaydeder. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
