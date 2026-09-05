# MetaMuseImageTextToImageApi

Meta Muse Image Text to Image, Meta'nın Muse Image modelini kullanarak metin istemlerinden görüntüler üretir. Model, görüntüyü oluşturmadan önce istem üzerinde akıl yürütür; planlama sırasında web araması, görsel araması ve kod çalıştırma kullanabilir. Düğüm, Muse Image API'sini çağırır ve sonuçta elde edilen görüntüyü veya görüntüleri döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. | DYNAMIC_COMBO | Evet | `"muse-image-1.0"` |

Listeden bir model seçmek, o modelin desteklediği ayarları gösterir. Mevcut tek model `muse-image-1.0`'dır; ayarları aşağıda listelenmiştir.

### muse-image-1.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Görüntüyü tanımlayan istem. Model, işleme başlamadan önce istem üzerinde akıl yürütür ve yerleşik web ve görsel aramasını kullanabilir. | STRING | Evet | Çok satırlı metin, en az 1 karakter |
| `aspect_ratio` | Çıktının görüntü oranı. Görüntüler yaklaşık 2,5 megapiksel olarak işlenir (1:1 1600x1600, 16:9 2048x1152); "auto" modelin istemden seçim yapmasını sağlar. | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | Modelin işleme öncesinde ne kadar düşündüğü, plan yaptığı ve kendini iyileştirdiği. | COMBO | Evet | `"high"`<br>`"low"` |
| `enable_web_search` | Modelin görüntüyü planlarken gerçekler ve canlı bilgiler için web'de arama yapmasını sağlar. | BOOLEAN | Hayır | True<br>False (varsayılan: True) |
| `enable_image_search` | Modelin görüntüyü planlarken referans görselleri aramasını sağlar. | BOOLEAN | Hayır | True<br>False (varsayılan: True) |
| `enable_shell` | Modelin hassas düzenler, çizelgeler ve diyagramlar için planlama sırasında kod çalıştırmasını sağlar; kapalıyken miktarlar ve hizalama yaklaşık olarak belirlenir. | BOOLEAN | Hayır | True<br>False (varsayılan: True) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; API'de tohum bulunmadığından, gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. | INT | Evet | 0 – 2147483647 (varsayılan: 42) |

Not: İstem en az bir karakter içermelidir. `aspect_ratio` "auto" olarak ayarlandığında API'ye açık bir boyut gönderilmez ve model çıktı boyutuna istemden karar verir. `seed` parametresi yalnızca düğümün ne zaman yeniden çalışacağını kontrol eder; API'ye gönderilmez, bu nedenle üretilen sonuçlar deterministik değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | API tarafından döndürülen, kodu çözülen ve toplu görüntü olarak sağlanan üretilen görüntü. API yanıtı birden çok görüntü içeriyorsa, bunlar tek bir toplu işte birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
