> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/tr.md)

## Genel Bakış

ConditioningStableAudio düğümü, ses üretimi için hem pozitif hem de negatif koşullandırma girdilerine zamanlama bilgisi ekler. Ses içeriğinin ne zaman ve ne kadar süreyle oluşturulacağını kontrol etmeye yardımcı olan başlangıç zamanı ve toplam süre parametrelerini ayarlar. Bu düğüm, mevcut koşullandırma verilerine sesle ilgili zamanlama meta verileri ekleyerek değiştirir.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `positive` | CONDITIONING | Evet | - | Ses zamanlama bilgisiyle değiştirilecek pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Ses zamanlama bilgisiyle değiştirilecek negatif koşullandırma girdisi |
| `seconds_start` | FLOAT | Evet | 0,0 - 1000,0 | Ses üretimi için saniye cinsinden başlangıç zamanı (varsayılan: 0,0) |
| `seconds_total` | FLOAT | Evet | 0,0 - 1000,0 | Ses üretimi için saniye cinsinden toplam süre (varsayılan: 47,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Ses zamanlama bilgisi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Ses zamanlama bilgisi uygulanmış değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
