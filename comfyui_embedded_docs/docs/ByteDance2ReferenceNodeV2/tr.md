# ByteDance Seedance 2.5 Referanstan Videoya

ByteDance Seedance 2.5 Reference to Video, metin istemi ve isteğe bağlı referans görseller, videolar, ses veya daha önce yüklenmiş kitaplık varlıkları rehberliğinde ByteDance Seedance modellerini (Seedance 2.5, 2.5 Draft, 2.0, 2.0 Fast ve 2.0 Mini) kullanarak video üretir, düzenler veya uzatır. Referansları yükler, bir oluşturma görevi gönderir, tamamlanmasını bekler ve tamamlanan video dosyasını döndürür. `Seedance 2.5 Draft` seçildiğinde bunun yerine hızlı bir 480p önizleme oluşturur; 1080p nihai videoyu oluşturmak için elde edilen `draft_task_id` çıktısını ByteDance Seedance 2.5 Draft to Final Video düğümüne bağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. En yeni model, 30 saniyeye kadar videolar ve mp4 çıktısı için Seedance 2.5; `draft_task_id` çıktısı ByteDance Seedance 2.5 Draft to Final Video düğümünde 1080p nihai videoyu oluşturan hızlı 480p önizleme için Seedance 2.5 Draft; maksimum kalite ve 4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı ve en düşük maliyetli oluşturma için Mini. Bir model seçmek, aşağıda gösterilen girdi bileşenlerini değiştirir. | DYNAMIC_COMBO | Evet | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 - 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan: False. Gelişmiş ayar. | BOOLEAN | Evet | true<br>false |

### Seedance 2.5 Girdileri

Bu girdiler `model` "Seedance 2.5" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşulan replikleri çift tırnak içine alın. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: 720p. | COMBO | Evet | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: 16:9. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-30). Varsayılan: 5. | INT | Evet | 4 - 30 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `task_type` | Referans medyasıyla ne yapılacağı. auto dışındaki her değer, görev gönderildiğinde doğrulanır; bu nedenle uyumsuz ayarlar oluşturma başlamadan önce başarısız olur.<br>auto: model görevi istemden ve girdilerden çıkarır; bunun yorumuyla çelişen ayarlar yalnızca oluşturma başladıktan sonra başarısız olur.<br>reference: referans görseller, videolar ve sesler rehberliğinde yeni bir video oluştur.<br>edit: bağlı bir referans videoyu değiştir (ekle, kaldır, değiştir); çıktı, kaynak klibin kendi uzunluğunu ve en-boy oranını korur ve `duration` ile `ratio` bileşenleri yok sayılır.<br>extend: bağlı bir referans videoyu ileri veya geri doğru sürdür; istem "extend forward", "extend backward" veya "continue" demelidir; en-boy oranı kaynak klibi izler ve çıktı, kaynak klibi değil, ayarladığınız sürede yalnızca yeni oluşturulan bölümü içerir. Varsayılan: auto. | COMBO | Evet | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Çıktı videosunun kapsayıcı biçimi. Varsayılan: mp4. | COMBO | Evet | "mp4" |

### Seedance 2.5 Draft Girdileri

Bu girdiler `model` "Seedance 2.5 Draft" olarak ayarlandığında görünür. Parametre kümesi yukarıdaki Seedance 2.5 ile eşleşir; ancak `resolution` yalnızca `"480p"` sunar (varsayılan `"480p"`).

### Seedance 2.0 Girdileri

Bu girdiler `model` "Seedance 2.0" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: adaptive. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan: 7. | INT | Evet | 4 - 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Bu girdiler `model` "Seedance 2.0 Fast" veya "Seedance 2.0 Mini" olarak ayarlandığında görünür. Her iki model de aynı girdi kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "480p"<br>"720p" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: adaptive. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan: 7. | INT | Evet | 4 - 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |

### Referans Girdileri

