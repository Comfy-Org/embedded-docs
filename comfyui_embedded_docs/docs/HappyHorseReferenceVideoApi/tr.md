# HappyHorse Referanstan Videoya

Bu düğüm, HappyHorse modelini kullanarak referans görüntülerinde yer alan bir kişiyi veya nesneyi içeren bir video oluşturur. Tek karakter performanslarını ve çok karakterli etkileşimleri destekler. Referans görüntüler yüklenir ve oluşturulan videodaki karakterleri temsil etmek için kullanılır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılacak HappyHorse referanstan videoya modeli. | COMBO | Evet | `"happyhorse-1.1-r2v"`<br>`"happyhorse-1.0-r2v"` |
| `tohum` | Oluşturma için kullanılacak tohum (varsayılan: 0). Her oluşturmadan sonra otomatik olarak değişecek şekilde ayarlanabilir. | INT | Hayır | 0 ile 2147483647 arası |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | True veya False |

### HappyHorse 1.1 Girdileri (happyhorse-1.1-r2v)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videoyu tanımlayan istem. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. | STRING | Evet | Yok |
| `resolution` | Oluşturulan videonun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | Oluşturulan videonun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"`<br>`"5:4"`<br>`"4:5"` |
| `duration` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 ile 15 arası |

### HappyHorse 1.0 Girdileri (happyhorse-1.0-r2v)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videoyu tanımlayan istem. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. | STRING | Evet | Yok |
| `resolution` | Oluşturulan videonun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | Oluşturulan videonun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 ile 15 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: videoda yer alacak kişiye veya nesneye ait 1 ila 9 arasında referans görüntüsü bağlayın. En az bir referans görüntüsü sağlanmalıdır. | IMAGE | Evet | 1 ila 9 (model başına) |

Not: En az bir referans görüntüsü sağlanmalıdır, aksi takdirde düğüm bir hata verir. Her referans görüntüsü en az 400 x 400 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. İstem boş olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`
