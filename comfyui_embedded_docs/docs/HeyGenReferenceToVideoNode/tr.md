# HeyGen Video 1.0 Reference to Video

HeyGen Video 1.0 kullanarak bir metin isteminden senkronize diyalog ve ses içeren bir video oluşturun; isteğe bağlı olarak bağlı referans materyaliyle yönlendirilebilir. İnsan, ürün veya yer görselleri, yeniden kullanılacak videolar ve ses sağlayan ses klipleri referans olarak kullanılabilir. İstemde her referanstan @Image1, @Video1 veya @Audio1 olarak bahsedin; girdilerin bağlanma sırasına göre her tür için numaralandırılır: bu etiketler HeyGen'in beklediği etiketlere dönüştürülür ve bağlı olmayan bir referansa işaret eden etiket hata verir. Herhangi bir referans görsel veya video olmadan düğüm, metinden videoya oluşturma olarak çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılan model sürümü. (varsayılan: `"heygen-video-1"`) | DYNAMIC_COMBO | Evet | `"heygen-video-1"` |
| `prompt` | Videonun açıklaması, herhangi bir diyalog dahil. Bağlı referanslara @Image1, @Video1, @Audio1 olarak başvurun; girdi sırasına göre her tür için numaralandırılır. (varsayılan: boş dize) | STRING | Evet | 1 ila 32000 karakter |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 5 ila 15 |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: `"768p"`) | COMBO | Evet | `"768p"`<br>`"480p"` |
| `aspect_ratio` | Çıktı en-boy oranı. Bağlı referans yoksa `"auto"` 16:9 olur; aksi takdirde ilk referans görselini veya görsel bağlı değilse ilk referans videosunu takip eder. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Oluşturma için seed. Aynı seed ile çalıştırmalar arasında sonuçlar yine de değişebilir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |
| `reference_images` | Genişletilebilir yuva: videoda kullanılacak insan, ürün veya yer görselleri (`image_1` ... `image_9`); bunlara @Image1, @Image2, ... olarak başvurun. Her girdi tam olarak bir görsel içermelidir ve her görselin en-boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Hayır | 0 ila 9 görsel |
| `reference_videos` | Genişletilebilir yuva: referans olarak kullanılacak videolar (`video_1` ... `video_3`); bunlara @Video1, @Video2, ... olarak başvurun. | VIDEO | Hayır | 0 ila 3 video |
| `reference_audios` | Genişletilebilir yuva: bir konuşmacının sesi gibi ses klipleri (`audio_1` ... `audio_3`); bunlara @Audio1, @Audio2, ... olarak başvurun. En az bir referans görsel veya video gerektirir. Bir ses referansı birkaç saniyelik temiz konuşma gerektirir ve yaklaşık 2 saniyeden kısa klipler genellikle yok sayılır. | AUDIO | Hayır | 0 ila 3 ses klibi |

### Parametre Kısıtlamaları

- **Referans sınırı:** `reference_images`, `reference_videos` ve `reference_audios` genelinde toplamda en fazla 12 referans; daha fazlasını bağlamak hata verir.
- **Ses, görsel veya video gerektirir:** referans görsel ve referans video bağlı değilken referans ses reddedilir.
- **Referans görsel kuralları:** her `reference_images` girdisi tam olarak bir görsel içermelidir (bir toplu iş reddedilir) ve her görselin en-boy oranı 1:4 ile 4:1 arasında olmalıdır.
- **İstem etiketleri:** `@ImageN`, `@VideoN` ve `@AudioN` büyük/küçük harfe duyarsız olarak eşleştirilir. Sayı, o türde bağlı referans sayısını aşmamalıdır ve istem, boşluklar kırpıldıktan sonra boş olmamalıdır.
- **Mod:** en az bir referans görsel veya videoyla istek, referanstan videoya çalıştırmasıdır; hiçbiri yoksa düz metinden videoya çalıştırmasıdır.
- **Seed:** seed yalnızca düğümün yeniden çalıştırılıp çalıştırılmayacağını belirler; sonuçlar aynı seed ile tekrarlanabilir değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Senkronize diyalog ve ses içeren oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `44de381703821043aa1399e58c9132f9b6a2b0ac5dbf47197dffed0438ea7ad7`
