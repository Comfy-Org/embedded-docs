# ElevenLabs Metinden Konuşmaya

ElevenLabs Metin-Konuşma düğümü, yazılı metni ElevenLabs API'sini kullanarak sesli konuşmaya dönüştürür. Belirli bir ses seçmenize ve stabilite, hız ve stil gibi çeşitli konuşma özelliklerini ince ayarlayarak özelleştirilmiş bir ses çıktısı oluşturmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Ses sentezi için kullanılacak ses. Ses Seçici veya Anlık Ses Klonlama'dan bağlayın. | CUSTOM | Evet | Yok |
| `metin` | Sese dönüştürülecek metin. | STRING | Evet | Yok |
| `kararlılık` | Ses stabilitesi. Düşük değerler daha geniş duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton konuşma üretir (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `metin normalizasyonunu uygula` | Metin normalizasyon modu. 'auto' sistemin karar vermesini sağlar, 'on' her zaman normalizasyon uygular, 'off' atlar. | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Metin-konuşma için kullanılacak model. Bir model seçmek, o modele özgü parametreleri gösterir. | DYNAMICCOMBO | Hayır | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın (varsayılan: ""). | STRING | Hayır | Yok |
| `tohum` | Tekrarlanabilirlik için tohum değeri (determinizm garanti edilmez) (varsayılan: 1). | INT | Hayır | 0 - 2147483647 |
| `çıktı_formatı` | Ses çıktı formatı. | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Modele Özgü Parametreler:**
`model` parametresi `"eleven_multilingual_v2"` olarak ayarlandığında, aşağıdaki ek parametreler kullanılabilir hale gelir:

* `speed`: Konuşma hızı. 1.0 normal, <1.0 yavaş, >1.0 hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
* `similarity_boost`: Benzerlik artırma. Yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).
* `use_speaker_boost`: Orijinal konuşmacı sesine benzerliği artırır (varsayılan: False).
* `style`: Stil abartma. Yüksek değerler stilistik ifadeyi artırır ancak stabiliteyi azaltabilir (varsayılan: 0.0, aralık: 0.0 - 0.2).

`model` parametresi `"eleven_v3"` olarak ayarlandığında, aşağıdaki ek parametreler kullanılabilir hale gelir:

* `speed`: Konuşma hızı. 1.0 normal, <1.0 yavaş, >1.0 hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
* `similarity_boost`: Benzerlik artırma. Yüksek değerler sesi orijinale daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Metin-konuşma dönüşümünden oluşturulan ses. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `d11d4ffa2d1f11dfd5ce378d9496cd9788d2197bf7f4135092ecefb287f3c2f7`
