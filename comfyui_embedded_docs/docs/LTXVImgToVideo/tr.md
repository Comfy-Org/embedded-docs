# LTXVGörüntüdenVideoya

LTXVImgToVideo, girdi olarak aldığı bir görüntüyü video üretim modelleri için video latent gösterimine dönüştürür. Görüntüyü istenen genişlik ve yüksekliğe yeniden boyutlandırır, VAE ile kodlar ve kodlanmış kareleri sıfırlardan oluşan video boyutundaki bir latentin başına yerleştirir. Strength kontrolü, video üretimi sırasında orijinal görüntü içeriğinin ne kadarının korunacağını ve ne kadarının değiştirileceğini belirler.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimini yönlendiren pozitif koşullandırma promptları | CONDITIONING | Evet | - |
| `negatif` | Videoda belirli öğelerden kaçınmak için kullanılan negatif koşullandırma promptları | CONDITIONING | Evet | - |
| `vae` | Girdi görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `görüntü` | Video karelerine dönüştürülecek girdi görüntüsü | IMAGE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768, adım: 32) | INT | Hayır | 64 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512, adım: 32) | INT | Hayır | 64 to MAX_RESOLUTION |
| `uzunluk` | Üretilen videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Hayır | 9 to MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 |
| `güç` | Üretilen videonun ilk karelerinde orijinal görüntü içeriğinin ne kadarının korunacağını kontrol eder. 1.0 değeri orijinal görüntüyü tamamen korurken, 0.0 değeri maksimum değişikliğe izin verir (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 |

Not: `width` ve `height` değerleri 32 piksel adımlarla, `length` değeri ise 8 kare adımlarla değişir; bu, video latent sıkıştırmasıyla uyumludur (uzamsal boyutlarda 32 kat, zamansal boyutta 8 kat). Video latenti, ((length - 1) // 8) + 1 kare içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `pozitif` | Üretilen latent ile kullanılmak üzere değiştirilmeden iletilen pozitif koşullandırma | CONDITIONING |
| `negatif` | Üretilen latent ile kullanılmak üzere değiştirilmeden iletilen negatif koşullandırma | CONDITIONING |
| `gizli` | Kodlanmış görüntü karelerini ve video üretimi sırasında koşullandırmanın ne kadar güçlü uygulanacağını kontrol eden bir gürültü maskesini içeren video latent gösterimi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
