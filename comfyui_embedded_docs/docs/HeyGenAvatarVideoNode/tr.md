# HeyGen Avatar Video

Bir HeyGen avatarından konuşan sunucu videosu oluşturun. Bu düğüm, HeyGen'in işleme motorlarını kullanarak, sağladığınız metni konuşan veya kendi sesinizle dudak senkronizasyonu yapan bir yapay zeka avatarı videosu oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `motor` | İşleme motoru; her seçenek yalnızca onu destekleyen avatarları listeler. `"auto"` tüm avatarları sunar ve en iyi motorunu seçer (Avatar IV tercih edilir). Avatar V en yüksek sadakate sahiptir, Avatar III ise en uygun maliyetlidir. | DYNAMIC_COMBO | Evet | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `özel_avatar_id` | İsteğe bağlı HeyGen avatar görünüm kimliği. Ayarlandığında yukarıda seçilen avatarı geçersiz kılar. HeyGen'in 3000+ genel görünümünden (veya özel avatarlarınızdan) herhangi biri kullanılabilir. Varsayılan: `""`. | STRING | Hayır |  |
| `konuşma` | Avatarı bir metin betiği (HeyGen metinden konuşmaya) veya kendi sesinizle yönlendirin. Görünen ad: "speech source". | DYNAMIC_COMBO | Evet | `"script"`<br>`"audio"` |
| `çözünürlük` | Çıktı video çözünürlüğü. Varsayılan: `"1080p"`. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `en-boy oranı` | Çıktı en boy oranı. `"auto"` avatarın kaynak görüntüsünü takip eder. Varsayılan: `"auto"`. | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `arka plan rengi` | İsteğe bağlı düz arka plan rengi, hex kodu olarak (örn. `"#00ff00"`). Avatarın kendi arka planı için boş bırakın. Sağlanırsa değer `#` ile başlamalıdır. Varsayılan: `""`. | STRING | Hayır |  |
| `tohum` | HeyGen'e gönderilmez; yeniden çalıştırmaya zorlamak için değiştirin. Varsayılan: `42`. | INT | Hayır | Min: 0<br>Max: 2147483647 |

### `auto` Girdileri

`engine` `"auto"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Videoyu sunacak avatar görünümü (HeyGen'in genel kitaplığından seçilmiştir). Görünümün desteklediği en iyi motor otomatik olarak seçilir. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_iv` Girdileri

`engine` `"avatar_iv"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar IV motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_iii` Girdileri

`engine` `"avatar_iii"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar III motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `avatar_v` Girdileri

`engine` `"avatar_v"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Avatar V motorunu destekleyen avatar görünümleri. | COMBO | Evet | Birden çok seçenek mevcut |

### `script` Girdileri

`speech` `"script"` olduğunda aşağıdaki alt parametreler kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Avatarın konuşacağı metin (en fazla 5000 karakter). Oluşturulan konuşma en az 1 saniye uzunluğunda olmalıdır. Varsayılan: `""`. | STRING | Evet | Min: 1 karakter<br>Max: 5000 karakter |
| `voice` | Betik için ses. Varsayılan seçenek, HeyGen'in avatara atadığı sesi kullanır. `custom_voice_id` ayarlanmışsa yok sayılır. | COMBO | Evet | `"(avatar's default voice)"`<br>Birden çok genel ses seçeneği mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlandığında yukarıda seçilen sesi geçersiz kılar. HeyGen kitaplığındaki (2000+) herhangi bir ses kullanılabilir. Varsayılan: `""`. | STRING | Hayır |  |
| `voice_speed` | Konuşma hızı çarpanı. Varsayılan: `1.0`. | FLOAT | Hayır | Min: 0.5<br>Max: 1.5<br>Adım: 0.05 |

### `audio` Girdileri

`speech` `"audio"` olduğunda aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Avatarın dudak senkronizasyonu yapacağı ses, en fazla 10 dakika. | AUDIO | Evet |  |

Not: `engine` ve `speech`, seçilen değere bağlı olarak farklı alt parametreleri ortaya çıkaran seçicilerdir. `speech` seçicisinin birbirini dışlayan iki modu vardır: `"script"` modunda `text` gereklidir; `custom_voice_id` sağlanırsa `voice` yerine geçer. `"audio"` modunda avatar, sağlanan ses klibiyle dudak senkronizasyonu yapar. `background_color` sağlandığında `#` ile başlayan bir hex renk kodu olmalıdır. `custom_avatar_id` ayarlandığında `avatar` seçimini geçersiz kılar ve seçilen `engine`, o avatar görünümü tarafından desteklenmelidir; aksi halde `engine` `"auto"` olmadıkça bir hata oluşur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan avatar sunucu videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
