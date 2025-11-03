> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/tr.md)

Bu düğüm, derinlik kontrol görüntüsünü rehber olarak kullanarak görüntüler oluşturur. Bir kontrol görüntüsü ve bir metin istemi alır, ardından hem kontrol görüntüsündeki derinlik bilgisini hem de istemdeki açıklamayı takip eden yeni bir görüntü oluşturur. Düğüm, görüntü oluşturma işlemini gerçekleştirmek için harici bir API'ye bağlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Evet | - | Görüntü oluşturmayı yönlendirmek için kullanılan derinlik kontrol görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istemi otomatik olarak değiştirir, ancak sonuçlar belirsizdir (aynı tohum tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `skip_preprocessing` | BOOLEAN | Hayır | - | Ön işlemenin atlanıp atlanmayacağı; control_image zaten derinlik bilgisi içeriyorsa True, ham bir görüntü ise False olarak ayarlayın. (varsayılan: False) |
| `guidance` | FLOAT | Hayır | 1-100 | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 15) |
| `steps` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0-18446744073709551615 | Gürültüyü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Derinlik kontrol görüntüsü ve isteme dayalı olarak oluşturulan görüntü |