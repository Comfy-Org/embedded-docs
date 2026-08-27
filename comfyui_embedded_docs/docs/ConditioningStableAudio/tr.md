# KoşullandırmaKararlıSes

ConditioningStableAudio düğümü, ses üretimi için hem pozitif hem de negatif koşullandırma girdilerine zamanlama bilgisi ekler. Ses içeriğinin ne zaman ve ne kadar süreyle üretileceğini kontrol etmeye yardımcı olan başlangıç zamanı ve toplam süre parametrelerini ayarlar. Bu düğüm, mevcut koşullandırma verilerine sese özgü zamanlama meta verileri ekleyerek bu verileri değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Ses zamanlama bilgisiyle değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Ses zamanlama bilgisiyle değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `saniye_başlangıç` | Ses üretimi için saniye cinsinden başlangıç zamanı (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1000.0 |
| `saniye_toplam` | Ses üretimi için saniye cinsinden toplam süre (varsayılan: 47.0) | FLOAT | Evet | 0.0 ile 1000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Ses zamanlama bilgisi uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Ses zamanlama bilgisi uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/tr.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
