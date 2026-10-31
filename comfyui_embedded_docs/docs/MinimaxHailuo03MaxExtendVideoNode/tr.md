# MiniMax H3 Max Extend Video

Bu düğüm, bir videoyu istem ve isteğe bağlı ses referanslarıyla yönlendirilen yeni görüntülerle sürdürür. Kaynak video yüklenir, devamı oluşturulur ve sonuç ya yeniden işlenmiş videonun tamamı ya da yalnızca yeni görüntüler olarak döndürülür. İki model kullanılabilir: "MiniMax H3 Max" ve birim başına daha ucuz olan "MiniMax H3 Max Turbo".

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Videoyu sürdürmek için kullanılacak model. Her iki model de aşağıdaki aynı girdileri sunar. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### Model Girdileri

Bu girdiler her iki model için geçerlidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Uzatılacak video, 1.625 ila 60 saniye uzunluğunda, en fazla 50 MB. En-boy oranı 0.4 ile 2.5 arasında olmalıdır. | VIDEO | Evet | 1.625 ila 60 saniye |
| `prompt` | Bundan sonra ne olacağı. Kaynağı değil, devamı açıklayın. Referans seslere `@Audio1`..`@Audio3` şeklinde başvurun; örneğin "@Audio1 ses için". | STRING | Evet | 1 ila 50000 karakter |
| `reference_audios` | Genişletilebilir yuva: yeni görüntüler için en fazla 3 ses klibi (`audio_1`...`audio_3`) bağlayın; her biri en az 2 saniye ve toplamda 14.5 saniye olmalıdır. | AUDIO | Hayır | 0 ila 3 klip |
| `duration` | Eklenecek yeni görüntü süresi, saniye cinsinden (varsayılan: 5). | INT | Evet | 1 ila 15 |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | Çıktının en-boy oranı. "auto" kaynak videoyu takip eder; diğer değerler videoyu seçilen orana kırpar (varsayılan: "auto"). | COMBO | Evet | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | "extended", tüm videoyu seçilen çözünürlükte yeniden işlenmiş olarak ve yeni görüntülerle birlikte döndürür. "continuation" yalnızca yeni görüntüleri döndürür; kaynak videonun sonunun 1.6 saniyelik tekrarıyla başlar (varsayılan: "extended"). | COMBO | Evet | "extended"<br>"continuation" |
| `prompt_expansion` | Devamın tutarlı kalması için istemi kaynak videoyu kullanarak yeniden yazın. Aynı `seed` için tekrarlanabilir sonuçlar almak üzere kapatın (varsayılan: true). | BOOLEAN | Hayır | true<br>false |
| `seed` | Rastgele `seed`. Aynı `seed` ile yapılan aynı istek benzer sonuçlar verir; ancak birebir aynı sonuçlar garanti edilmez (varsayılan: 42). | INT | Evet | 0 ila 4294967295 |

### Parametre Kısıtlamaları

- 2K çözünürlükte "extended" çıktısı, kaynak video artı yeni görüntüler olmak üzere toplamda 45 saniye ile sınırlıdır. Daha uzun klipler için "continuation" veya daha düşük bir çözünürlük kullanın.
- Her referans ses klibi en az 2 saniye uzunluğunda olmalı ve hepsi birlikte 14.5 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | `output` ayarına bağlı olarak uzatılmış video veya yalnızca yeni görüntüler. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
