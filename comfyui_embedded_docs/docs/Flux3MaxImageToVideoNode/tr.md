# FLUX 3 Max Image to Video

FLUX 3 Max Image to Video, FLUX 3 Max ile 1 ila 10 görseli canlandırır. Her görsel klibin bir karesi olur: tek görsel klibi başlatır, iki görsel ilk ve son kare olur, daha fazlası klip boyunca yayılır veya seçtiğiniz zamanlara sabitlenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Sahnenin nasıl hareket edeceği ve seslendirileceği (varsayılan: boş). | STRING | Evet | Çok satırlı metin |
| `keyframes` | Genişletilebilir yuva: oynatma sırasına göre 1 ila 10 ana kare görselini bağlayın, ör. `image_1`, `image_2` ve benzeri. Her görsel klibin bir karesi olur. | IMAGE | Evet | 1 - 10 görsel |
| `placement` | `"spread across the clip"` ilk görseli başa, son görseli sona ve geri kalanları araya eşit şekilde yerleştirir; `"at times"` her görseli seçtiğiniz bir saniyeye sabitler (varsayılan: `"spread across the clip"`). | DYNAMIC_COMBO | Evet | `"spread across the clip"`<br>`"at times"` |
| `aspect_ratio` | Çıktı en-boy oranı. `"auto"` ilk ana kare görselini izler (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Klip uzunluğu saniye cinsinden (varsayılan: `"5"`). | COMBO | Evet | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Çıktı çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Modelin istemi oluşturmadan önce ne kadar akıl yürütüp genişleteceği. `"high"` daha uzun sürer; fiyat aynıdır (varsayılan: `"high"`). | COMBO | Evet | `"low"`<br>`"high"` |
| `generate_audio` | Senkronize ses oluştur. Kapalı seçildiğinde ses parçası olmayan bir video üretir (varsayılan: true). | BOOLEAN | Evet | `true`<br>`false` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden tohum. Sonuçlar bu değerden bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 - 2147483646 |

### at times Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `times` | Her görsel için saniye cinsinden bir zaman; virgülle ayrılmış ve artan sırada, ör. "0, 2.5, 5". Yalnızca `placement` değeri `"at times"` olduğunda görünür. | STRING | Hayır | Virgülle ayrılmış saniyeler |

Not: `prompt` en az bir karakter içermelidir. `keyframes` en az bir görsel içermeli ve 10'dan fazla görsel içeremez; toplu girdi her görsel için bir kez sayılır.

`placement` `"spread across the clip"` olarak ayarlandığında, bir veya iki görsel başlangıç görseli ve isteğe bağlı bir bitiş görseli olarak gönderilir; üç veya daha fazla görsel ise klip boyunca 24 fps'te eşit şekilde yayılan ana karelere yerleştirilir.

`placement` `"at times"` olarak ayarlandığında, `times` her görsel için bir değer vermeli ve bu değerler artmalı, negatif olamaz ve son zaman klip sonunun ötesinde olamaz.

Görüntülenen fiyat `resolution` ve `duration` değerlerine dayanır: 720p, 7 Kasım 2026'ya kadar saniye başına $0.060775 ve 1080p saniye başına $0.103675 olarak ücretlendirilir; bu tarihten sonra saniye başına $0.2431 ve $0.4147 olarak ücretlendirilir. Klip için toplam tahmini maliyet arayüzde gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen en-boy oranı, süre, çözünürlük ve ses ayarıyla ana kare görsellerinden oluşturulan video klip. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `fd8bbd627022f86d3ecb3482530a6c8c37d4225e32db36c35185eac318ed4c75`
