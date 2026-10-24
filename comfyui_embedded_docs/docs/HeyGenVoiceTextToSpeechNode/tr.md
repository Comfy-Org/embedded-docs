# HeyGen Voice 1.0 Text to Speech

Metni, HeyGen Voice 1.0 Instant Clone ile klonlanmış bir seste konuşturur. Düğüm, metni ve ses kimliğini HeyGen'e gönderir ve oluşturulan konuşmayı ses olarak döndürür. İki model mevcuttur: `heygen-voice-1` ve daha hızlı ve daha ucuz `heygen-voice-1-turbo`.

Bir `model` seçildiğinde, o modele özgü parametreler görünür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-voice-1-turbo` daha hızlıdır ve daha ucuzdur. Bir model seçildiğinde, o modele özgü parametreler görünür: `voice_id`, `text`, `language` ve `expressiveness_boost`. | DYNAMIC_COMBO | Evet | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | HeyGen Voice 1.0 Instant Clone'dan ses (varsayılan: boş). | STRING | Evet | N/A |
| `text` | Konuşturulacak metin. En fazla 5000 karakter; yaklaşık 12 dakikadan uzun konuşmalar başarısız olur, bu nedenle çok uzun Çince veya Japonca metinleri bölün (varsayılan: boş). | STRING | Evet | 1 ila 5000 karakter |
| `language` | Metnin dili. Sırpça veya Malayca gibi otomatik algılamanın karıştırabileceği yakın akraba diller için ayarlayın (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>Birden çok dil ön ayarı |
| `expressiveness_boost` | Yüksek değerler daha ifade edici; düşük değerler orijinal sese daha yakın kalır (varsayılan: 0.5). | FLOAT | Evet | 0.0 ila 1.0 (adım 0.05) |

**Not:** `voice_id`, HeyGen Voice 1.0 Instant Clone tarafından oluşturulmuş bir ses olmalıdır; boş olduğunda düğüm hatayla durur. `text` en az bir karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Metinden oluşturulan, klonlanmış seste seslendirilen konuşma. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/tr.md)

---
**Source fingerprint (SHA-256):** `936cb63237681779dd4d9a74d048afae93160638d069be6b16e5855d333e584a`
