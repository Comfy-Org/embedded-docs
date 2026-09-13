# MiniMax H3 İlk-Son-Kare'den Videoya

Bu düğüm, MiniMax H3 modellerini kullanarak bir ilk kare görüntüsünden ve isteğe bağlı olarak bir son kare görüntüsünden video oluşturur. `model` seçicisi hangi oluşturma ayarlarının ve kısıtlamaların geçerli olacağını değiştirir; oluşturulan videonun en-boy oranı sağlanan görüntüleri takip eder.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. Bir model seçmek, aşağıda o modele özgü ayarları görünür kılar. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Video için ilk kare görüntüsü. Oluşturulan video bu görüntünün en-boy oranını takip eder. | IMAGE | Evet | - |
| `last_frame` | Video için isteğe bağlı son kare görüntüsü. Sağlandığında video, ilk kareden bu son kareye doğru oluşturulur. | IMAGE | Hayır | - |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer sonuçlar verir ancak aynı sonuçlar garanti edilmez. Bir "oluşturma sonrası kontrol" seçeneği içerir. Varsayılan: 42. | INT | Evet | 0 - 4294967295 |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği. Bu gelişmiş bir parametredir. Yalnızca `MiniMax H3` modeli tarafından desteklenir. Varsayılan: False. | BOOLEAN | Evet | True<br>False |

### MiniMax H3 Girdileri

Bu ayarlar, `model` seçicisinde `MiniMax H3` seçildiğinde gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturmak için metin istemi. En az bir boşluk dışı karakter içermelidir. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `duration` | Çıktı videosunun saniye cinsinden süresi. Varsayılan: 5. | INT | Evet | 4 - 15 |

### MiniMax H3 Max ve MiniMax H3 Max Turbo Girdileri

Bu ayarlar hem `MiniMax H3 Max` hem de `MiniMax H3 Max Turbo` tarafından paylaşılır. İki modelden birinin seçilmesi aynı ayarları görünür kılar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturmak için metin istemi. Boş veya yalnızca boşluklardan oluşan bir değer olmamalıdır ve 50.000 karakterle sınırlıdır. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: 768P. | COMBO | Evet | "480P"<br>"768P" |
| `duration` | Çıktı videosunun saniye cinsinden süresi. Varsayılan: 5. | INT | Evet | 5 - 15 |
| `prompt_expansion_mode` | Oluşturmadan önce istemin yeniden yazılması için ne kadar çaba harcanacağı. Varsayılan: balanced. | COMBO | Evet | "balanced"<br>"quality" |

**Kısıtlamalar hakkında notlar:**

- İstem metin içermelidir: boş veya yalnızca boşluklardan oluşan istemler reddedilir.
- Sağlanan her kare görüntüsü en az 256 piksel genişliğinde ve 256 piksel yüksekliğinde olmalı ve genişlik-yükseklik en-boy oranı 0,4 ile 2,5 arasında olmalıdır (yaklaşık 2:5 ila 5:2). Bu gereksinim `first_frame` için ve sağlandığında `last_frame` için geçerlidir.
- `last_frame` atlandığında, video yalnızca ilk kareden oluşturulur.
- Çıktı videosu, sağlanan görüntülerin en-boy oranını takip eder.
- `watermark` yalnızca `MiniMax H3` tarafından desteklenir. `MiniMax H3 Max` veya `MiniMax H3 Max Turbo` ile etkinleştirilmesi bir hataya neden olur.
- Süre, `MiniMax H3` için 4 ila 15 saniye, `MiniMax H3 Max` ve `MiniMax H3 Max Turbo` için 5 ila 15 saniye arasındadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen MiniMax H3 modeli kullanılarak ilk kareden ve isteğe bağlı son kareden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
