> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/tr.md)

LossGraphNode, eğitim kayıp değerlerinin zaman içindeki değişimini görsel bir grafik olarak oluşturur ve bunu bir görüntü dosyası olarak kaydeder. Eğitim süreçlerinden gelen kayıp verilerini alır ve kaybın eğitim adımları boyunca nasıl değiştiğini gösteren bir çizgi grafiği oluşturur. Ortaya çıkan grafik, eksen etiketlerini, minimum/maksimum kayıp değerlerini içerir ve otomatik olarak geçici çıktı dizinine bir zaman damgası ile kaydedilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `loss` | LOSS | Evet | Birden fazla seçenek mevcut | Grafiği çizilecek kayıp değerlerini içeren kayıp verisi (varsayılan: boş sözlük) |
| `filename_prefix` | STRING | Evet | - | Çıktı görüntü dosya adı için önek (varsayılan: "loss_graph") |

**Not:** `loss` parametresi, kayıp değerleri içeren bir "loss" anahtarı barındıran geçerli bir kayıp sözlüğü gerektirir. Düğüm, kayıp değerlerini grafik boyutlarına sığdırmak için otomatik olarak ölçeklendirir ve eğitim adımları boyunca kayıp ilerlemesini gösteren bir çizgi grafiği oluşturur.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | Geçici dizine kaydedilen oluşturulmuş kayıp grafiği görüntüsü |