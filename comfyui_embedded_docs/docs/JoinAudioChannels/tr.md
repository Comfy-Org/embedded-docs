> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/tr.md)

# JoinAudioChannels Düğümü

JoinAudioChannels düğümü, iki ayrı mono ses girişini tek bir stereo ses çıkışında birleştirir. Bir sol kanal ve bir sağ kanal alır, örnekleme hızları ve uzunluklarının uyumlu olmasını sağlar ve bunları iki kanallı bir ses dalga formunda birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `ses_sol` | AUDIO | Evet | | Ortaya çıkan stereo seste sol kanal olarak kullanılacak mono ses verisi. |
| `ses_sağ` | AUDIO | Evet | | Ortaya çıkan stereo seste sağ kanal olarak kullanılacak mono ses verisi. |

**Not:** Her iki giriş ses akışı da mono (tek kanallı) olmalıdır. Farklı örnekleme hızlarına sahiplerse, düşük hızlı kanal otomatik olarak yüksek hıza uyacak şekilde yeniden örneklenir. Ses akışlarının uzunlukları farklıysa, kısa olanın uzunluğuna göre kırpılırlar.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `audio` | AUDIO | Birleştirilmiş sol ve sağ kanalları içeren ortaya çıkan stereo ses. |

---
**Source fingerprint (SHA-256):** `6dced8c2288fb8f214e04b621ed3ab934231983d7987ff08aa43da6814331be0`
