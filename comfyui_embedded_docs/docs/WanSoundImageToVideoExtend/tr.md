> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/tr.md)

WanSoundImageToVideoExtend düğümü, mevcut bir video latentini, isteğe bağlı olarak ses, referans görüntü ve kontrol videosu rehberliğinde ek kareler oluşturarak genişletir. Bir başlangıç video latentini alır ve sağlanan koşullandırma ile ses ipuçlarını kullanarak yeni içeriği etkileyerek daha uzun bir video dizisi üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Videonun ne içermesi gerektiğini yönlendiren pozitif koşullandırma promptları |
| `negative` | CONDITIONING | Evet | - | Videonun nelerden kaçınması gerektiğini belirten negatif koşullandırma promptları |
| `vae` | VAE | Evet | - | Video karelerini kodlamak ve çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı |
| `length` | INT | Evet | 1 ile MAKSİMUM ÇÖZÜNÜRLÜK | Video dizisi için oluşturulacak toplam kare sayısı (varsayılan: 77, adım: 4) |
| `video_latent` | LATENT | Evet | - | Genişletme için başlangıç noktası görevi gören ilk video latent temsili |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Hayır | - | Ses özelliklerine dayalı olarak video oluşturmayı etkileyebilen isteğe bağlı ses gömme vektörleri |
| `ref_image` | IMAGE | Hayır | - | Video oluşturma için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü |
| `control_video` | IMAGE | Hayır | - | Oluşturulan videonun hareketini ve stilini yönlendirebilen isteğe bağlı kontrol videosu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `negative` | CONDITIONING | Video bağlamı uygulanmış işlenmiş pozitif koşullandırma |
| `latent` | CONDITIONING | Video bağlamı uygulanmış işlenmiş negatif koşullandırma |
| `latent` | LATENT | Genişletilmiş video dizisini içeren oluşturulmuş video latent temsili |

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
