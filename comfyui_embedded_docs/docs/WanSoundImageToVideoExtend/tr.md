# WanSoundImageToVideoExtend

WanSoundImageToVideoExtend düğümü, isteğe bağlı olarak ses, referans görüntü ve kontrol videosu tarafından yönlendirilen ek kareler oluşturarak mevcut bir video latentini genişletir. Bir başlangıç video latenti alır ve sağlanan koşullandırma ile ses ipuçlarını kullanarak yeni içeriği etkileyen daha uzun bir video dizisi üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Videonun neleri içermesi gerektiğini yönlendiren pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negative` | Videonun nelerden kaçınması gerektiğini belirten negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Referans görüntüyü ve kontrol videosunu latent uzaya kodlamak için kullanılan Varyasyonel Otomatik Kodlayıcı | VAE | Evet | - |
| `length` | Video dizisi için oluşturulacak toplam kare sayısı (varsayılan: 77, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `video_latent` | Genişletme için başlangıç noktası olarak hizmet eden başlangıç video latenti. Çıktı genişliği, yüksekliği, parti boyutu ve kare ofseti bu latentten türetilir. Son 19 karesi referans hareket koşullandırması olarak kullanılır. | LATENT | Evet | - |
| `audio_encoder_output` | Ses özelliklerine göre video oluşturmayı etkileyebilen isteğe bağlı ses gömme vektörleri. Sağlandığında, ses enterpole edilir ve koşullandırmaya eklenen bir ses gömme grubuna dönüştürülür. | AUDIOENCODEROUTPUT | Hayır | - |
| `ref_image` | Video oluşturma için görsel rehberlik sağlayan isteğe bağlı referans görüntü. Görüntü, hedef boyutlara uyacak şekilde büyütülür ve bir latent olarak kodlanır, ardından hem pozitif hem de negatif koşullandırmaya eklenir. Partideki yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |
| `control_video` | Oluşturulan videonun hareketini ve yapısını yönlendiren isteğe bağlı kontrol videosu. Video büyütülür, kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. Kontrol videosu, belirtilen `length` değerine göre kısaltılır. | IMAGE | Hayır | - |

Not: Çıktı latenti, hedef boyutlarla sıfırlar olarak başlatılır. Girdi `video_latent` bu çıktıya kopyalanmaz; bunun yerine son 19 karesi referans hareket olarak kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video bağlamı uygulanmış işlenmiş pozitif koşullandırma; ses gömme vektörlerini, referans latentlerini, referans hareketini ve sağlanmışsa kontrol videosunu içerir | CONDITIONING |
| `negative` | Video bağlamı uygulanmış işlenmiş negatif koşullandırma; ses gömme vektörlerini (sıfırlanmış), referans latentlerini, referans hareketini ve sağlanmışsa kontrol videosunu içerir | CONDITIONING |
| `latent` | Genişletilmiş dizinin video latent temsili; girdi `video_latent` ve hedef `length` değerinden türetilen boyutlarla sıfırlar olarak başlatılır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/tr.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
