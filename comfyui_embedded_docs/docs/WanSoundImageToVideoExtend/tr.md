WanSoundImageToVideoExtend düğümü, mevcut bir video latentini, isteğe bağlı olarak ses, referans görüntü ve kontrol videosu rehberliğinde ek kareler oluşturarak genişletir. Bir başlangıç video latentini alır ve sağlanan koşullandırma ile ses ipuçlarını kullanarak yeni içeriği etkileyerek daha uzun bir video dizisi üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Videonun ne içermesi gerektiğini yönlendiren pozitif koşullandırma promptları | CONDITIONING | Evet | - |
| `negative` | Videonun nelerden kaçınması gerektiğini belirten negatif koşullandırma promptları | CONDITIONING | Evet | - |
| `vae` | Video karelerini kodlamak ve çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı | VAE | Evet | - |
| `length` | Video dizisi için oluşturulacak toplam kare sayısı (varsayılan: 77, adım: 4) | INT | Evet | 1 ile MAKSİMUM ÇÖZÜNÜRLÜK |
| `video_latent` | Genişletme için başlangıç noktası görevi gören ilk video latent temsili | LATENT | Evet | - |
| `audio_encoder_output` | Ses özelliklerine dayalı olarak video oluşturmayı etkileyebilen isteğe bağlı ses gömme vektörleri | AUDIOENCODEROUTPUT | Hayır | - |
| `ref_image` | Video oluşturma için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Oluşturulan videonun hareketini ve stilini yönlendirebilen isteğe bağlı kontrol videosu | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video bağlamı uygulanmış işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Video bağlamı uygulanmış işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Genişletilmiş video dizisini içeren oluşturulmuş video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/tr.md)

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
