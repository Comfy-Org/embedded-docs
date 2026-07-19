# ByteDanceSeedAudio

ByteDance Seed Audio 1.0 ile tek bir istemden konuşma, müzik, ses efektleri ve çok konuşmacılı diyalog oluşturun. İstemde ses(ler)i, duyguyu, ortamı, arka plan müziğini ve ses efektlerini tanımlayın ve söylenecek satırları ekleyin. İsteğe bağlı olarak yerleşik bir ön ayarlı ses seçin, en fazla 3 referans klibinden (istemde @Audio1-3 olarak etiketlenmiş) ses klonlayın veya bir karakter görüntüsünden ses türetin. Çalıştırma başına en fazla 2 dakika ses.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `text_prompt` | Ses(ler)i, duyguyu, tempoyu, ortamı, arka plan müziğini ve ses efektlerini tanımlayın ve söylenecek satırları ekleyin (diyalog için karakterleri satır içinde adlandırın). 'Ses referansı' modunda, bağlı kliplere sırayla @Audio1, @Audio2, @Audio3 olarak başvurun. Maksimum 3000 karakter. | STRING | Evet | 1 ila 3000 karakter |
| `reference_mode` | Sesin nasıl koşullandırılacağı: 'yalnızca metin' (her şeyi istemde tanımlayın), 'ses referansı' (en fazla 3 sesi klonlayın, @Audio1-3 olarak etiketlenmiş), 'görüntü referansı' (bir karakter görüntüsünden ses türetin) veya 'ön ayarlı ses' (istemde okuyan yerleşik adlandırılmış bir ses seçin). | COMBO | Evet | `"yalnızca metin"`<br>`"ses referansı"`<br>`"görüntü referansı"`<br>`"ön ayarlı ses"` |
| `reference_audio_1` | Ses klonlama için referans klibi, istemde @Audio1 olarak etiketlenmiştir. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_2` | İstemde @Audio2 olarak etiketlenmiş referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_3` | İstemde @Audio3 olarak etiketlenmiş referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_image` | Tek bir karakter görüntüsü; model bundan bir ses türetir. Referans ses ile birleştirilemez. Yalnızca `reference_mode` "görüntü referansı" olduğunda kullanılabilir. | IMAGE | Hayır | - |
| `preset_voice` | İstemde okuyan yerleşik bir TTS 2.0 sesi. Referans klibi gerekmez ve bu modda @AudioN etiketleri kullanılmaz. Yalnızca `reference_mode` "ön ayarlı ses" olduğunda kullanılabilir. | COMBO | Hayır | Birden çok seçenek mevcuttur (açıklamaya bakın) |
| `sample_rate` | Çıkış örnekleme hızı (Hz cinsinden). (varsayılan: "24000") | COMBO | Evet | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Konuşma hızı. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ila 100 |
| `loudness_rate` | Ses yüksekliği. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ila 100 |
| `pitch_rate` | Perde kaydırması (yarım ton cinsinden, -12 ila 12). (varsayılan: 0) | INT | Evet | -12 ila 12 |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 2147483647 |

### Parametre Kısıtlamaları

- **Referans modu bağımlılıkları**: `reference_mode` parametresi, diğer hangi girişlerin gerekli olduğunu belirler:
  - **"yalnızca metin"**: Ek giriş gerekmez. İstem @AudioN etiketleri içermemelidir.
  - **"ses referansı"**: `reference_audio_1`, `reference_audio_2` veya `reference_audio_3`'ten en az birinin bağlı olmasını gerektirir. Referans klipleri boşluksuz sırayla bağlanmalıdır (ör. _1, ardından _2, ardından _3). Her klip maksimum 30 saniye süreyle sınırlıdır. İstem, bağlı kliplere @Audio1, @Audio2, @Audio3 etiketlerini kullanarak başvurmalıdır.
  - **"görüntü referansı"**: `reference_image`'in bağlı olmasını gerektirir. İstem @AudioN etiketleri içermemelidir.
  - **"ön ayarlı ses"**: `preset_voice`'un seçilmesini gerektirir. İstem @AudioN etiketleri içermemelidir (istemin tamamı seçilen seste okunur).

- **Ses referansı sıralaması**: "Ses referansı" modu kullanılırken, referans ses girişleri `reference_audio_1`'den başlayarak boşluksuz sırayla bağlanmalıdır. Örneğin, _1 ve _2'yi bağlayabilirsiniz, ancak _2 olmadan _1 ve _3'ü bağlayamazsınız.

- **Maksimum ses etiketi**: "Ses referansı" modundayken istem en fazla 3 ses klibine (@Audio1, @Audio2, @Audio3) başvurabilir. En yüksek numaralı etiket, bağlı referans ses girişlerinin sayısını aşmamalıdır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `AUDIO` | ByteDance Seed Audio 1.0'dan oluşturulan, istemde açıklandığı gibi konuşma, müzik, ses efektleri veya çok konuşmacılı diyalog içeren ses çıkışı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/tr.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
