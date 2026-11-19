# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video, metin istemini sesli bir videoya dönüştürür; bunu video reklamları için geliştirilmiş Creatify'ın sonradan eğitilmiş H3 modelini kullanarak yapar. Bir hareketsiz görüntüyü canlandırmak için bir ilk kare bağlayın ve isteğe bağlı olarak çekimi seçilen bir görüntüde sonlandırmak için bir son kare bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videoyu tanımlayan metin istemi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Boş olmayan herhangi bir metin |
| `first_frame` | Videonun başladığı görüntü. Bağlandığında, videonun görüntüyü izlemesi için `aspect_ratio` değerini `"auto"` olarak bırakın. | IMAGE | Hayır | - |
| `last_frame` | Videonun sonlandığı görüntü. Bağlı bir `first_frame` gerektirir. | IMAGE | Hayır | - |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"768p"`). | COMBO | Evet | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. Bir ilk kare bağlı olduğunda `"auto"` ilk kareyi izler; bu durumda `"auto"` olarak bırakın (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). `"2k"` değerinde maksimum 14 saniyedir. | INT | Evet | 1 ile 15 arası (adım 1) |
| `prompt_enhancement` | Creatify'ın istemi oluşturmadan önce nasıl yeniden yazdığı: `"auto"` ve `"ads"` onu bir video reklam istemine dönüştürür ve seslendirilmiş replikler ekleyebilir, `"general"` onu diğer tüm videolar için yeniden yazar, `"none"` yazıldığı gibi oluşturur (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | `seed`, düğümün yeniden çalışıp çalışmayacağını kontrol eder. Creatify kendi rastgeleliğini seçer; bu nedenle aynı girdiler aynı videoyu yalnızca `prompt_enhancement` `"none"` olarak ayarlandığında verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:** bir `first_frame` ile en-boy oranı her zaman görüntüden gelir; bu nedenle diğer herhangi bir `aspect_ratio` değeri hata oluşturur. `first_frame` olmadan bir `last_frame` reddedilir ve `"2k"` değerinde 14 saniyenin üzerindeki `duration` reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sesli olarak oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
