# MiniMax H3 İlk-Son-Kare'den Videoya

Bu düğüm, MiniMax H3 modelini kullanarak bir ilk kare görüntüsünden ve isteğe bağlı bir son kare görüntüsünden video oluşturur. Video, sağlanan görüntülerin en-boy oranını takip eder ve bir son kare sağlandığında ilk kareden son kareye doğru animasyon yapar.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. Bir model seçmek, modele özgü ayarlarını (istem, çözünürlük, süre) görüntüler. | COMBO | Evet | "MiniMax H3" |
| `first_frame` | Videonun ilk kare görüntüsü. Oluşturulan videonun en-boy oranı bu görüntüyü takip eder. En az 256x256 piksel olmalı ve genişlik-yükseklik en-boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | - |
| `last_frame` | Videonun isteğe bağlı son kare görüntüsü. Sağlandığında video ilk kareden başlar ve bu görüntüde sona erer. `first_frame` ile aynı boyut ve en-boy oranı gereksinimlerini karşılamalıdır. | IMAGE | Hayır | - |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer sonuçlar verir, ancak birebir aynı sonuçlar garanti edilmez. Her üretimden sonra rastgeleleştirme için 'üretimden sonra kontrol' seçeneğini içerir. Varsayılan: 42. | INT | Evet | 0 ile 4294967295 arası |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. Bu gelişmiş bir parametredir. Varsayılan: False. | BOOLEAN | Evet | True<br>False |

### MiniMax H3 Girdileri

Bu girdiler, `model` seçicisinde "MiniMax H3" seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan: 5. | INT | Evet | 4 ile 15 arası |

**Kısıtlamalar hakkında not:**
- `model` birleşik kutusundaki metin istemi boş olamaz; yalnızca boşluk içeren istemler reddedilir.
- Sağlanan herhangi bir kare görüntüsü (`first_frame` ve kullanılıyorsa `last_frame`) en az 256 piksel genişliğinde ve 256 piksel yüksekliğinde olmalı, genişlik-yükseklik en-boy oranı 0,4 ile 2,5 arasında olmalıdır (yaklaşık 2:5 ila 5:2).
- `last_frame` isteğe bağlıdır. Atlanırsa video yalnızca ilk kareden oluşturulur.
- Çıktı videosunun en-boy oranı, ayrı bir oran ayarıyla değil, sağlanan görüntülerle belirlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | MiniMax H3 modeli kullanılarak ilk kareden ve isteğe bağlı son kareden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `5c9fadf20f994950df9f1b0630fdce1416fe4459ad23bcd20dfa6f22adbe4598`
