# ByteDanceSeedAudio

ByteDance Seed Audio 1.0 ile tek bir istemden konuşma, müzik, ses efektleri ve çok konuşmacılı diyalog oluşturun. İstemde ses(ler)i, duyguyu, ortamı, arka plan müziğini ve ses efektlerini tanımlayın ve söylenecek satırları ekleyin. İsteğe bağlı olarak yerleşik bir ön ayarlı ses seçin, en fazla 3 referans klibinden (istemde @Audio1-3 olarak etiketlenmiş) ses klonlayın veya bir karakter görüntüsünden ses türetin. Çalıştırma başına en fazla 2 dakika ses.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `text_prompt` | Ses(ler)i, duyguyu, tempoyu, ortamı, arka plan müziğini ve ses efektlerini tanımlayın ve söylenecek satırları ekleyin (diyalog için karakterleri satır içinde adlandırın). 'Ses referansı' modunda, bağlı kliplere sırayla @Audio1, @Audio2, @Audio3 olarak başvurun. Çok dilli modelde, tırnak içindeki bir satır, ne zaman ve ne kadar süre konuşulacağını kontrol eden bir zaman damgası aralığıyla başlayabilir, ör. `[5.5s:8.0s] Beni bekle!`. İstemi, konuşulacak satırlarla aynı dilde yazın. En az 1 karakter, Maksimum 3000 karakter. | STRING | Evet | 1 ila 3000 karakter |
  - **"ses referansı"**: `reference_audio_1`, `reference_audio_2` veya `reference_audio_3`'ten en az birinin bağlı olmasını gerektirir. Referans klipler boşluksuz sırayla bağlanmalıdır. Her klip en fazla 30 saniye ile sınırlıdır. İstemde @AudioN etiketleri kullanılırsa, en yüksek etiket numarası bağlı referans klip sayısını aşmamalıdır.
| `reference_audio_1` | Ses klonlama için referans klibi, istemde @Audio1 olarak etiketlenmiştir. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_2` | İstemde @Audio2 olarak etiketlenmiş referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
| `reference_audio_3` | İstemde @Audio3 olarak etiketlenmiş referans klibi. En fazla 30 sn. Yalnızca `reference_mode` "ses referansı" olduğunda kullanılabilir. | AUDIO | Hayır | En fazla 30 saniye |
  - **"görüntü referansı"**: `reference_image`'in bağlı olmasını gerektirir. @AudioN etiketleri kullanılmaz; istem yalnızca sentezlenecek metni içermelidir.
  - **"ön ayarlı ses"**: Önceden ayarlanmış bir sesin seçilmesini gerektirir. İstemin tamamı seçilen seste okunur; @AudioN etiketleri referans olarak kullanılmaz ve @Audio2 veya üzeri etiketler reddedilir.
| `sample_rate` | Çıkış örnekleme hızı (Hz cinsinden). (varsayılan: "24000") | COMBO | Evet | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Konuşma hızı. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ila 100 |
| `loudness_rate` | Ses yüksekliği. 0 = normal, 100 = 2.0x, -50 = 0.5x. (varsayılan: 0) | INT | Evet | -50 ila 100 |
| `pitch_rate` | Perde kaydırması (yarım ton cinsinden, -12 ila 12). (varsayılan: 0) | INT | Evet | -12 ila 12 |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 2147483647 |
| `model` | Model sürümü. `seed-audio-1.0-multilingual`, 20 dil ve `[5.5s:8.0s]` zaman damgalarıyla cümle başına zamanlama kontrolünü destekler. `seed-audio-1.0` yalnızca İngilizce ve Çinceyi destekler, zamanlama kontrolü yoktur. (varsayılan: "seed-audio-1.0-multilingual") | COMBO | Hayır | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Parametre Kısıtlamaları

- **Referans modu bağımlılıkları**: `reference_mode` parametresi, diğer hangi girişlerin gerekli olduğunu belirler:
  - **"yalnızca metin"**: Ek giriş gerekmez. İstem @AudioN etiketleri içermemelidir.
  - **"ses referansı"**: `reference_audio_1`, `reference_audio_2` veya `reference_audio_3`'ten en az birinin bağlı olmasını gerektirir. Referans klipleri boşluksuz sırayla bağlanmalıdır (ör. _1, ardından _2, ardından _3). Her klip maksimum 30 saniye süreyle sınırlıdır. İstem, bağlı kliplere @Audio1, @Audio2, @Audio3 etiketlerini kullanarak başvurmalıdır.
  - **"görüntü referansı"**: `reference_image`'in bağlı olmasını gerektirir. İstem @AudioN etiketleri içermemelidir.
  - **"ön ayarlı ses"**: `preset_voice`'un seçilmesini gerektirir. İstem @AudioN etiketleri içermemelidir (istemin tamamı seçilen seste okunur).

- **Ses referansı sıralaması**: "Ses referansı" modu kullanılırken, referans ses girişleri `reference_audio_1`'den başlayarak boşluksuz sırayla bağlanmalıdır. Örneğin, _1 ve _2'yi bağlayabilirsiniz, ancak _2 olmadan _1 ve _3'ü bağlayamazsınız.

- **Maksimum ses etiketi**: "Ses referansı" modundayken istem en fazla 3 ses klibine (@Audio1, @Audio2, @Audio3) başvurabilir ve istemdeki en yüksek @AudioN etiketi bağlı referans ses girişi sayısını aşamaz.

- **Model farkları**: `seed-audio-1.0-multilingual` modeli 20 dili (İngilizce, Çince, Japonca, Korece, Meksika ve Kastilya İspanyolcası, Endonezce, Almanca, Brezilya Portekizcesi, Fransızca, Tayca, Vietnamca, Malayca, Filipince, İtalyanca, Rusça, Felemenkçe, Lehçe, Türkçe, İsveççe) ve `[5.5s:8.0s]` biçimindeki zaman damgalarıyla cümle başına zamanlama kontrolünü destekler. `seed-audio-1.0` modeli yalnızca İngilizce ve Çinceyi destekler, zamanlama kontrolü yoktur.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `AUDIO` | ByteDance Seed Audio 1.0'dan oluşturulan, istemde açıklandığı gibi konuşma, müzik, ses efektleri veya çok konuşmacılı diyalog içeren ses çıkışı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/tr.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
