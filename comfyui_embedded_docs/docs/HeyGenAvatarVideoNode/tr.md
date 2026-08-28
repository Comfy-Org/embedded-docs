# HeyGen Avatar Video

Bir HeyGen avatarından konuşan sunucu videosu oluşturur. Bu düğüm, HeyGen'in işleme motorlarını kullanarak sağladığınız metni söyleyen veya kendi sesinize dudak senkronu yapan bir yapay zeka avatarının videosunu oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `motor` | İşleme motoru; her seçenek yalnızca onu destekleyen avatarları listeler. "auto" tüm avatarları sunar ve her biri için en iyi motoru seçer (Avatar IV tercih edilir). Avatar V en yüksek kalitedir, Avatar III en uygun maliyetlidir. | DYNAMIC_COMBO | Evet | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `özel_avatar_id` | İsteğe bağlı HeyGen avatar görünüm kimliği. Ayarlanırsa yukarıda seçilen avatarı geçersiz kılar. HeyGen'in 3000'den fazla herkese açık görünümünden (veya özel avatarlarınızdan) herhangi biri kullanılabilir. Varsayılan: boş dize. | STRING | Hayır |  |
| `konuşma` | Avatarı bir metin komut dosyasıyla (HeyGen metinden konuşmaya) veya kendi sesinizle yönlendirin. | DYNAMIC_COMBO | Evet | `"script"`<br>`"audio"` |
| `çözünürlük` | Çıktı video çözünürlüğü. Varsayılan: `"1080p"`. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `en-boy oranı` | Çıktı en-boy oranı. "auto" avatarın kaynak görüntüsünü izler. Varsayılan: `"auto"`. | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `arka plan rengi` | Onaltılı kod olarak isteğe bağlı düz arka plan rengi (örn. `"#00ff00"`). Avatarın kendi arka planı için boş bırakın. Sağlanırsa değer `#` ile başlamalıdır. Varsayılan: boş dize. | STRING | Hayır |  |
| `tohum` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin. Varsayılan: `42`. | INT | Hayır | Min: 0<br>Maks: 2147483647 |

### `auto` Girdileri

`engine` `"auto"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Videoyu sunacak avatar görünümü (HeyGen'in herkese açık kitaplığından seçilir). Görünümün desteklediği en iyi motor otomatik olarak seçilir. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_iv` Girdileri

`engine` `"avatar_iv"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar IV motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_iii` Girdileri

`engine` `"avatar_iii"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar III motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_v` Girdileri

`engine` `"avatar_v"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar V motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `script` Girdileri

`speech` `"script"` olduğunda aşağıdaki alt parametreler kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Avatarın söyleyeceği metin (en fazla 5000 karakter). Üretilen konuşma en az 1 saniye uzunluğunda olmalıdır. Varsayılan: boş dize. | STRING | Evet | Min: 1 karakter<br>Maks: 5000 karakter |
| `voice` | Komut dosyası için ses. Varsayılan seçenek, HeyGen'in avatara atadığı sesi kullanır. | COMBO | Evet | `"(avatarın varsayılan sesi)"`<br>Birden çok genel ses seçeneği mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlanırsa yukarıda seçilen sesi geçersiz kılar. HeyGen'in kitaplığındaki (2000+) herhangi bir ses kullanılabilir. Varsayılan: boş dize. | STRING | Hayır |  |
| `voice_speed` | Konuşma hızı çarpanı. Varsayılan: `1.0`. | FLOAT | Hayır | Min: 0.5<br>Maks: 1.5<br>Adım: 0.05 |

### `audio` Girdileri

`speech` `"audio"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Avatarın dudak senkronu yapacağı ses, en fazla 10 dakika. | AUDIO | Evet |  |

Not: `speech`, birbirini dışlayan iki modu olan bir kaynak seçicidir. `"script"` modunda `text` zorunludur (1 ila 5000 karakter); `custom_voice_id` sağlanırsa `voice` değerini geçersiz kılar. `"audio"` modunda avatar, sağlanan ses klibine dudak senkronu yapar. `background_color`, sağlandığında `#` ile başlayan onaltılı bir renk kodu olmalıdır. `custom_avatar_id` ayarlandığında `avatar` seçimini geçersiz kılar ve seçilen `engine` bu avatar görünümü tarafından desteklenmelidir; aksi takdirde bir hata oluşur (`engine` `"auto"` değilse).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan avatar sunucu videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
