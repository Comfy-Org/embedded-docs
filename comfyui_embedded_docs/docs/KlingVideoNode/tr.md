> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/tr.md)

Bu düğüm, Kling V3 modelini kullanarak videolar oluşturur. İki ana modu destekler: metinden videoya, burada bir metin açıklamasından video oluşturulur ve görüntüden videoya, burada mevcut bir görüntü canlandırılır. Ayrıca, her bölüm için farklı yönlendirmelerle (storyboard'lar) çok parçalı videolar oluşturma ve isteğe bağlı olarak eşlik eden ses üretme gibi gelişmiş özellikler sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `multi_shot` | COMBO | Evet | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Tek bir video mu yoksa her biri için ayrı yönlendirmeler ve süreler içeren bir dizi bölüm mü oluşturulacağını kontrol eder. "disabled" dışında bir değer olduğunda, her storyboard'un yönlendirmesi ve süresi için ek girişler görünür. |
| `generate_audio` | BOOLEAN | Evet | `True` / `False` | Etkinleştirildiğinde, düğüm video için ses oluşturur. Varsayılan `True` değerindedir. |
| `model` | COMBO | Evet | `"kling-v3"` | Model ve ilişkili ayarları. Bu seçeneğin seçilmesi, `resolution` ve `aspect_ratio` alt parametrelerini ortaya çıkarır. |
| `model.resolution` | COMBO | Evet | `"4k"`<br>`"1080p"`<br>`"720p"` | Oluşturulan video için çözünürlük. Bu ayar, `model` "kling-v3" olarak ayarlandığında kullanılabilir. |
| `model.aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan video için en boy oranı. Bu ayar, `start_frame` için bir görüntü sağlandığında (görüntüden videoya modu) dikkate alınmaz. `model` "kling-v3" olarak ayarlandığında kullanılabilir. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Oluşturma için bir tohum değeri. Bu değerin değiştirilmesi düğümün yeniden çalışmasına neden olur, ancak sonuçlar deterministik değildir. Varsayılan `0` değerindedir. |
| `start_frame` | IMAGE | Hayır | - | İsteğe bağlı bir başlangıç görüntüsü. Bağlandığında, düğüm metinden videoya modundan görüntüden videoya moduna geçer ve sağlanan görüntüyü canlandırır. |

**`multi_shot` modu için girişler:**

* `multi_shot` **"disabled"** olarak ayarlandığında, aşağıdaki girişler görünür:
  * `prompt` (STRING): Video için ana metin açıklaması. Zorunlu. 1 ile 2500 karakter arasında olmalıdır.
  * `negative_prompt` (STRING): Videoda ne olmaması gerektiğini açıklayan metin. İsteğe bağlı.
  * `duration` (INT): Videonun saniye cinsinden uzunluğu. 3 ile 15 arasında olmalıdır. Varsayılan `5` değerindedir.
* `multi_shot` bir storyboard seçeneğine (ör. `"3 storyboards"`) ayarlandığında, her storyboard bölümü için girişler görünür (ör. `storyboard_1_prompt`, `storyboard_1_duration`). Her yönlendirme 1 ile 512 karakter arasında olmalıdır. **Tüm storyboard sürelerinin toplamı** 3 ile 15 saniye arasında olmalıdır.

**Kısıtlamalar:**

* Düğüm, `start_frame` bağlı olmadığında **metinden videoya** modunda çalışır. Bu modda `model.aspect_ratio` ayarını kullanır.
* Düğüm, `start_frame` bağlı olduğunda **görüntüden videoya** modunda çalışır. `model.aspect_ratio` ayarı dikkate alınmaz. Giriş görüntüsü en az 300x300 piksel olmalı ve 1:2,5 ile 2,5:1 arasında bir en boy oranına sahip olmalıdır.
* Storyboard modunda (`multi_shot` "disabled" değil), ana `prompt` ve `negative_prompt` girişleri gizlenir ve kullanılmaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `f7f827d657b1d057d273eba3215ce6848d3ea05c5f348e2f3fccccfdd030dfc3`
