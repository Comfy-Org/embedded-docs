> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/tr.md)

WanHuMoImageToVideo düğümü, görüntüleri video dizilerine dönüştürerek video kareleri için gizli temsiller oluşturur. Koşullandırma girdilerini işler ve video oluşturmayı etkilemek için referans görüntüler ve ses gömüleri içerebilir. Düğüm, video sentezi için uygun olan değiştirilmiş koşullandırma verilerini ve gizli temsilleri çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Video oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Referans görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı video karelerinin piksel cinsinden genişliği (varsayılan: 832, 16'ya bölünebilir olmalı) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı video karelerinin piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalı) |
| `length` | INT | Evet | 1 - MAX_RESOLUTION | Oluşturulan video dizisindeki kare sayısı (varsayılan: 97) |
| `batch_size` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video dizisi sayısı (varsayılan: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Hayır | - | Video oluşturmayı ses içeriğine dayalı olarak etkileyebilen isteğe bağlı ses kodlama verisi |
| `ref_image` | IMAGE | Hayır | - | Video oluşturma stilini ve içeriğini yönlendirmek için kullanılan isteğe bağlı referans görüntü |

**Not:** Bir referans görüntü sağlandığında, bu görüntü kodlanır ve hem pozitif hem de negatif koşullandırmaya eklenir. Ses kodlayıcı çıktısı sağlandığında, bu çıktı işlenir ve koşullandırma verisine dahil edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Referans görüntü ve/veya ses gömüleri dahil edilmiş değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Referans görüntü ve/veya ses gömüleri dahil edilmiş değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video dizi verilerini içeren oluşturulmuş gizli temsil |