# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video, Creatify'ın video reklamları için sonradan eğittiği H3 modelini kullanarak referans görüntüler, videolar ve ses rehberliğinde sesli bir video oluşturur. Her birinin neye katkıda bulunduğunu kontrol etmek için istemde referansları `@Image1`, `@Video1` ve `@Audio1` olarak adlandırın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | En fazla 9 referans görüntü için büyütülebilir yuva (`image_1` ... `image_9`); istemde bağlantı sırasına göre `@Image1` ... `@Image9` olarak anılır. En az bir görüntü veya video gereklidir ve toplamda en fazla 12 referans olabilir. | IMAGE | Hayır | En fazla 9 görüntü |
| `reference_videos` | En fazla 3 referans video için büyütülebilir yuva (`video_1` ... `video_3`); her biri en az 1 saniye uzunluğundadır. İstem onu sürdürmeyi istediğinde sesleri yeniden kullanılır; istemdeki yeni bir satır onu değiştirir. Toplamda en fazla 15 saniyelik referans video faturalandırılır. | VIDEO | Hayır | En fazla 3 video |
| `reference_audios` | En fazla 3 referans klip için büyütülebilir yuva (`audio_1` ... `audio_3`). Konuşma, sözcüklerden ziyade sesi yönlendirir ve enstrümantal müzik film müziği hâline gelebilir. | AUDIO | Hayır | En fazla 3 klip |
| `prompt` | Videoyu tanımlayan ve bağlı referanslara atıfta bulunan metin istemi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Boş olmayan herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"768p"`). | COMBO | Evet | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"auto"`, ilk referans görüntüyü veya görüntü bağlı değilse ilk referans videoyu izler (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). `"2k"` değerinde maksimum 14 saniyedir. | INT | Evet | 1 ile 15 arası (adım: 1) |
| `prompt_enhancement` | Creatify'ın istemi oluşturmadan önce nasıl yeniden yazdığı: `"auto"` ve `"ads"` onu bir video reklam istemine dönüştürür ve konuşulan satırlar ekleyebilir, `"general"` onu diğer tüm videolar için yeniden yazar, `"none"` yazıldığı gibi oluşturur (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | `seed`, düğümün yeniden çalışıp çalışmayacağını kontrol eder. Creatify kendi rastgeleliğini seçtiğinden, aynı girdiler aynı videoyu yalnızca `prompt_enhancement` `"none"` olarak ayarlandığında verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:** en az bir referans görüntü veya video bağlayın; yalnızca ses kabul edilmez. O türde bağlı referans sayısının ötesine işaret eden bir referans etiketi hata oluşturur; toplamda 12'den fazla referans da hata oluşturur. `"1088p"` ve `"auto"` ile referans görüntü yokken en-boy oranı ilk referans videodan alınır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sesli oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
