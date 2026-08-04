# MinimaxHailuo03FirstLastFrameNode

Bu düğüm, MiniMax H3 modelini kullanarak bir ilk kare görüntüsünden ve isteğe bağlı bir son kare görüntüsünden bir video oluşturur. Video, sağlanan görüntülerin en-boy oranına uyar ve bir son kare sağlandığında ilk kareden son kareye doğru animasyon yapar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. Bu birleşik kutu, model seçimini ("MiniMax H3"), oluşturulacak videoyu tanımlayan bir metin istemini, çıktı çözünürlüğünü ve video süresini içerir. İstem, en az bir boşluk olmayan karakter içermelidir. | COMBO | Evet | "MiniMax H3" |
| `first_frame` | Video için ilk kare görüntüsü. Oluşturulan videonun en-boy oranı bu görüntüyü izler. En az 256x256 piksel olmalı ve genişlik-yükseklik en-boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | - |
| `last_frame` | Video için isteğe bağlı son kare görüntüsü. Sağlandığında video ilk kareden başlar ve bu görüntüde biter. `first_frame` ile aynı boyut ve en-boy oranı gereksinimlerini karşılamalıdır. | IMAGE | Hayır | - |
| `seed` | Rastgele tohum (seed). Aynı istek aynı tohumla benzer ancak birebir aynı olması garanti edilmeyen sonuçlar verir. Her üretimden sonra rastgeleleştirmek için bir "üretim sonrası kontrol" seçeneği içerir. Varsayılan: 42. | INT | Evet | 0 ila 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. Bu gelişmiş bir parametredir. Varsayılan: False. | BOOLEAN | Evet | True<br>False |

**Kısıtlamalara ilişkin not:**
- `model` birleşik kutusundaki metin istemi boş olamaz; yalnızca boşluk karakterlerinden oluşan istemler reddedilir.
- Sağlanan herhangi bir kare görüntüsü (`first_frame` ve kullanılıyorsa `last_frame`) en az 256 piksel genişliğinde ve 256 piksel yüksekliğinde olmalı ve genişlik-yükseklik en-boy oranı 0,4 ile 2,5 (yaklaşık 2:5 ile 5:2) arasında olmalıdır.
- `last_frame` isteğe bağlıdır. Atlanırsa video yalnızca ilk kareden oluşturulur.
- Çıktı videosunun en-boy oranı, ayrı bir oran ayarıyla değil, sağlanan görüntülerle belirlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | MiniMax H3 modeli kullanılarak ilk kareden ve isteğe bağlı son kareden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `f4cb9217eb346019680c64b30c1beacce16f0050616b7b76265edc5840f6b21e`
