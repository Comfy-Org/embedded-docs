# LTXVGörüntüdenVideoya

LTXVImgToVideo düğümü, bir girdi görüntüsünden video oluşturmak için bir latent temsili hazırlar. Görüntü istenen genişlik ve yüksekliğe yeniden boyutlandırılır, VAE ile kodlanır ve ilk latent karelere yerleştirilir. `strength` kullanılarak orijinal görüntü içeriğinin ne kadarının korunduğunu veya değiştirildiğini kontrol eden bir gürültü maskesi oluşturulur ve pozitif ve negatif koşullandırma değiştirilmeden iletilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Pozitif koşullandırma verisi girdi olarak sağlanır ve değiştirilmeden döndürülür. | CONDITIONING | Evet | - |
| `negative` | Negatif koşullandırma verisi girdi olarak sağlanır ve değiştirilmeden döndürülür. | CONDITIONING | Evet | - |
| `vae` | Girdi görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `image` | Video latentinin başlangıcını oluşturmak için yeniden boyutlandırılan ve kodlanan girdi görüntüsü. | IMAGE | Evet | - |
| `width` | Piksel cinsinden çıktı video genişliği (varsayılan: 768, adım: 32). | INT | Evet | 64 to MAX_RESOLUTION |
| `height` | Piksel cinsinden çıktı video yüksekliği (varsayılan: 512, adım: 32). | INT | Evet | 64 to MAX_RESOLUTION |
| `length` | Oluşturulan videodaki kare sayısı (varsayılan: 97, adım: 8). | INT | Evet | 9 to MAX_RESOLUTION |
| `batch_size` | Tek bir latent yığında oluşturulacak video sayısı (varsayılan: 1). | INT | Evet | 1 to 4096 |
| `strength` | Kodlanmış görüntü içeriğinin ilk latent karelerde ne kadarının korunduğunu kontrol eder. 1.0 değeri orijinal görüntüyü tamamen korurken, 0.0 değeri maksimum değişikliğe izin verir (varsayılan: 1.0). | FLOAT | Evet | 0.0 to 1.0 |

Not: `MAX_RESOLUTION`, ComfyUI kurulumunun izin verdiği maksimum çözünürlüktür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Değiştirilmeden iletilen pozitif koşullandırma. | CONDITIONING |
| `negative` | Değiştirilmeden iletilen negatif koşullandırma. | CONDITIONING |
| `latent` | Dizinin başında kodlanmış girdi görüntüsünü ve `strength` değerine dayalı bir gürültü maskesini içeren video latenti. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
