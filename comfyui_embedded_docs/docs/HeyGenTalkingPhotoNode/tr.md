# HeyGen Konuşan Fotoğraf

Bir kişinin durağan görüntüsünü, HeyGen'in Avatar IV teknolojisini kullanarak dudak senkronlu konuşan bir videoya dönüştürün. Animasyonu, HeyGen'in metinden konuşmaya dönüştürdüğü bir metin komut dosyasıyla veya avatarın dudak senkronu yapması için kendi sesinizi sağlayarak sürücüleyebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Animasyonu yapılacak kişinin görüntüsü. 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Evet | - |
| `konuşma` | Avatary bir metin komut dosyasıyla (HeyGen metinden konuşmaya) veya kendi sesinizle sürücüleyin. | DYNAMIC_COMBO | Evet | `"script"`<br>`"audio"` |
| `çözünürlük` | Çıktı video çözünürlüğü (varsayılan: `"1080p"`). | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `en boy oranı` | Çıktı en-boy oranı. `"auto"`, giriş görüntüsünü takip eder (varsayılan: `"auto"`). | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `ifadeler` | Animasyonlu yüzün ve jestlerin ne kadar etkileyici olduğu (varsayılan: `"low"`). | COMBO | Hayır | `"low"`<br>`"medium"`<br>`"high"` |
| `tohum` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 |

### Komut Dosyası Girdileri

`speech` değeri `"script"` olduğunda gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Avatarın konuşacağı metin (en fazla 5000 karakter). Üretilen konuşma en az 1 saniye uzunluğunda olmalıdır. (varsayılan: boş) | STRING | Evet | 1 ila 5000 karakter |
| `voice` | Komut dosyası için ses (HeyGen'in en popüler sesleri). | COMBO | Evet | Birden fazla seçenek mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlandığında, yukarıda seçilen sesi geçersiz kılar. HeyGen'in kitaplığındaki (2000+) herhangi bir ses kullanılabilir. (varsayılan: boş) | STRING | Hayır | - |
| `voice_speed` | Konuşma hızı çarpanı (varsayılan: 1.0). | FLOAT | Hayır | 0.5 ila 1.5 (adım 0.05) |

### Ses Girdileri

`speech` değeri `"audio"` olduğunda gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Avatarın dudak senkronu yapacağı, en fazla 10 dakikalık ses. | AUDIO | Evet | En fazla 10 dakika |

Not: `speech` değeri `"script"` olduğunda, `text` belirtilmeli ve `voice` seçici (avatarın varsayılan sesi dışında bir ses seçilerek) veya bir `custom_voice_id` aracılığıyla bir ses gerekir. `speech` değeri `"audio"` olduğunda ise bunun yerine `audio` gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Dudak senkronlu konuşma içeren, animasyonlu konuşan fotoğrafın üretilen videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
