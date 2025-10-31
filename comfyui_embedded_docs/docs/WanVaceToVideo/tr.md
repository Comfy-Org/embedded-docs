> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

WanVaceToVideo düğümü, video üretim modelleri için video koşullandırma verilerini işler. Pozitif ve negatif koşullandırma girişlerini video kontrol verileriyle birlikte alır ve video üretimi için gizli temsilleri hazırlar. Düğüm, video modelleri için uygun koşullandırma yapısını oluşturmak üzere video yükseltme, maskeleme ve VAE kodlama işlemlerini gerçekleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Üretimi yönlendirmek için pozitif koşullandırma girişi |
| `negative` | CONDITIONING | Evet | - | Üretimi yönlendirmek için negatif koşullandırma girişi |
| `vae` | VAE | Evet | - | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16 to MAX_RESOLUTION | Çıkış videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 to MAX_RESOLUTION | Çıkış videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 to MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 to 4096 | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `strength` | FLOAT | Evet | 0.0 to 1000.0 | Video koşullandırma için kontrol gücü (varsayılan: 1.0, adım: 0.01) |
| `control_video` | IMAGE | Hayır | - | Kontrol koşullandırması için isteğe bağlı giriş videosu |
| `control_masks` | MASK | Hayır | - | Videoda hangi bölümlerin değiştirileceğini kontrol etmek için isteğe bağlı maskeler |
| `reference_image` | IMAGE | Hayır | - | Ek koşullandırma için isteğe bağlı referans görüntüsü |

**Not:** `control_video` sağlandığında, belirtilen genişlik ve yüksekliğe uyacak şekilde yükseltilir. `control_masks` sağlandığında, kontrol videosunun boyutlarıyla eşleşmelidir. `reference_image` sağlandığında, VAE üzerinden kodlanır ve gizli diziye ön eklenir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video kontrol verisi uygulanmış pozitif koşullandırma |
| `negative` | CONDITIONING | Video kontrol verisi uygulanmış negatif koşullandırma |
| `latent` | LATENT | Video üretimi için hazır boş gizli tensör |
| `trim_latent` | INT | Referans görüntüsü kullanıldığında kırpılacak gizli kare sayısı |