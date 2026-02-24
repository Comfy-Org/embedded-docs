> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/tr.md)

ElevenLabs Text to Sound Effects düğümü, bir metin açıklamasından ses efektleri oluşturur. ElevenLabs API'sini kullanarak isteminize dayalı ses efektleri oluşturur ve süre, döngü davranışı ile sesin metni ne kadar yakından takip ettiğini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | Yok | Oluşturulacak ses efektinin metin açıklaması. Bu zorunlu bir alandır. |
| `model` | COMBO | Evet | `"eleven_sfx_v2"` | Ses efekti oluşturmak için kullanılacak model. Bu model seçildiğinde ek parametreler görünür: `duration` (varsayılan: 5.0, aralık: 0.5 ila 30.0 saniye), `loop` (varsayılan: False) ve `prompt_influence` (varsayılan: 0.3, aralık: 0.0 ila 1.0). |
| `output_format` | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` | Ses çıktı formatı. |

**Parametre Detayları:**

* **`model["duration"]`**: Oluşturulan sesin saniye cinsinden süresi. Varsayılan 5.0'dır, minimum 0.5 ve maksimum 30.0'dır.
* **`model["loop"]`**: Etkinleştirildiğinde, sorunsuz bir şekilde döngü yapan bir ses efekti oluşturur. Varsayılan değer False'dur.
* **`model["prompt_influence"]`**: Oluşturmanın metin istemini ne kadar yakından takip ettiğini kontrol eder. Daha yüksek değerler, sesin metni daha yakından takip etmesini sağlar. Varsayılan 0.3'tür ve aralığı 0.0 ila 1.0'dır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Oluşturulan ses efekti ses dosyası. |
