Bu düğüm, ByteDance'in Seedance 2.0 modelini kullanarak bir video oluşturur. Videoyu bir metin istemine ve gerekli bir ilk kare görüntüsüne dayanarak oluşturur. Video dizisinin sonunu yönlendirmek için isteğe bağlı olarak bir son kare görüntüsü sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model. Seedance 2.0 maksimum kalite içindir, Seedance 2.0 Fast ise hız için optimize edilmiştir. Bir model seçmek, `prompt`, `resolution`, `ratio`, `duration` ve `generate_audio` için ek girişler ortaya çıkaracaktır. | COMBO | Evet | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `first_frame` | Videonun ilk karesi olarak kullanılacak görüntü. | IMAGE | Hayır | - |
| `last_frame` | Videonun son karesi olarak kullanılacak görüntü. | IMAGE | Hayır | - |
| `first_frame_asset_id` | İlk kare olarak kullanılacak bir Seedance asset_id'si. Bu, `first_frame` görüntü girişi ile aynı anda kullanılamaz. Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `last_frame_asset_id` | Son kare olarak kullanılacak bir Seedance asset_id'si. Bu, `last_frame` görüntü girişi ile aynı anda kullanılamaz. Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `seed` | Bir tohum değeri. Bu tohumu değiştirmek düğümün yeniden çalışmasına neden olur, ancak sonuçlar deterministik değildir. Varsayılan 0'dır. | INT | Hayır | 0 ile 2147483647 arası |
| `watermark` | Oluşturulan videoya filigran eklenip eklenmeyeceği. Varsayılan False (Yanlış) değeridir. | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**
*   **Ya** bir `first_frame` görüntüsü **ya da** bir `first_frame_asset_id` sağlamalısınız. Her ikisini de sağlamak hataya neden olur.
*   Aynı kare için hem bir `last_frame` görüntüsü hem de bir `last_frame_asset_id` sağlayamazsınız.
*   `model` girişi dinamik bir birleşik kutudur. Bir model seçtikten sonra, ortaya çıkan `prompt` alanını (bir metin açıklaması) da doldurmalı ve diğer ortaya çıkan parametreleri (`resolution`, `ratio`, `duration`, `generate_audio`) yapılandırmalısınız.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `2c9c1fe8fddd0c3e1c356d2b93a06a07f83db8f7a0380e94629a91ce1ff1e29a`
