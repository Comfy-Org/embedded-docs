# Breeze Text to Speech

Converts metni Breeze TTS 2 ile sese dönüştürür. Bir Breeze sesi seçin, metnin dilini belirleyin ve isteğe bağlı olarak satırın nasıl seslendirileceğini yönlendirin. İngilizce ve Çince, Breeze TTS 2 modellerinden herhangi birini kullanabilir; diğer tüm diller Breeze TTS 2 Multilingual kullanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voice` | Seslendirme için kullanılacak Breeze sesi; Breeze Voice Selector veya Breeze ses oluşturma düğümlerinden birinden alınır. | BREEZE_VOICE | Evet | - |
| `text` | Seslendirilecek metin, 1 ile 1000 karakter arası. `(laughs)` veya `(sighs)` gibi ses etiketleri okunmak yerine uygulanır. Varsayılan: boş. | STRING | Evet | 1 ile 1000 karakter arası |
| `language` | Metnin dili. İngilizce ve Çince iki modelden herhangi birini kullanabilir; diğer diller Breeze TTS 2 Multilingual kullanır. Bir ses en iyi kendi dilinde duyulur; bu nedenle başka bir dil için Breeze Voice Localize ile oluşturulmuş bir kopya kullanın. | DYNAMIC_COMBO | Evet | Birden çok seçenek mevcut |
| `delivery` | Satırın nasıl seslendirileceği: `neutral` sesi olduğu gibi tutar, `directed` yazılı talimatları izler. Varsayılan: `"neutral"`. | DYNAMIC_COMBO | Evet | `"neutral"`<br>`"directed"` |
| `speed` | Perdeyi değiştirmeden tempo çarpanı. Varsayılan: 1.0. | FLOAT | Hayır | 0.5 ile 2.0 arası (adım: 0.05) |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |

### Dil "English" ve "Chinese" Girdileri

Bunlar yalnızca `language` değeri English veya Chinese olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` veya `Breeze TTS 2 Multilingual`. Varsayılan: `"Breeze TTS 2"`. | COMBO | Evet | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Sunum "neutral" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `speaker_boost` | Sesi özgün sesine daha yakın tutar. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |

### Sunum "directed" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `instructions` | Metnin nasıl seslendirileceği; metinle aynı dilde yazılır. Varsayılan: boş. | STRING | Hayır | Çok satırlı metin |
| `strength` | Sesin talimatlara ne kadar güçlü uyduğu. Varsayılan: 4.0. | FLOAT | Hayır | 1.0 ile 10.0 arası (adım: 0.1) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | WAV sesi biçiminde oluşturulan konuşma. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`
