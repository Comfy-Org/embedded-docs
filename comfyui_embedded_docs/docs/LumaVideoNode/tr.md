> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/tr.md)

İstem ve çıktı ayarlarına dayalı olarak senkron bir şekilde video oluşturur. Bu düğüm, metin açıklamaları ve çeşitli oluşturma parametrelerini kullanarak video içeriği oluşturur ve oluşturma işlemi tamamlandığında nihai video çıktısını üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Video oluşturma için istem (varsayılan: boş dize) |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | Kullanılacak video oluşturma modeli |
| `en_boy_oranı` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan video için en-boy oranı (varsayılan: 16:9) |
| `çözünürlük` | COMBO | Evet | Birden fazla seçenek mevcut | Video için çıktı çözünürlüğü (varsayılan: 540p) |
| `süre` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan videonun süresi |
| `döngü` | BOOLEAN | Evet | - | Videoda döngü olup olmayacağı (varsayılan: False) |
| `tohum` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohuma bakılmaksızın belirsizdir (varsayılan: 0) |
| `luma_kavramları` | CUSTOM | Hayır | - | Luma Concepts düğümü aracılığıyla kamera hareketini belirlemek için isteğe bağlı Kamera Kavramları |

**Not:** `ray_1_6` modeli kullanılırken, `duration` ve `resolution` parametreleri otomatik olarak None olarak ayarlanır ve oluşturma işlemini etkilemez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |