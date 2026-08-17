# WanSoundImageToVideoExtend

WanSoundImageToVideoExtend düğümü, mevcut bir video latentini genişleterek ek kareler üretir; isteğe bağlı olarak ses, referans görüntü ve kontrol videosu tarafından yönlendirilir. Başlangıç video latentini alır ve sağlanan koşullandırma ile ses ipuçlarını kullanarak daha uzun bir video dizisi üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Videonun ne içermesi gerektiğini yönlendiren pozitif koşullandırma ipuçları | CONDITIONING | Evet | - |
| `negative` | Videonun nelerden kaçınması gerektiğini belirten negatif koşullandırma ipuçları | CONDITIONING | Evet | - |
| `vae` | Video karelerini kodlamak ve kodunu çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı | VAE | Evet | - |
| `length` | Video dizisi için üretilecek toplam kare sayısı (varsayılan: 77, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `video_latent` | Genişletme için başlangıç noktası görevi gören ilk video latent gösterimi. Genişlik, yükseklik, parti boyutu ve kare ofseti bu latentten türetilir. Bu latentin son 19 karesi ayrıca yeni dizi için referans hareketi olarak kullanılır. | LATENT | Evet | - |
| `audio_encoder_output` | Ses özelliklerine dayalı olarak video üretimini etkileyebilen isteğe bağlı ses yerleştirmeleri. Sağlandığında, ses enterpole edilir ve koşullandırmaya eklenen bir ses yerleştirme demeti oluşturmak için kullanılır. | AUDIO_ENCODER_OUTPUT | Hayır | - |
| `ref_image` | Video üretimi için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü. Görüntü, hedef boyutlara uyacak şekilde büyütülür ve latente kodlanır; ardından hem pozitif hem de negatif koşullandırmaya eklenir. Partideki yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |
| `control_video` | Üretilen videonun hareketini ve stilini yönlendirebilen isteğe bağlı kontrol videosu. Video büyütülür, kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. Kontrol videosu belirtilen `length` değerine kırpılır. | IMAGE | Hayır | - |

Not: `audio_encoder_output` sağlandığında, ses yerleştirmeleri pozitif koşullandırmaya eklenir; negatif koşullandırma ise aynı yerleştirmelerin sıfırlanmış halini alır. `video_latent`'ten türetilen kare ofseti, yeni karelerin ses dizisinde nerede başlayacağını belirler. Ses dizisi, istenen uzatmayı kapsayacak yeterli kare içermiyorsa, ses koşullandırması uygulanmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Ses yerleştirmeleri, referans latentleri, referans hareketi ve sağlanmışsa kontrol videosu dahil olmak üzere video bağlamı uygulanmış işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Ses yerleştirmeleri (sıfırlanmış), referans latentleri, referans hareketi ve sağlanmışsa kontrol videosu dahil olmak üzere video bağlamı uygulanmış işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Girdi `video_latent` ve hedef `length` değerinden türetilen boyutlarla sıfır olarak başlatılan, genişletilmiş video dizisini içeren üretilmiş video latent gösterimi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/tr.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
