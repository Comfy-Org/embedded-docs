> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/tr.md)

WanDancerVideo düğümü, WanDancer modeli ile video oluşturma için koşullandırma verilerini ve boş bir latent tensörü hazırlar. Başlangıç görüntüsü, maske, CLIP vision gömme vektörleri ve ses özellikleri gibi isteğe bağlı girdilerle pozitif ve negatif koşullandırmayı birleştirerek oluşturulan videoyu kontrol eder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | | Video oluşturmayı yönlendiren pozitif koşullandırma. |
| `negative` | CONDITIONING | Evet | | Video oluşturmayı yönlendiren negatif koşullandırma. |
| `vae` | VAE | Evet | | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE. |
| `width` | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 480). |
| `height` | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 832). |
| `length` | INT | Evet | 1 - MAX_RESOLUTION (adım: 4) | Oluşturulan videodaki kare sayısı. WanDancer için 149 olarak kalmalıdır (varsayılan: 149). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | | İlk kare için CLIP vision gömme vektörleri. |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | Hayır | | Referans görüntüsü için CLIP vision gömme vektörleri. |
| `start_image` | IMAGE | Hayır | | Kodlanacak başlangıç görüntüsü(leri). Belirtilen `length` değerine kadar herhangi bir sayıda kare olabilir. |
| `mask` | MASK | Hayır | | Başlangıç görüntüsü(leri) için görüntü koşullandırma maskesi. Beyaz alanlar korunur, siyah alanlar oluşturulur. Yerel oluşturmalar için kullanılır. |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | Hayır | | Ses kodlayıcıdan gelen çıktı; ses koşullu oluşturma için ses özellikleri, fps ve enjeksiyon ölçeği sağlar. |

**Parametre Kısıtlamalarına İlişkin Not:**
- `start_image` ve `mask` girdileri isteğe bağlıdır ancak birlikte kullanılabilir. `start_image` sağlandığında kodlanır ve latent ile birleştirilir. Ayrıca `mask` sağlanırsa, başlangıç görüntüsünün hangi bölümlerinin korunacağını (beyaz) ve hangilerinin yeniden oluşturulacağını (siyah) kontrol eder. `mask` sağlanmazsa, başlangıç görüntüsü alanının tamamı koşullandırma kılavuzu olarak kullanılır.
- `clip_vision_output` ve `clip_vision_output_ref` girdileri isteğe bağlıdır ve ilk kare ile bir referans görüntüsü için görsel bağlam sağlamak amacıyla birlikte kullanılabilir.
- `audio_encoder_output` girdisi isteğe bağlıdır ve ses koşullu oluşturma için ses özellikleri sağlar.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Ek veriler (birleştirilmiş latent, CLIP vision, ses) eklenmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Ek veriler (birleştirilmiş latent, CLIP vision, ses) eklenmiş negatif koşullandırma. |
| `latent` | LATENT | Boyutları belirtilen video uzunluğu, yüksekliği ve genişliğiyle eşleşen boş bir latent tensörü. |