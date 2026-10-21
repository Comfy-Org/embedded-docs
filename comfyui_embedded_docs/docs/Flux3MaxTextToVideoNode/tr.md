# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video, bir metin isteminden senkronize ses içeren video oluşturur. İstem, render işleminden önce FLUX 3 Max tarafından yorumlanır ve genişletilir; düğüm render işleminin bitmesini bekler ve tamamlanan klip döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Klibin ne göstermesi gerektiğini sade bir dille açıklayın. Katmanlı ses için ortam sesini, müziği ve konuşmayı ayrı ayrı tanımlayın (varsayılan: boş). | STRING | Evet | Çok satırlı metin |
| `aspect_ratio` | Çıktı en-boy oranı. Metin istemleri için `"auto"` 16:9'dur (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Klip uzunluğu saniye cinsinden (varsayılan: `"5"`). | COMBO | Evet | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Çıktı çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Modelin oluşturmadan önce istem hakkında ne kadar akıl yürüteceği ve istemi ne kadar genişleteceği. `"high"` daha uzun sürer; fiyat aynıdır (varsayılan: `"high"`). | COMBO | Evet | `"low"`<br>`"high"` |
| `generate_audio` | Senkronize ses oluştur. Kapalı olduğunda ses parçası olmayan bir video üretir (varsayılan: true). | BOOLEAN | Evet | `true`<br>`false` |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eden tohum. Bu değerden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 42). | INT | Evet | 0 - 2147483646 |

Not: `prompt` en az bir karakter içermelidir. Görüntülenen fiyat `resolution` ve `duration` değerlerine dayanır: 7 Kasım 2026 tarihine kadar 720p için saniye başına $0.060775 ve 1080p için saniye başına $0.103675, bu tarihten sonra ise saniye başına $0.2431 ve $0.4147 uygulanır. Klip için tahmini toplam maliyet kullanıcı arayüzünde gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video klip; `generate_audio` etkinleştirildiğinde senkronize ses içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
