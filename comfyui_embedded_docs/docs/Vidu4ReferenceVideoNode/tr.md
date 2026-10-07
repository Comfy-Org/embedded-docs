# Vidu Q4 Reference-to-Video Generation

Referans görüntülerden, isteğe bağlı referans sesten ve bir istemden Vidu Q4 modeliyle video üretin. Bu, Vidu Q4 üretim düğümlerinin referanstan videoya varyantıdır.

Bir `model` seçmek, ona özgü parametreleri gösterir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `reference_images`, `reference_audios`, `prompt`, `aspect_ratio`, `resolution`, `duration`, `audio` ve `seed`. | DYNAMIC_COMBO | Evet | `"Vidu Q4 Preview"` |
| `reference_images` | Genişletilebilir yuva: üretilen video için bir veya daha fazla referans görüntüsü (`image_1`, `image_2`, ...) bağlayın; bir toplu işteki her görüntü toplam sayıya dahil edilir. İstemde bunlara sırayla başvurun: görüntü 1, görüntü 2, vb. | IMAGE | Evet | En fazla 15 görüntü |
| `reference_audios` | Genişletilebilir yuva: isteğe bağlı ses referanslarını (`audio_1`, `audio_2`, `audio_3`) bağlayın; her biri 3 ila 12 saniyedir. Yalnızca ses kullanılır, sözcükler değil: diyaloğu istemde yazın ve sırayla bir ses atayın, örneğin `image 1 says "Hello!" in the voice from audio 1`. `audio` etkinleştirilmiş olmalıdır. | AUDIO | Hayır | En fazla 3 klip |
| `prompt` | Video üretimi için metinsel açıklama; en fazla 5000 karakter. Kullanmak istediğiniz referansları tanımlamak için gereklidir. | STRING | Evet | Herhangi bir metin |
| `aspect_ratio` | Çıktı videosunun en boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 - 16 |
| `audio` | Etkinleştirildiğinde, diyalog ve ses efektleri dahil olmak üzere sesli video çıkarır (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevine sahiptir (varsayılan: 42). | INT | Evet | 1 - 2147483647 |

**Not:** Toplamda en fazla 15 referans görüntüsü kullanılabilir; bir toplu işteki her görüntü sayılır. Her görüntü en az 128x128 piksel olmalı ve en boy oranı 1:5 ile 5:1 arasında olmalıdır. Referans sesi, `audio` etkinleştirilmiş olmasını gerektirir; aksi halde hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`
