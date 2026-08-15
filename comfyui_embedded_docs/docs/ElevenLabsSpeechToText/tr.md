# ElevenLabs Konuşmadan Metne

ElevenLabs Speech to Text düğümü, ElevenLabs'ın konuşmayı metne dönüştürme API'sini kullanarak sesi metne dönüştürür. Otomatik dil algılamayı, hangi konuşmacının konuştuğunu belirlemeyi ve dökümde (kahkaha) veya (müzik) gibi konuşma dışı sesleri etiketlemeyi destekler.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yazıya dökme için kullanılacak model. Bir model seçmek, o modele özgü parametreleri gösterir. | DYNAMIC_COMBO | Evet | `"scribe_v2"` |
| `ses` | Yazıya dökülecek ses. | AUDIO | Evet | - |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (ör. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: "") | STRING | Hayır | - |
| `konuşmacı_sayısı` | Tahmin edilecek maksimum konuşmacı sayısı. Otomatik algılama için 0 olarak ayarlayın. (varsayılan: 0) | INT | Hayır | 0 - 32 |
| `tohum` | Tekrarlanabilirlik için tohum (determinizm garanti edilmez). (varsayılan: 1) | INT | Hayır | 0 - 2147483647 |

### Scribe v2 Girdileri

Bu parametreler, `"scribe_v2"` modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Dökümde (kahkaha), (müzik) vb. sesleri etiketleyin. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarize` | Hangi konuşmacının konuştuğunu etiketleyin. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarization_threshold` | Konuşmacı ayırma hassasiyeti. Daha düşük değerler konuşmacı değişimlerine daha duyarlıdır. Yalnızca `diarize` etkinleştirildiğinde kullanılır. (varsayılan: 0.22) | FLOAT | Hayır | 0.1 - 0.4 |
| `temperature` | Rastgelelik kontrolü. 0.0 model varsayılanını kullanır. Daha yüksek değerler rastgeleliği artırır. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 2.0 |
| `timestamps_granularity` | Döküm sözcükleri için zamanlama hassasiyeti. (varsayılan: "word") | COMBO | Hayır | `"word"`<br>`"character"`<br>`"none"` |

**Not:** `diarize` etkinleştirildiğinde `num_speakers` 0'dan büyük bir değere ayarlanamaz. `diarize` özelliğini devre dışı bırakın veya `num_speakers` değerini 0 olarak ayarlayın; aksi takdirde bir hata oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `metin` | Ses dosyasından yazıya dökülen metin. | STRING |
| `dil_kodu` | Sesin algılanan dil kodu. | STRING |
| `kelimeler_json` | Etkinleştirilirse zaman damgaları ve konuşmacı etiketleri dahil olmak üzere sözcük düzeyinde ayrıntılı bilgi içeren JSON biçimli bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/tr.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
