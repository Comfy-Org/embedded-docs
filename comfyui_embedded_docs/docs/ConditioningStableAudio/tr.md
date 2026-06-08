## Genel Bakış

ConditioningStableAudio düğümü, ses üretimi için hem pozitif hem de negatif koşullandırma girdilerine zamanlama bilgisi ekler. Ses içeriğinin ne zaman ve ne kadar süreyle oluşturulacağını kontrol etmeye yardımcı olan başlangıç zamanı ve toplam süre parametrelerini ayarlar. Bu düğüm, mevcut koşullandırma verilerine sesle ilgili zamanlama meta verileri ekleyerek değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Ses zamanlama bilgisiyle değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Ses zamanlama bilgisiyle değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `saniye_başlangıç` | Ses üretimi için saniye cinsinden başlangıç zamanı (varsayılan: 0,0) | FLOAT | Evet | 0,0 - 1000,0 |
| `saniye_toplam` | Ses üretimi için saniye cinsinden toplam süre (varsayılan: 47,0) | FLOAT | Evet | 0,0 - 1000,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Ses zamanlama bilgisi uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Ses zamanlama bilgisi uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
