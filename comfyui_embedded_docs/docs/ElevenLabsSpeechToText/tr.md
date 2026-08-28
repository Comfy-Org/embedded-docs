# ElevenLabs Konuşmadan Metne

ElevenLabs Speech to Text düğümü, sesi ElevenLabs API'sini kullanarak metne dönüştürür. Otomatik dil algılama, konuşmacı diarizasyonu (farklı konuşmacıları tanımlama) ve ses olayı etiketleme (transkriptte kahkaha veya müzik gibi sesleri açıklama) özelliklerini destekler.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Transkripsiyon için kullanılacak model. Bu modeli seçmek ek parametreleri görüntüler. | DYNAMIC_COMBO | Evet | `"scribe_v2"` |
| `ses` | Transkripsiyonu yapılacak ses. | AUDIO | Evet | - |
| `dil_kodu` | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: "") | STRING | Hayır | - |
| `konuşmacı_sayısı` | Tahmin edilecek maksimum konuşmacı sayısı. Otomatik algılama için 0 olarak ayarlayın. (varsayılan: 0) | INT | Hayır | 0 - 32 |
| `tohum` | Tekrarlanabilirlik için tohum değeri (determinizm garanti edilmez). (varsayılan: 1) | INT | Hayır | 0 - 2147483647 |

### Scribe v2 Girdileri

Bu parametreler `"scribe_v2"` modeli seçildiğinde gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Transkriptte (kahkaha), (müzik) gibi sesleri açıklayın. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarize` | Hangi konuşmacının konuştuğunu açıklayın. (varsayılan: False) | BOOLEAN | Hayır | - |
| `diarization_threshold` | Konuşmacı ayrımı hassasiyeti. Düşük değerler konuşmacı değişikliklerine daha duyarlıdır. Yalnızca `diarize` etkinleştirildiğinde kullanılır. (varsayılan: 0.22) | FLOAT | Hayır | 0.1 - 0.4 |
| `temperature` | Rastgelelik kontrolü. 0.0 model varsayılanını kullanır. Daha yüksek değerler rastgeleliği artırır. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 2.0 |
| `timestamps_granularity` | Transkript kelimeleri için zamanlama hassasiyeti. (varsayılan: "word") | COMBO | Hayır | `"word"`<br>`"character"`<br>`"none"` |

**Not:** `diarize` etkinleştirildiğinde `num_speakers` 0'dan büyük bir değere ayarlanamaz. `diarize` özelliğini devre dışı bırakmanız veya `num_speakers` değerini 0 olarak ayarlamanız gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `metin` | Sesten elde edilen transkribe edilmiş metin. | STRING |
| `dil_kodu` | Sesin algılanan dil kodu. | STRING |
| `kelimeler_json` | Etkinleştirilmişse zaman damgaları ve konuşmacı etiketleri dahil olmak üzere ayrıntılı kelime düzeyinde bilgileri içeren JSON biçimli bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/tr.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
