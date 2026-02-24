> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/tr.md)

Save Image and Text Dataset to Folder düğümü, bir dizi görüntüyü ve bunlara karşılık gelen metin açıklamalarını, ComfyUI'nin çıktı dizini içinde belirtilen bir klasöre kaydeder. PNG dosyası olarak kaydedilen her görüntü için, aynı temel ada sahip eşleşen bir metin dosyası, açıklamasını saklamak üzere oluşturulur. Bu, oluşturulan görüntülerin ve bunların açıklamalarının düzenli veri kümeleri oluşturmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Kaydedilecek görüntü listesi. |
| `texts` | STRING | Evet | - | Kaydedilecek metin açıklaması listesi. |
| `folder_name` | STRING | Hayır | - | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "dataset") |
| `filename_prefix` | STRING | Hayır | - | Kaydedilen görüntü dosya adları için önek. (varsayılan: "image") |

**Not:** `images` ve `texts` girişleri liste şeklindedir. Düğüm, sağlanan metin açıklamalarının sayısının, sağlanan görüntü sayısıyla eşleşmesini bekler. Her açıklama, eşleştirildiği görüntüye karşılık gelen bir `.txt` dosyasına kaydedilecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğümün herhangi bir çıktısı yoktur. Dosyaları doğrudan dosya sistemine kaydeder. |
