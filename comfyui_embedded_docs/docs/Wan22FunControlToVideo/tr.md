> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/tr.md)

Wan22FunControlToVideo düğümü, Wan video model mimarisi kullanılarak video üretimi için koşullandırma ve gizli temsilleri hazırlar. Pozitif ve negatif koşullandırma girdilerini, isteğe bağlı referans görüntüler ve kontrol videoları ile birlikte işleyerek video sentezi için gerekli gizli uzay temsillerini oluşturur. Düğüm, video modelleri için uygun koşullandırma verisi oluşturmak üzere uzamsal ölçekleme ve zamansal boyutları işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Hayır | 1 - MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Hayır | 1 - 4096 | Üretilecek video dizisi sayısı (varsayılan: 1) |
| `ref_image` | IMAGE | Hayır | - | Görsel rehberlik sağlamak için isteğe bağlı referans görüntü |
| `control_video` | IMAGE | Hayır | - | Üretim sürecini yönlendirmek için isteğe bağlı kontrol videosu |

**Not:** `length` parametresi 4 karelik gruplar halinde işlenir ve düğüm, gizli uzay için zamansal ölçeklemeyi otomatik olarak yönetir. `ref_image` sağlandığında, koşullandırmayı referans gizli temsiller aracılığıyla etkiler. `control_video` sağlandığında, koşullandırmada kullanılan birleştirilmiş gizli temsili doğrudan etkiler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video özel gizli veri içeren değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Video özel gizli veri içeren değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video üretimi için uygun boyutlara sahip boş gizli tensör |