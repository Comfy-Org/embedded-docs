# ElevenLabs Konuşmadan Metne

ElevenLabs Speech to Text düğümü, ses dosyalarını metne dönüştürür. ElevenLabs API'sini kullanarak konuşulan kelimeleri yazılı bir metne çevirir; otomatik dil algılama, farklı konuşmacıları tanımlama ve müzik veya kahkaha gibi konuşma dışı sesleri etiketleme gibi özellikleri destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Transkripsiyonu yapılacak ses. | AUDIO | Evet | - |
| `model` | Transkripsiyon için kullanılacak model. Bu modelin seçilmesi ek parametreleri ortaya çıkarır. | COMBO | Evet | `"scribe_v2"` |
| `tag_audio_events` | Transkriptte (kahkaha), (müzik) vb. sesleri etiketleyin. Bu parametre, `"scribe_v2"` modeli seçildiğinde ortaya çıkar. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarize` | Hangi konuşmacının konuştuğunu etiketleyin. Bu parametre, `"scribe_v2"` modeli seçildiğinde ortaya çıkar. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarization_threshold` | Konuşmacı ayrımı hassasiyeti. Daha düşük değerler konuşmacı değişikliklerine daha duyarlıdır. Bu parametre, `"scribe_v2"` modeli seçildiğinde ve `diarize` etkinleştirildiğinde ortaya çıkar. (varsayılan: 0.22) | FLOAT | Hayır | 0.1 - 0.4 |
| `temperature` | Rastgelelik kontrolü. 0.0 model varsayılanını kullanır. Daha yüksek değerler rastgeleliği artırır. Bu parametre, `"scribe_v2"` modeli seçildiğinde ortaya çıkar. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 2.0 |
| `timestamps_granularity` | Transkript kelimeleri için zamanlama hassasiyeti. Bu parametre, `"scribe_v2"` modeli seçildiğinde ortaya çıkar. (varsayılan: "word") | COMBO | Hayır | `"word"`<br>`"character"`<br>`"none"` |
| `language_code` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: "") | STRING | Hayır | - |
| `num_speakers` | Tahmin edilecek maksimum konuşmacı sayısı. Otomatik algılama için 0 olarak ayarlayın. (varsayılan: 0) | INT | Hayır | 0 - 32 |
| `seed` | Yeniden üretilebilirlik için tohum değeri (determinizm garanti edilmez). (varsayılan: 1) | INT | Hayır | 0 - 2147483647 |

**Not:** `diarize` seçeneği etkinleştirildiğinde `num_speakers` parametresi 0'dan büyük bir değere ayarlanamaz. `diarize` seçeneğini devre dışı bırakmanız veya `num_speakers` değerini 0 olarak ayarlamanız gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `text` | Sesten elde edilen transkripsiyon metni. | STRING |
| `language_code` | Sesin algılanan dil kodu. | STRING |
| `words_json` | Etkinleştirilmişse zaman damgaları ve konuşmacı etiketleri dahil olmak üzere ayrıntılı kelime düzeyinde bilgi içeren JSON biçimli bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/tr.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
