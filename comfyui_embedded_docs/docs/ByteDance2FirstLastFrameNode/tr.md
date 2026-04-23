> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/tr.md)

Bu düğüm, ByteDance'in Seedance 2.0 modelini kullanarak bir video oluşturur. Videoyu bir metin istemine ve gerekli bir ilk kare görüntüsüne dayanarak oluşturur. Video dizisinin sonunu yönlendirmek için isteğe bağlı olarak bir son kare görüntüsü sağlayabilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Video oluşturma için kullanılacak model. Seedance 2.0 maksimum kalite içindir, Seedance 2.0 Fast ise hız için optimize edilmiştir. Bir model seçmek, `prompt`, `resolution`, `ratio`, `duration` ve `generate_audio` için ek girişler ortaya çıkaracaktır. |
| `first_frame` | IMAGE | Hayır | - | Videonun ilk karesi olarak kullanılacak görüntü. |
| `last_frame` | IMAGE | Hayır | - | Videonun son karesi olarak kullanılacak görüntü. |
| `first_frame_asset_id` | STRING | Hayır | - | İlk kare olarak kullanılacak bir Seedance asset_id'si. Bu, `first_frame` görüntü girişi ile aynı anda kullanılamaz. Varsayılan boş bir dizedir. |
| `last_frame_asset_id` | STRING | Hayır | - | Son kare olarak kullanılacak bir Seedance asset_id'si. Bu, `last_frame` görüntü girişi ile aynı anda kullanılamaz. Varsayılan boş bir dizedir. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Bir tohum değeri. Bu tohumu değiştirmek düğümün yeniden çalışmasına neden olur, ancak sonuçlar deterministik değildir. Varsayılan 0'dır. |
| `watermark` | BOOLEAN | Hayır | - | Oluşturulan videoya filigran eklenip eklenmeyeceği. Varsayılan False değeridir. |

**Parametre Kısıtlamaları:**
*   **Ya** bir `first_frame` görüntüsü **ya da** bir `first_frame_asset_id` sağlamalısınız. Her ikisini de sağlamak hataya neden olur.
*   Aynı kare için hem bir `last_frame` görüntüsü hem de bir `last_frame_asset_id` sağlayamazsınız.
*   `model` girişi dinamik bir birleşik giriştir. Bir model seçtikten sonra, ortaya çıkan `prompt` alanını (bir metin açıklaması) da doldurmalı ve diğer ortaya çıkan parametreleri (`resolution`, `ratio`, `duration`, `generate_audio`) yapılandırmalısınız.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video. |