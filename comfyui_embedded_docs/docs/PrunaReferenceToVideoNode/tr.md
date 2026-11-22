# Pruna P-Video-2 Pro Reference to Video

Pruna P-Video-2 Pro Reference to Video ile referans görüntüler, videolar ve seslerle yönlendirilen bir istemden video oluşturun. Her referansa istemde numarasıyla atıfta bulunun; model, konusunu, stilini veya hareketini sonuca taşır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Pruna video modeli. Bir model seçmek, girdilerini aşağıda gösterir. | DYNAMIC_COMBO | Evet | `"p-video-2-pro-reference"` |

### P-Video-2 Pro Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Referans görüntüler için büyütülebilir yuva (`image_1`, `image_2`, ...); istemde bağlantı sırasına göre `@Image1` ile `@Image9` arasında atıfta bulunulur. İlk ve son kareler dahil olmak üzere en fazla 9 görüntü. | AUTOGROW | Hayır | 0 ile 9 görsel arası |
| `model.videos` | Referans videolar için büyütülebilir yuva (`video_1`, `video_2`, ...); `@Video1` ile `@Video3` arasında atıfta bulunulur. Her biri en fazla 60 fps hızında 2 ile 15 saniye arasındadır; toplamda 15 saniye. 1080p üzerindeki videolar küçültülür. | AUTOGROW | Hayır | 0 ile 3 video arası |
| `model.audios` | Referans ses için büyütülebilir yuva (`audio_1`, `audio_2`, ...); `@Audio1` ile `@Audio3` arasında atıfta bulunulur. Toplamda en fazla 15 saniye. | AUTOGROW | Hayır | 0 ile 3 ses klibi arası |
| `model.prompt` | Videoyu açıklar. Referanslara `@Image1`, `@Video1` veya `@Audio1` olarak atıfta bulunun (varsayılan: boş). En fazla 5000 karakter. | STRING | Evet | 1 ile 5000 karakter arası |
| `model.first_frame` | Videonun başladığı görüntü. 9 görüntü sınırına dahil edilir. | IMAGE | Hayır | - |
| `model.last_frame` | Videonun bittiği görüntü. 9 görüntü sınırına dahil edilir. | IMAGE | Hayır | - |
| `model.keep_audio` | Bağlı sesi film müziği olarak kullanın ve videoyu buna uyacak şekilde oluşturun (varsayılan: False). Tam olarak bir ses gerektirir: daha kısa sesin ardından oluşturulan ses gelir; daha uzun ses ise süreye göre kesilir. | BOOLEAN | Evet | `True`<br>`False` |
| `model.duration` | Videonun saniye cinsinden uzunluğu (varsayılan: `"5"`). | COMBO | Evet | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `model.resolution` | Çıktı çözünürlüğü (varsayılan: `"768p"`). 1080p, 2k ve 4k, oluşturulan 768p videoyu üst ölçekler. | COMBO | Evet | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `model.mode` | `"cost"` daha ucuzdur, `"speed"` daha hızlı oluşturur (varsayılan: `"speed"`). | COMBO | Evet | `"cost"`<br>`"speed"` |
| `model.aspect_ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"16:9"`). `"adaptive"`, referanslar arasında en yaygın oranı kullanır; `enhance_prompt` açıkken yeniden yazılan istem bunun yerine oranı seçer. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.enhance_prompt` | Oluşturmadan önce istemi daha fazla ayrıntıyla yeniden yazın; `"max"` daha yavaştır (varsayılan: `"turbo"`). İstem referanslara numarayla atıfta bulunduğunda bunu açık tutun; ilk veya son kare her zaman `"turbo"` kullanır. Gelişmiş ayar. | COMBO | Evet | `"off"`<br>`"turbo"`<br>`"max"` |
| `model.seed` | Oluşturma için tohum (varsayılan: 42). Aynı tohum, yalnızca `model.enhance_prompt` kapalıyken bir sonucu tam olarak yeniden üretir. | INT | Evet | 0 ile 2147483647 arası<br>Adım: 1 |

**Notlar:**

- En az bir referans görüntü, video, ilk kare veya son kare bağlayın; aksi takdirde düğüm bir hatayla durur.
- İlk ve son kareler dahil olmak üzere 9 görüntüye ve görüntüler, kareler, videolar ve sesler arasında toplamda 12 referansa izin verilir.
- Referans video ve referans ses ayrı ayrı toplamda 15 saniye ile sınırlıdır ve her bir referans video, en fazla 60 fps hızında 2 ile 15 saniye uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
