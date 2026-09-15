# ByteDance Seed Audio 1.0

ByteDance Seed Audio 1.0 ile tek bir istemden konuşma, müzik, ses efektleri ve çok konuşmacılı diyalog oluşturun. İstemde ses(leri), duyguyu, ortam sesini, arka plan müziğini ve ses efektlerini tanımlayın ve söylenecek replikleri ekleyin. İsteğe bağlı olarak yerleşik bir ön ayarlı ses seçin, en fazla 3 referans klipten sesleri klonlayın (istemde @Audio1-3 olarak etiketlenir) veya bir karakter görselinden ses türetin. Her çalıştırmada en fazla 2 dakika ses. Çok dilli model 20 dili ve zaman damgası tabanlı zamanlama kontrolünü destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | Ses(leri), duyguyu, tempoyu, ortam sesini, arka plan müziğini ve ses efektlerini tanımlayın; söylenecek replikleri ekleyin (diyalog için karakterleri satır içinde adlandırın). "audio reference" modunda, bağlı kliplere sırayla @Audio1, @Audio2, @Audio3 olarak başvurun. Çok dilli modelde, tırnak içindeki bir replik, ne zaman ve ne kadar süreyle söyleneceğini kontrol eden bir zaman damgası aralığıyla başlayabilir; örn. `[5.5s:8.0s] Wait for me!`. İstemi, söylenecek repliklerle aynı dilde yazın. En az 1 karakter, en fazla 3000 karakter. | STRING | Evet | 1 - 3000 karakter |
| `reference_mode` | Sesin nasıl koşullandırılacağı: "text only" (her şeyi istemde tanımlayın), "audio reference" (en fazla 3 sesi klonlayın, @Audio1-3 olarak etiketlenir), "image reference" (bir karakter görselinden ses türetin) veya "preset voice" (istemdeki metni okuyan yerleşik adlandırılmış bir ses seçin). | COMBO | Evet | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Ses klonlama için referans klibi, istemde @Audio1 olarak etiketlenir. En fazla 30 sn. Yalnızca `reference_mode` "audio reference" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_2` | İstemde @Audio2 olarak etiketlenen referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "audio reference" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_3` | İstemde @Audio3 olarak etiketlenen referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "audio reference" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_image` | Tek bir karakter görseli; model bundan bir ses türetir. Referans sesle birlikte kullanılamaz. Yalnızca `reference_mode` "image reference" olduğunda kullanılabilir. | IMAGE | Hayır | - |
| `preset_voice` | İstemdeki metni okuyan yerleşik bir TTS 2.0 sesi. Referans klibi gerekmez ve bu modda @AudioN etiketleri kullanılmaz. `reference_mode` "preset voice" olduğunda gereklidir. | COMBO | Hayır | Birden çok yerleşik ön ayarlı ses seçeneği (varsayılan olarak ilk seçenek seçilir) |
| `sample_rate` | Çıktı örnekleme hızı (Hz). (varsayılan: "24000") | COMBO | Evet | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Konuşma hızı. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ile 100 |
| `loudness_rate` | Ses yüksekliği. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ile 100 |
| `pitch_rate` | Yarım ton cinsinden perde kaydırma (-12 ile 12). (varsayılan: 0) | INT | Evet | -12 ile 12 |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |
| `model` | Model sürümü. `seed-audio-1.0-multilingual` 20 dili ve `[5.5s:8.0s]` zaman damgaları aracılığıyla cümle başına zamanlama kontrolünü destekler. `seed-audio-1.0` yalnızca İngilizce ve Çinceyi destekler; zamanlama kontrolü yoktur. (varsayılan: "seed-audio-1.0-multilingual") | COMBO | Hayır | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Parametre Kısıtlamaları

- **Referans modu bağımlılıkları**: `reference_mode` parametresi hangi diğer girdilerin gerekli olduğunu belirler:
  - **"text only"**: Ek girdi gerekmez. İstem @AudioN etiketleri içermemelidir.
  - **"audio reference"**: `reference_audio_1`, `reference_audio_2` veya `reference_audio_3` girdilerinden en az birinin bağlanması gerekir. Referans klipleri boşluksuz sırayla bağlanmalıdır. Her klip en fazla 30 saniye ile sınırlıdır. İstemde @AudioN etiketleri kullanılırsa, en yüksek etiket numarası bağlı referans klip sayısını aşmamalıdır.
  - **"image reference"**: `reference_image` bağlanmalıdır. @AudioN etiketleri kullanılmaz; istem yalnızca sentezlenecek metni içermelidir.
  - **"preset voice"**: Bir ön ayarlı sesin seçilmesi gerekir. İstem tamamen seçilen sesle okunur; @AudioN etiketleri referans olarak kullanılmaz ve @Audio2 veya üzeri etiketler reddedilir.

- **Ses referansı sıralaması**: "audio reference" modunda, referans ses girdileri `reference_audio_1` ile başlayarak boşluksuz sırayla bağlanmalıdır. Örneğin, `reference_audio_1` ve `reference_audio_2` bağlayabilirsiniz, ancak `reference_audio_2` olmadan `reference_audio_1` ve `reference_audio_3` bağlayamazsınız.

- **Maksimum ses etiketi**: "audio reference" modunda en fazla 3 referans klibi bağlanabilir (@Audio1, @Audio2, @Audio3) ve istemdeki en yüksek @AudioN etiketi, bağlı referans ses girdisi sayısını aşamaz.

- **Model farklılıkları**: `seed-audio-1.0-multilingual` modeli 20 dili (İngilizce, Çince, Japonca, Korece, Meksika ve Kastilya İspanyolcası, Endonezce, Almanca, Brezilya Portekizcesi, Fransızca, Tayca, Vietnamca, Malayca, Filipince, İtalyanca, Rusça, Felemenkçe, Lehçe, Türkçe, İsveççe) ve `[5.5s:8.0s]` biçimindeki zaman damgalarını kullanarak cümle başına zamanlama kontrolünü destekler. `seed-audio-1.0` modeli yalnızca İngilizce ve Çinceyi destekler; zamanlama kontrolü yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | ByteDance Seed Audio 1.0 tarafından üretilen ve istemde açıklanan konuşma, müzik, ses efektleri veya çok konuşmacılı diyaloğu içeren ses çıktısı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/tr.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`
