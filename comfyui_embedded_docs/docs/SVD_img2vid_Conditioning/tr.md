> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/tr.md)

SVD_img2vid_Conditioning düğümü, Stable Video Diffusion kullanarak video üretimi için koşullandırma verilerini hazırlar. Başlangıç görüntüsünü alır ve CLIP vision ve VAE kodlayıcılarından geçirerek pozitif ve negatif koşullandırma çiftleri ile birlikte video üretimi için boş bir gizli alan oluşturur. Bu düğüm, üretilen videodaki hareket, kare hızı ve artırım seviyelerini kontrol etmek için gerekli parametreleri ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Evet | - | Giriş görüntüsünü kodlamak için CLIP vision modeli |
| `init_image` | IMAGE | Evet | - | Video üretimi için başlangıç noktası olarak kullanılacak başlangıç görüntüsü |
| `vae` | VAE | Evet | - | Görüntüyü gizli uzaya kodlamak için VAE modeli |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Çıkış videosu genişliği (varsayılan: 1024, adım: 8) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Çıkış videosu yüksekliği (varsayılan: 576, adım: 8) |
| `video_frames` | INT | Evet | 1 - 4096 | Videoda üretilecek kare sayısı (varsayılan: 14) |
| `motion_bucket_id` | INT | Evet | 1 - 1023 | Üretilen videodaki hareket miktarını kontrol eder (varsayılan: 127) |
| `fps` | INT | Evet | 1 - 1024 | Üretilen video için saniyedeki kare sayısı (varsayılan: 6) |
| `augmentation_level` | FLOAT | Evet | 0.0 - 10.0 | Giriş görüntüsüne uygulanacak gürültü artırım seviyesi (varsayılan: 0.0, adım: 0.01) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Görüntü yerleştirmelerini ve video parametrelerini içeren pozitif koşullandırma verisi |
| `negative` | CONDITIONING | Sıfırlanmış yerleştirmeler ve video parametreleri içeren negatif koşullandırma verisi |
| `latent` | LATENT | Video üretimi için hazır boş gizli uzay tensörü |