# JoinAudioChannels Düğümü

JoinAudioChannels düğümü, iki ayrı mono ses girişini tek bir stereo ses çıkışında birleştirir. Bir sol kanal ve bir sağ kanal alır, örnekleme hızları ve uzunluklarının uyumlu olmasını sağlar ve bunları iki kanallı bir ses dalga formunda birleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses_sol` | Ortaya çıkan stereo seste sol kanal olarak kullanılacak mono ses verisi. | AUDIO | Evet |  |
| `ses_sağ` | Ortaya çıkan stereo seste sağ kanal olarak kullanılacak mono ses verisi. | AUDIO | Evet |  |

**Not:** Her iki giriş ses akışı da mono (tek kanallı) olmalıdır. Farklı örnekleme hızlarına sahiplerse, düşük hızlı kanal otomatik olarak yüksek hıza uyacak şekilde yeniden örneklenir. Ses akışlarının uzunlukları farklıysa, kısa olanın uzunluğuna göre kırpılırlar.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Birleştirilmiş sol ve sağ kanalları içeren ortaya çıkan stereo ses. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/tr.md)

---
**Source fingerprint (SHA-256):** `6dced8c2288fb8f214e04b621ed3ab934231983d7987ff08aa43da6814331be0`
