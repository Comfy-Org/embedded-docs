# KoşullandırmaKararlıSes

ConditioningStableAudio düğümü, ses üretimi için hem pozitif hem de negatif conditioning girdilerine zamanlama bilgisi ekler. Ses içeriğinin ne zaman ve ne kadar süreyle üretileceğini kontrol etmeye yardımcı olan başlangıç zamanı ve toplam süre parametrelerini ayarlar. Bu düğüm, mevcut conditioning verilerine sese özgü zamanlama meta verileri ekleyerek bunları değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Ses zamanlama bilgisiyle değiştirilecek pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negative` | Ses zamanlama bilgisiyle değiştirilecek negatif conditioning girdisi | CONDITIONING | Evet | - |
| `seconds_start` | Ses üretimi için saniye cinsinden başlangıç zamanı (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 1000.0 |
| `seconds_total` | Ses üretimi için saniye cinsinden toplam süre (varsayılan: 47.0) | FLOAT | Evet | 0.0 to 1000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Ses zamanlama bilgisi uygulanmış değiştirilmiş pozitif conditioning | CONDITIONING |
| `negative` | Ses zamanlama bilgisi uygulanmış değiştirilmiş negatif conditioning | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/tr.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
