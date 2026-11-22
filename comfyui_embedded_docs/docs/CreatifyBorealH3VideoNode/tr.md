# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video, bir metin istemini, Creatify'nin video reklamları için geliştirilmiş sonradan eğitilmiş H3 modelini kullanarak sesli bir videoya dönüştürür. Durağan bir görüntüyü canlandırmak için bir ilk kare bağlayın; çekimi seçilen bir görüntüye oturtmak için isteğe bağlı olarak bir son kare bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Videoyu tanımlayan metin istemi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Boş olmayan herhangi bir metin |
| `ilk_kare` | Videonun başladığı görüntü. Bağlandığında, videonun görüntüyü izlemesi için `aspect_ratio` değerini `"auto"` olarak tutun. | IMAGE | Hayır | - |
| `son_kare` | Videonun üzerinde bittiği görüntü. Bağlı bir `first_frame` gerektirir. | IMAGE | Hayır | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü (varsayılan: `"768p"`). | COMBO | Evet | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. Bir ilk kare bağlı olduğunda `"auto"` ilk kareyi izler; bu durumda `"auto"` olarak bırakın (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `süre` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). `"2k"` değerinde maksimum 14 saniyedir. | INT | Evet | 1 ile 15 arası (adım: 1) |
| `istem iyileştirme` | Creatify'nin istemi render etmeden önce nasıl yeniden yazdığı: `"auto"` ve `"ads"` onu bir video reklam istemine dönüştürür ve konuşma replikleri ekleyebilir, `"general"` onu diğer herhangi bir video için yeniden yazar, `"none"` yazıldığı gibi render eder (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `tohum` | `seed`, düğümün yeniden çalışıp çalışmayacağını kontrol eder. Boreal-H3'e seed gönderilmez; bu nedenle aynı girdilerle yeniden çalıştırmak farklı bir video üretebilir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:** Bir `first_frame` olduğunda en-boy oranı her zaman görüntüden gelir; bu nedenle başka herhangi bir `aspect_ratio` değeri hata verir. Bir `first_frame` olmadan `last_frame` reddedilir ve `"2k"` değerinde 14 saniyenin üzerindeki `duration` reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sesli üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
