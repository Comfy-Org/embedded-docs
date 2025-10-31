> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

LTXVImgToVideo düğümü, bir giriş görüntüsünü video üretim modelleri için video latents (gizil) temsiline dönüştürür. Tek bir görüntüyü alır ve VAE kodlayıcı kullanarak bir kare dizisine genişletir, ardından video üretimi sırasında orijinal görüntü içeriğinin ne kadarının korunacağını ve ne kadarının değiştirileceğini belirlemek için güç kontrolü ile koşullandırma uygular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için olumlu koşullandırma ipuçları |
| `negative` | CONDITIONING | Evet | - | Videoda belirli öğelerin bulunmaması için olumsuz koşullandırma ipuçları |
| `vae` | VAE | Evet | - | Giriş görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli |
| `image` | IMAGE | Evet | - | Video karelerine dönüştürülecek giriş görüntüsü |
| `width` | INT | Hayır | 64 - MAX_RESOLUTION | Çıkış videosunun piksel cinsinden genişliği (varsayılan: 768, adım: 32) |
| `height` | INT | Hayır | 64 - MAX_RESOLUTION | Çıkış videosunun piksel cinsinden yüksekliği (varsayılan: 512, adım: 32) |
| `length` | INT | Hayır | 9 - MAX_RESOLUTION | Oluşturulan videodaki kare sayısı (varsayılan: 97, adım: 8) |
| `batch_size` | INT | Hayır | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `strength` | FLOAT | Hayır | 0.0 - 1.0 | Video üretimi sırasında orijinal görüntünün ne kadar değiştirileceğini kontrol eder; 1.0 orijinal içeriğin çoğunu korur, 0.0 ise maksimum değişikliğe izin verir (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş olumlu koşullandırma |
| `negative` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş olumsuz koşullandırma |
| `latent` | LATENT | Video üretimi için kodlanmış kareleri ve gürültü maskesini içeren video latent temsili |