> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/tr.md)

ElevenLabs Speech to Text düğümü, ses dosyalarını metne dönüştürür. ElevenLabs'ın API'sini kullanarak konuşulan kelimeleri yazılı bir transkripte çevirir; otomatik dil algılama, farklı konuşmacıları tanımlama ve müzik veya kahkaha gibi konuşma dışı sesleri etiketleme gibi özellikleri destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Transkripte dönüştürülecek ses. |
| `model` | COMBO | Evet | `"scribe_v2"` | Transkripsiyon için kullanılacak model. Bu model seçildiğinde ek parametreler görünür. |
| `tag_audio_events` | BOOLEAN | Hayır | - | Transkriptte (kahkaha), (müzik) vb. sesleri notlandırır. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür. (varsayılan: False) |
| `diarize` | BOOLEAN | Hayır | - | Hangi konuşmacının konuştuğunu notlandırır. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür. (varsayılan: False) |
| `diarization_threshold` | FLOAT | Hayır | 0.1 - 0.4 | Konuşmacı ayrımı hassasiyeti. Düşük değerler, konuşmacı değişikliklerine karşı daha hassastır. Bu parametre, `"scribe_v2"` modeli seçildiğinde ve `diarize` etkinleştirildiğinde görünür. (varsayılan: 0.22) |
| `temperature` | FLOAT | Hayır | 0.0 - 2.0 | Rastgelelik kontrolü. 0.0 modelin varsayılanını kullanır. Daha yüksek değerler rastgeleliği artırır. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür. (varsayılan: 0.0) |
| `timestamps_granularity` | COMBO | Hayır | `"word"`<br>`"character"`<br>`"none"` | Transkript kelimeleri için zaman damgası hassasiyeti. Bu parametre, `"scribe_v2"` modeli seçildiğinde görünür. (varsayılan: "word") |
| `language_code` | STRING | Hayır | - | ISO-639-1 veya ISO-639-3 dil kodu (örn., 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: "") |
| `num_speakers` | INT | Hayır | 0 - 32 | Tahmin edilecek maksimum konuşmacı sayısı. Otomatik algılama için 0 olarak ayarlayın. (varsayılan: 0) |
| `seed` | INT | Hayır | 0 - 2147483647 | Tekrarlanabilirlik için tohum (determinizm garanti edilmez). (varsayılan: 1) |

**Not:** `diarize` seçeneği etkinleştirildiğinde, `num_speakers` parametresi 0'dan büyük bir değere ayarlanamaz. Ya `diarize`'ı devre dışı bırakmalı ya da `num_speakers`'ı 0 olarak ayarlamalısınız.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | Sesten transkripte dönüştürülen metin. |
| `language_code` | STRING | Sesin algılanan dil kodu. |
| `words_json` | STRING | Zaman damgaları ve etkinleştirilmişse konuşmacı etiketleri de dahil olmak üzere ayrıntılı kelime düzeyinde bilgiler içeren JSON formatlı bir dize. |
