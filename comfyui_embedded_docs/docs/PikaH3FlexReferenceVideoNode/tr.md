# Pika H3 Flex Reference to Video

Bu düğüm, referans görüntüler, videolar ve ses klipleri rehberliğinde senkronize sesli bir video oluşturur veya düzenler. Pika H3 Flex, Pika'nın sonradan eğitilmiş MiniMax H3 modelidir. Referansları bağlayın ve istemde bağlantı sırasına göre `@Image1`, `@Video1` veya `@Audio1` olarak adresleyin. En az bir referans görüntü veya video gereklidir ve toplamda en fazla 12 referans bağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | En fazla 9 görüntü; istemde bağlantı sırasına göre `@Image1` ile `@Image9` arası olarak adreslenir. En az bir görüntü veya video gereklidir. | AUTOGROW | Hayır | 0 ile 9 görsel arası |
| `reference_videos` | En fazla 3 klip; istemde bağlantı sırasına göre `@Video1` ile `@Video3` arası olarak adreslenir. Her klip 2 ile 15 saniye arasında olmalı ve klipler toplamda 15 saniye veya daha az olmalıdır. Saniye başına ücretlendirilir. | AUTOGROW | Hayır | 0 ile 3 video arası |
| `reference_audios` | En fazla 3 klip; istemde `@Audio1` ile `@Audio3` arası olarak adreslenir. Her klip 2 ile 15 saniye arasında olmalı ve klipler toplamda 15 saniye veya daha az olmalıdır. Çıktıya kopyalandığında, klipler bağlantı sırasına göre, bağlı videoların sesinden önce çalar. | AUTOGROW | Hayır | 0 ile 3 ses klibi arası |
| `prompt` | Ne oluşturulacağı veya yapılacak düzenleme. Referanslara `@Image1`, `@Video1`, `@Audio1` veya `<Picture 1>`, `<Video 1>`, `<Audio 1>` olarak başvurun. Boş olmamalıdır. Varsayılan: "" (boş dize). | STRING | Evet | 1 ile 8000 karakter arası |
| `reference_video_audio` | Bağlı videoların sesini çıktıya kopyalar. Yeni ortam sesi veya yeni müzikle hareket aktarımı için kapatın. İstemde diyalog içermeyen bir konuşan kafa daha sonra uydurma konuşma alır. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `resolution` | Çıktı çözünürlüğü. `"1080p"` ve üzeri 768p'de oluşturur ve bir kez yükseltir. 480p'de aynı tohum farklı bir video verir. Varsayılan: `"768p"`. | COMBO | Evet | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Çıktı en boy oranı. `"auto"` bir referans videoyu takip eder, aksi takdirde istemi takip eder. Referans görüntüler bunu etkilemez. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Klibin saniye cinsinden uzunluğu. Çıktı uzunluğu bir kare ızgarasını takip eder: 5 saniye 124 kare verir, yaklaşık 5.17 saniye. Varsayılan: 5. | INT | Evet | 5 ile 15 saniye arası |
| `rewrite_prompt` | Pika'nın istemi önce genişletmesine izin verin. Aynı tohum daha sonra her çalıştırmada farklı bir video verir. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `seed` | Örnekleme için tohum. `rewrite_prompt` kapalıyken, aynı tohum videoyu tam olarak tekrarlar, ancak aynı tohumla yerel bir çalıştırma farklı bir sonuç verir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:**

* En az bir referans görüntü veya video gereklidir.
* Toplamda en fazla 12 referans bağlanabilir; görüntüler, videolar ve ses klipleri birlikte sayılır.
* Her referans video ve ses klibi 2 ile 15 saniye arasında olmalıdır; videolar toplamda 15 saniye veya daha az, ses klipleri ise 15 saniye veya daha az olmalıdır.
* İstem 1 ile 8000 karakter arasında olmalıdır.
* Bağlı olmayan bir yuvaya başvurmak, örneğin iki görüntü sağlanmışken `@Image3` belirtmek, bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Senkronize sesiyle birlikte oluşturulan veya düzenlenen klip. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c6d8700e3bb0c4ed7663aff55d477314af566568bd6db353fc21d6249ddd93bd`
