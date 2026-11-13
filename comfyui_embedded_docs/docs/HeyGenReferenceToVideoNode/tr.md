# HeyGen Video 1.0 Referanstan Videoya

HeyGen Video 1.0 kullanarak bir metin isteminden senkronize diyalog ve ses içeren bir video oluşturun; isteğe bağlı olarak bağlı referans materyalleriyle yönlendirilebilir. İnsan, ürün veya yer görüntüleri, yeniden kullanılacak videolar ve ses sağlayan ses klipleri referans olarak kullanılabilir. İstemde her referanstan @Image1, @Video1 veya @Audio1 olarak bahsedin; bunlar girdilerin bağlanma sırasına göre tür başına numaralandırılır: bu etiketler HeyGen'in beklediği etiketlere dönüştürülür ve bağlı olmayan bir referansa işaret eden etiket hata verir. Herhangi bir referans görüntü veya video olmadan düğüm metinden videoya oluşturma olarak çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Oluşturma için kullanılan model sürümü. (varsayılan: `"heygen-video-1"`) | DYNAMIC_COMBO | Evet | `"heygen-video-1"` |
| `prompt` | Videonun açıklaması, varsa diyalog dahil. Bağlı referanslara @Image1, @Video1, @Audio1 olarak atıfta bulunun; girdi sırasına göre tür başına numaralandırılır. (varsayılan: boş dize) | STRING | Evet | 1 ile 16000 karakter arası |
| `duration` | Çıktı videosunun saniye cinsinden süresi. 15 saniyeden fazlası yalnızca referans görüntü ve video olmadan kullanılabilir. (varsayılan: 5) | INT | Evet | 5 ile 30 arası |
| `resolution` | Çıktı çözünürlüğü. 1080p ve 2k, 16:9 veya 9:16 en-boy oranını gerektirir; 'auto' bu çözünürlüklerde yalnızca referans olmadan çalışır. (varsayılan: `"768p"`) | COMBO | Evet | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı en-boy oranı. Hiç referans bağlı değilken `"auto"` 16:9'dur; aksi halde ilk referans görüntüyü veya hiç görüntü bağlı değilken ilk referans videoyu izler. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Oluşturma için tohum. Sonuçlar aynı tohumla çalıştırmalar arasında yine de değişebilir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 arası |
| `reference_images` | Büyütülebilir yuva: videoda kullanılacak insan, ürün veya yer görüntüleri (`image_1` ... `image_9`); bunlara @Image1, @Image2, ... olarak atıfta bulunun. Her girdi tam olarak bir görüntü içermelidir ve her görüntünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Hayır | 0 ile 9 görsel arası |
| `reference_videos` | Büyütülebilir yuva: referans olarak kullanılacak videolar (`video_1` ... `video_3`); bunlara @Video1, @Video2, ... olarak atıfta bulunun. Toplamda en fazla 15 saniyelik görüntü kullanılır. | VIDEO | Hayır | 0 ile 3 video arası |
| `reference_audios` | Büyütülebilir yuva: bir konuşmacı için ses gibi ses klipleri (`audio_1` ... `audio_3`); bunlara @Audio1, @Audio2, ... olarak atıfta bulunun. En az bir referans görüntü veya video gerektirir. Bir ses referansı birkaç saniyelik temiz konuşma gerektirir ve yaklaşık 2 saniyeden kısa klipler genellikle yok sayılır. | AUDIO | Hayır | 0 ile 3 ses klibi arası |
| `auto_duration` | Etkinleştirildiğinde, video uzunluğu istemde alıntılanan diyaloğu izler (8 ile 30 saniye arası veya referans görüntü ya da videolar varken 8 ile 15 saniye arası) ve `duration` yok sayılır. (varsayılan: `"disabled"`) | COMBO | Hayır | `"disabled"`<br>`"enabled"` |

### Parametre Kısıtlamaları

- **Referans sınırı:** toplamda en fazla 15 referans: en fazla 9 görüntü, 3 video ve 3 ses klibi. Daha fazlasını bağlamak hata verir.
- **Ses, görüntü veya video gerektirir:** ne referans görüntü ne de referans video bağlı değilken referans ses reddedilir.
- **Referans görüntü kuralları:** her `reference_images` girdisi tam olarak bir görüntü içermelidir (toplu girdi reddedilir) ve her görüntünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır.
- **İstem etiketleri:** `@ImageN`, `@VideoN` ve `@AudioN` büyük/küçük harf duyarsız olarak eşleştirilir. Sayı, o türde bağlı referansların sayısını aşmamalıdır ve istem, boşluklar kırpıldıktan sonra boş olmamalıdır.
- **Mod:** en az bir referans görüntü veya video varsa istek referanstan videoya oluşturma olarak çalıştırılır; hiçbiri yoksa düz metinden videoya oluşturma olarak çalıştırılır.
- **1080p ve 2k çözünürlük:** `resolution` `"1080p"` veya `"2k"`, `aspect_ratio` `"16:9"` veya `"9:16"` gerektirir; `"auto"` bu çözünürlüklerde yalnızca ne referans görüntü ne de referans video bağlı değilken kabul edilir.
- **Süre:** 15 saniyenin üzeri, `auto_duration` `"enabled"` olmadıkça yalnızca referans görüntü veya video olmadan kullanılabilir.
- **Tohum:** tohum yalnızca düğümün yeniden çalışıp çalışmayacağını belirler; sonuçlar aynı tohumla yeniden üretilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `VIDEO` | Senkronize diyalog ve ses içeren oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `415ffca1c385936e35bdb0451a23f03756e936b3b871d8d6a958da1ef8c56c36`
