> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/tr.md)

Bir kontrol görüntüsünü (canny) kullanarak görüntü oluşturur. Bu düğüm, bir kontrol görüntüsü alır ve sağlanan prompt'a dayalı olarak, kontrol görüntüsünde tespit edilen kenar yapısını takip ederek yeni bir görüntü oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Evet | - | Canny kenar tespiti kontrolü için kullanılan girdi görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için prompt (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Hayır | - | Prompt üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinse, prompt'u daha yaratıcı oluşturum için otomatik olarak değiştirir, ancak sonuçlar belirsizdir (aynı seed tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `canny_low_threshold` | FLOAT | Hayır | 0.01 - 0.99 | Canny kenar tespiti için düşük eşik; skip_processing True ise yok sayılır (varsayılan: 0.1) |
| `canny_high_threshold` | FLOAT | Hayır | 0.01 - 0.99 | Canny kenar tespiti için yüksek eşik; skip_processing True ise yok sayılır (varsayılan: 0.4) |
| `skip_preprocessing` | BOOLEAN | Hayır | - | Ön işleme atlanıp atlanmayacağı; control_image zaten canny işleminden geçirilmişse True, ham bir görüntü ise False olarak ayarlayın. (varsayılan: False) |
| `guidance` | FLOAT | Hayır | 1 - 100 | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 30) |
| `steps` | INT | Hayır | 15 - 50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0 - 18446744073709551615 | Gürültüyü oluşturmak için kullanılan rastgele seed. (varsayılan: 0) |

**Not:** `skip_preprocessing` True olarak ayarlandığında, kontrol görüntüsünün zaten bir canny kenar görüntüsü olarak işlendiği varsayıldığından, `canny_low_threshold` ve `canny_high_threshold` parametreleri yok sayılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Kontrol görüntüsü ve prompt'a dayalı olarak oluşturulan görüntü |