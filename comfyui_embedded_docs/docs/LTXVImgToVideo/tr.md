# LTXVGörüntüdenVideoya

LTXVImgToVideo, girdi görüntüsünü video oluşturma modelleri için bir video latent temsiline dönüştürür. Görüntüyü istenen genişlik ve yüksekliğe yeniden boyutlandırır, VAE ile kodlar ve kodlanmış kareleri sıfırlardan oluşan video boyutlu bir latentin başına yerleştirir. `strength` denetimi, video oluşturma sırasında orijinal görüntü içeriğinin ne kadarının korunacağını ve ne kadarının değiştirileceğini belirler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Videoda belirli öğelerden kaçınmak için negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Girdi görüntüsünü latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `görüntü` | Video karelerine dönüştürülecek girdi görüntüsü | IMAGE | Evet | - |
| `genişlik` | Piksel cinsinden çıktı video genişliği (varsayılan: 768, adım: 32) | INT | Evet | 64 - MAX_RESOLUTION |
| `yükseklik` | Piksel cinsinden çıktı video yüksekliği (varsayılan: 512, adım: 32) | INT | Evet | 64 - MAX_RESOLUTION |
| `uzunluk` | Oluşturulan videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Evet | 9 - MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `güç` | Oluşturulan videonun ilk karelerinde orijinal görüntü içeriğinin ne kadarının korunacağını kontrol eder. 1.0 değeri orijinal görüntüyü tamamen korur, 0.0 ise maksimum değişikliğe izin verir (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Not: `width` ve `height` 32 piksel adımlarla, `length` ise 8 kare adımlarla değişir; bu, video latent sıkıştırmasıyla uyumludur (uzamsal boyutlarda 32x ve zamansal boyutta 8x). Video latenti ((length - 1) // 8) + 1 kare içerir. Girdi görüntüsü, merkez kırpma ile bilineer ölçekleme kullanılarak `width` x `height` boyutuna yeniden boyutlandırılır ve kodlama için yalnızca ilk üç kanal kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Oluşturulan latent ile kullanılmak üzere değiştirilmeden aktarılan pozitif koşullandırma | CONDITIONING |
| `negative` | Oluşturulan latent ile kullanılmak üzere değiştirilmeden aktarılan negatif koşullandırma | CONDITIONING |
| `latent` | Kodlanmış görüntü karelerini ve video oluşturma sırasında koşullandırmanın ne kadar güçlü uygulanacağını kontrol eden bir gürültü maskesini içeren video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
