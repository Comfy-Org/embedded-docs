# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video, video reklamları için geliştirilmiş Creatify'ın sonradan eğitilmiş H3 modelini kullanarak referans görseller, videolar ve ses eşliğinde sesli bir video üretir. Her birinin neye katkıda bulunduğunu kontrol etmek için referansları prompt içinde `@Image1`, `@Video1` ve `@Audio1` olarak adlandırın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|----------|--------|
| `reference_images` | En fazla 9 referans görsel için büyütülebilir yuva (`image_1` ... `image_9`); bunlara prompt içinde bağlantı sırasına göre `@Image1` ... `@Image9` olarak başvurulur. En az bir görsel veya video gerekir ve toplamda en fazla 12 referans kullanılabilir. | IMAGE | Hayır | En fazla 9 görsel |
| `reference_videos` | En fazla 3 referans video için büyütülebilir yuva (`video_1` ... `video_3`); her biri en az 1 saniye uzunluğundadır. Prompt bunu devam ettirmeyi istediğinde sesleri yeniden kullanılır; prompt içindeki yeni bir replik bunun yerini alır. Toplamda en fazla 15 saniyelik referans video faturalandırılır. | VIDEO | Hayır | En fazla 3 video |
| `reference_audios` | En fazla 3 referans klip için büyütülebilir yuva (`audio_1` ... `audio_3`). Konuşma, sözcükleri değil sesi yönlendirir ve enstrümantal müzik ses parçası hâline gelebilir. | AUDIO | Hayır | En fazla 3 klip |
| `prompt` | Videoyu tanımlayan ve bağlı referanslara atıfta bulunan metin istemi. En az bir boşluk dışı karakter içermelidir. | STRING | Evet | Boş olmayan herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"768p"`). | COMBO | Evet | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"auto"` ilk referans görseli takip eder. Yalnızca referans videolar varken `"1088p"` çözünürlüğünde düğüm, ilk videoya en yakın desteklenen oranı seçer; bu oran videonun tam oranından farklı olabilir; diğer çözünürlüklerde `"auto"` olduğu gibi Creatify'a iletilir (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). `"2k"` değerinde en fazla 14 saniyedir. | INT | Evet | 1 ile 15 arası (adım 1) |
| `prompt_enhancement` | Creatify'ın promptu render etmeden önce nasıl yeniden yazacağı: `"auto"` ve `"ads"` onu bir video reklam promptuna dönüştürür ve konuşma satırları ekleyebilir, `"general"` onu diğer her tür video için yeniden yazar, `"none"` yazıldığı gibi render eder (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder. Boreal-H3'e seed gönderilmez; bu nedenle aynı girdilerle yeniden çalıştırmak farklı bir video üretebilir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:** en az bir referans görsel veya video bağlayın; yalnızca ses kabul edilmez. O türde bağlı referans sayısını aşan bir referans etiketi hata oluşturur; toplamda 12'den fazla referans da aynı hatayı verir. `"1088p"` ve `"auto"` kullanılırken referans görsel yoksa en-boy oranı ilk referans videodan alınır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `VIDEO` | Sesli olarak üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