Bu büyütülebilir referans yuvaları tüm modeller için kullanılabilir. Maksimum yuva sayısı modele göre değişir: Seedance 2.5 en fazla 30 görsel, 10 video, 10 ses ve 30 varlık destekler; Seedance 2.0, 2.0 Fast ve 2.0 Mini en fazla 9 görsel, 3 video, 3 ses ve 9 varlık destekler.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Büyütülebilir yuva: çıktıyı yönlendiren 1..N referans görseli bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Görseller en-boy oranı (0,4 ila 2,5) açısından doğrulanır ve en uzun kenarı en fazla 6000 piksel olacak şekilde otomatik olarak küçültülür. | IMAGE | Hayır | 1..9 yuva (Seedance 2.0 ailesi)<br>1..30 yuva (Seedance 2.5) |
| `reference_videos` | Büyütülebilir yuva: 1..N referans videosu bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Her video en az 1,8 saniye uzunluğunda olmalı ve seçilen model ile çözünürlük için piksel sınırlarına uymalıdır. | VIDEO | Hayır | 1..3 yuva (Seedance 2.0 ailesi)<br>1..10 yuva (Seedance 2.5) |
| `reference_audios` | Büyütülebilir yuva: 1..N referans ses parçası bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Her ses en az 1,8 saniye uzunluğunda olmalıdır. | AUDIO | Hayır | 1..3 yuva (Seedance 2.0 ailesi)<br>1..10 yuva (Seedance 2.5) |
| `reference_assets` | Büyütülebilir yuva: Seedance sanal kitaplığına zaten yüklenmiş medya için 1..N varlık kimliği dizesi bağlayın. Her varlık Active olmalıdır. İstemde `asset1` veya `asset 1` gibi belirteçlerle bir varlığa başvurabilirsiniz; düğüm bunları varlığın konumsal etiketiyle (örneğin "Image 2" veya "Video 1") değiştirir. | STRING | Hayır | 1..9 yuva (Seedance 2.0 ailesi)<br>1..30 yuva (Seedance 2.5) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videolarını otomatik olarak küçült. En-boy oranı korunur; zaten sınırlar içinde olan videolara dokunulmaz. Varsayılan: True. | BOOLEAN | Hayır | true<br>false |
| `auto_upscale` | Seçilen çözünürlük için modelin minimum piksel sayısının altında kalan referans videolarını otomatik olarak büyüt. En-boy oranı korunur; minimumu zaten karşılayan videolara dokunulmaz. Not: düşük çözünürlüklü bir kaynağı büyütmek gerçek ayrıntı eklemez ve daha düşük kaliteli oluşturmalar üretebilir. Varsayılan: False. Gelişmiş ayar. | BOOLEAN | Hayır | true<br>false |

**Not:** Düğümü çalıştırmak için en az bir referans görsel, video veya varlık gereklidir (Seedance 2.5 ayrıca yalnızca sesli referansları da kabul eder). Referans videolar ve seslerin her biri en az 1,8 saniye uzunluğunda olmalıdır ve tüm referans videoların (ve ayrı olarak, tüm referans seslerin) toplam süresi seçilen modelin maksimum toplam saniyesini aşmamalıdır. Referans görseller yaklaşık 2:5 ile 5:2 arasında bir en-boy oranına (0,4 ila 2,5) sahip olmalı, en az 300x300 piksel olmalı ve otomatik olarak en uzun kenarı en fazla 6000 piksel olacak şekilde küçültülür. `task_type` "edit" ve "extend" seçenekleri yalnızca Seedance 2.5 ile kullanılabilir ve her ikisi de en az bir referans video gerektirir; "edit" kullanıldığında çıktı, kaynak klibin kendi uzunluğunu ve en-boy oranını korur ve `duration` ile `ratio` bileşenleri yok sayılır; "extend" kullanıldığında çıktı, ayarladığınız sürede yalnızca yeni oluşturulan bölümü içerir. Referans verilen varlıklar Active durumunda olmalıdır, aksi takdirde görev başarısız olur. Her çalıştırma görev kimliğini `draft_task_id` olarak döndürür, ancak yalnızca bir `Seedance 2.5 Draft` çalıştırmasının kimliği ByteDance Seedance 2.5 Draft to Final Video düğümü tarafından oluşturulabilir; bu nedenle başka herhangi bir modelle çıktı bağlantısız bırakılmalıdır, aksi takdirde çalıştırma başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturma görevi tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. Ses oluşturma etkinleştirildiğinde ses içerir. | VIDEO |
| `draft_task_id` | Çalıştırma tarafından döndürülen görev kimliği. Yalnızca bir `Seedance 2.5 Draft` çalıştırması, ByteDance Seedance 2.5 Draft to Final Video düğümünün oluşturabileceği bir taslak üretir; başka herhangi bir modelle çıktı bağlantısız bırakılmalıdır, aksi takdirde çalıştırma başarısız olur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
