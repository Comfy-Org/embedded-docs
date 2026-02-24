> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/tr.md)

ElevenLabs Metinden Sese düğümü, ElevenLabs API'sini kullanarak yazılı metni konuşulan sese dönüştürür. Belirli bir ses seçmenize ve kararlılık, hız ve stil gibi çeşitli konuşma özelliklerini ince ayarlayarak özelleştirilmiş bir ses çıktısı oluşturmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Evet | N/A | Konuşma sentezi için kullanılacak ses. Ses Seçici veya Anında Ses Klonlama düğümünden bağlayın. |
| `text` | STRING | Evet | N/A | Sese dönüştürülecek metin. |
| `stability` | FLOAT | Hayır | 0.0 - 1.0 | Ses kararlılığı. Düşük değerler daha geniş bir duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton bir konuşma üretir (varsayılan: 0.5). |
| `apply_text_normalization` | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` | Metin normalleştirme modu. 'auto' sisteme karar verme izni verir, 'on' her zaman normalleştirme uygular, 'off' atlar. |
| `model` | DYNAMICCOMBO | Hayır | `"eleven_multilingual_v2"`<br>`"eleven_v3"` | Metinden sese dönüşüm için kullanılacak model. Bir model seçmek, o modele özgü parametreleri görünür kılar. |
| `language_code` | STRING | Hayır | N/A | ISO-639-1 veya ISO-639-3 dil kodu (örn. 'en', 'es', 'fra'). Otomatik algılama için boş bırakın (varsayılan: ""). |
| `seed` | INT | Hayır | 0 - 2147483647 | Tekrarlanabilirlik için tohum (determinizm garanti edilmez) (varsayılan: 1). |
| `output_format` | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` | Ses çıktı formatı. |

**Modele Özgü Parametreler:**
`model` parametresi `"eleven_multilingual_v2"` olarak ayarlandığında, aşağıdaki ek parametreler kullanılabilir hale gelir:
*   `speed`: Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
*   `similarity_boost`: Benzerlik artırımı. Daha yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).
*   `use_speaker_boost`: Orijinal konuşmacı sesine benzerliği artırır (varsayılan: False).
*   `style`: Stil abartısı. Daha yüksek değerler stilistik ifadeyi artırır ancak kararlılığı azaltabilir (varsayılan: 0.0, aralık: 0.0 - 0.2).

`model` parametresi `"eleven_v3"` olarak ayarlandığında, aşağıdaki ek parametreler kullanılabilir hale gelir:
*   `speed`: Konuşma hızı. 1.0 normaldir, <1.0 daha yavaş, >1.0 daha hızlı (varsayılan: 1.0, aralık: 0.7 - 1.3).
*   `similarity_boost`: Benzerlik artırımı. Daha yüksek değerler sesi orijinaline daha benzer hale getirir (varsayılan: 0.75, aralık: 0.0 - 1.0).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Metinden sese dönüşümden elde edilen oluşturulmuş ses. |