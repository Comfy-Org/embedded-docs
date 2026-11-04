# Pika H3 Flex Video

Bu düğüm, bir metin isteminden senkronize sesli video oluşturur; isteğe bağlı olarak bir ilk kare, bir son kare veya her ikisiyle sabitlenebilir. Pika H3 Flex, Pika'nın sonradan eğitilmiş MiniMax H3 modelidir: görüntüyü ve sesini tek geçişte oluşturur; çözünürlük, en-boy oranı ve süreyi siz ayarlarsınız. Hiç kare bağlı değilken düğüm metinden videoya çalışır; bir kare bağlamak onu görüntüden videoya geçirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videoda ne olacağı, istediğiniz ses de dahil. Boş olamaz. Varsayılan: "" (boş dize). | STRING | Evet | 1 ile 8000 karakter arası |
| `first_frame` | Açılış karesi olarak kullanılan isteğe bağlı görüntü. Bağlandığında metinden videoya yerine görüntüden videoya çalışır. | IMAGE | Hayır | - |
| `last_frame` | Kapanış karesi olarak kullanılan isteğe bağlı görüntü. `first_frame` ile birlikte veya tek başına kullanılabilir. | IMAGE | Hayır | - |
| `resolution` | Çıktı çözünürlüğü. `"1080p"` ve üzeri, 768p'de oluşturur ve bir kez büyütür. 480p'de aynı seed farklı bir video verir. Varsayılan: `"768p"`. | COMBO | Evet | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Çıktı en-boy oranı. `"auto"` ilk bağlanan kareyi, aksi takdirde istemi takip eder. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Saniye cinsinden klip uzunluğu. Çıktı uzunluğu bir kare ızgarasını izler: 5 saniye 124 kare, yaklaşık 5,17 saniye verir. Varsayılan: 5. | INT | Evet | 5 ile 15 saniye arası |
| `rewrite_prompt` | Önce Pika'nın istemi genişletmesine izin verin. Aynı seed daha sonra her çalıştırmada farklı bir video verir. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `seed` | Örnekleme için seed. `rewrite_prompt` kapalıyken aynı seed videoyu tam olarak yineler; ancak aynı seed ile yerel bir çalıştırma farklı bir sonuç verir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:**

* İstem 1 ile 8000 karakter arasında olmalıdır.
* Faturalandırma, seçilen çözünürlüğe ve klip uzunluğuna göre yapılır ve çıktının saniyesi başına hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Senkronize sesiyle birlikte oluşturulan klip. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `63a90fc5874ed861db3c0821e702cfcd1a14650f09459b242b4ec5e3ba5b0cd5`
