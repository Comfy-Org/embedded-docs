> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/tr.md)

Görselleri ve Metin Veri Kümesini Klasöre Kaydet düğümü, bir görsel listesini ve bunlara karşılık gelen metin açıklamalarını ComfyUI çıktı dizini içindeki belirtilen bir klasöre kaydeder. Her görsel PNG dosyası olarak kaydedilirken, aynı temel ada sahip eşleşen bir metin dosyası oluşturularak açıklaması saklanır. Bu özellik, oluşturulan görseller ve açıklamalarından oluşan düzenli veri kümeleri oluşturmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Kaydedilecek görsel listesi. |
| `texts` | STRING | Evet | - | Kaydedilecek metin açıklamaları listesi. |
| `folder_name` | STRING | Hayır | - | Görsellerin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "dataset") |
| `filename_prefix` | STRING | Hayır | - | Kaydedilen görsel dosya adları için ön ek. (varsayılan: "image") |

**Not:** `images` ve `texts` girişleri listedir. Düğüm, metin açıklamalarının sayısının sağlanan görsel sayısıyla eşleşmesini bekler. Her açıklama, eşleştirildiği görsele karşılık gelen bir `.txt` dosyasına kaydedilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| - | - | Bu düğümün herhangi bir çıktısı yoktur. Dosyaları doğrudan dosya sistemine kaydeder. |

---
**Source fingerprint (SHA-256):** `0c76f623e97b1502c850e0a59dc9edd7c241bcd823f5e32a8dcdd8b8160d2e44`
