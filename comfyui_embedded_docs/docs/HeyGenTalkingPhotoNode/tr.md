# HeyGenTalkingPhotoNode

Bir kişinin durağan fotoğrafını, HeyGen'in Avatar IV teknolojisini kullanarak dudak senkronizasyonlu konuşan bir videoya dönüştürün. Animasyonu, HeyGen'in sese dönüştürdüğü bir metin komut dosyasıyla yönlendirebilir veya avatarın dudak senkronizasyonu yapması için kendi sesinizi sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Canlandırılacak kişinin görüntüsü. 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Evet | - |
| `speech` | Avatari bir metin komut dosyası (HeyGen metinden sese) veya kendi sesinizle yönlendirin. | COMBO | Evet | `"script"`<br>`"audio"` |
| `text` | Avatarın söyleyeceği metin (en fazla 5000 karakter). Oluşturulan konuşma en az 1 saniye uzunluğunda olmalıdır. | STRING | Evet (konuşma "script" olduğunda) | - |
| `voice` | Komut dosyası için ses (HeyGen'in en popüler sesleri). | COMBO | Evet (konuşma "script" olduğunda) | Birden çok seçenek mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlandığında, yukarıda seçilen sesi geçersiz kılar. HeyGen'in kitaplığındaki (2000+) herhangi bir ses kullanılabilir. | STRING | Hayır | - |
| `voice_speed` | Konuşma hızı çarpanı (varsayılan: 1.0). | FLOAT | Hayır | 0.5 ila 1.5 |
| `audio` | Avatarın dudak senkronizasyonu yapacağı, en fazla 10 dakikalık ses. | AUDIO | Evet (konuşma "audio" olduğunda) | - |
| `resolution` | Çıktı video çözünürlüğü (varsayılan: "1080p"). | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı en boy oranı. 'auto', giriş görüntüsünü takip eder (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Canlandırılan yüzün ve jestlerin ne kadar ifade dolu olduğu (varsayılan: "low"). | COMBO | Hayır | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin (varsayılan: 42). | INT | Hayır | 0 ila 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Dudak senkronizasyonlu konuşma ile canlandırılmış konuşan fotoğrafın oluşturulan videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
