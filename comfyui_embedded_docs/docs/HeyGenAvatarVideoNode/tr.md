# HeyGenAvatarVideoNode

Bir HeyGen avatarından konuşan sunucu videosu oluşturun. Bu düğüm, HeyGen'in işleme motorlarını kullanarak, sağladığınız metni okuyan veya kendi sesinize dudak senkronizasyonu yapan bir yapay zeka avatar videosu oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `engine` | İşleme motoru; her seçenek yalnızca onu destekleyen avatarları listeler. 'auto' tüm avatarları sunar ve bunlar için en iyi motoru seçer (Avatar IV tercih edilir). Avatar V en yüksek kalitedir, Avatar III ise en uygun fiyatlıdır. | COMBO | Evet | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | İsteğe bağlı HeyGen avatar görünüm kimliği. Ayarlandığında, yukarıda seçilen avatarı geçersiz kılar. HeyGen'in 3000'den fazla herkese açık görünümünden (veya özel avatarlarınızdan) herhangi biri kullanılabilir. | STRING | Hayır |  |
| `speech` | Avatara bir metin komut dosyası (HeyGen metinden sese) veya kendi sesinizle yön verin. | COMBO | Evet | `"script"`<br>`"audio"` |
| `resolution` | Çıktı video çözünürlüğü (varsayılan: "1080p"). | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı en boy oranı. 'auto', avatarın kaynak görüntüsünü takip eder (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Onaltılık kod olarak isteğe bağlı düz arka plan rengi (örn. '#00ff00'). Avatarın kendi arka planı için boş bırakın. | STRING | Hayır |  |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin (varsayılan: 42). | INT | Hayır | Min: 0<br>Maks: 2147483647 |

`speech` parametresi `"script"` olarak ayarlandığında, aşağıdaki alt parametreler kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Avatarın konuşması için metin (en fazla 5000 karakter). Oluşturulan konuşma en az 1 saniye uzunluğunda olmalıdır. | STRING | Evet |  |
| `voice` | Komut dosyası için ses. Varsayılan seçenek, HeyGen'in avatara atadığı sesi kullanır. | COMBO | Evet | Birden çok seçenek mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlanırsa, yukarıda seçilen sesi geçersiz kılar. HeyGen'in kütüphanesindeki (2000'den fazla) herhangi bir ses kullanılabilir. | STRING | Hayır |  |
| `voice_speed` | Konuşma hızı çarpanı (varsayılan: 1.0). | FLOAT | Hayır | Min: 0.5<br>Maks: 1.5<br>Adım: 0.05 |

`speech` parametresi `"audio"` olarak ayarlandığında, aşağıdaki alt parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Avatarın dudak senkronizasyonu yapacağı, en fazla 10 dakikalık ses. | AUDIO | Evet |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan avatar sunucu videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
