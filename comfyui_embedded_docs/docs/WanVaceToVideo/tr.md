> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

WanVaceToVideo düğümü, video oluşturma modelleri için video koşullama verilerini işler. Pozitif ve negatif koşullama girdilerini video kontrol verileriyle birlikte alır ve video oluşturma için gizli temsiller hazırlar. Düğüm, video modelleri için uygun koşullama yapısını oluşturmak amacıyla video yükseltme, maskeleme ve VAE kodlama işlemlerini gerçekleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Oluşturmayı yönlendirmek için pozitif koşullama girdisi |
| `negative` | CONDITIONING | Evet | - | Oluşturmayı yönlendirmek için negatif koşullama girdisi |
| `vae` | VAE | Evet | - | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16 ila MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 ila MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 ila MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 ila 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `strength` | FLOAT | Evet | 0,0 ila 1000,0 | Video koşullaması için kontrol gücü (varsayılan: 1,0, adım: 0,01) |
| `control_video` | IMAGE | Hayır | - | Kontrol koşullaması için isteğe bağlı video girdisi |
| `control_masks` | MASK | Hayır | - | Videonun hangi bölümlerinin değiştirileceğini kontrol etmek için isteğe bağlı maskeler |
| `reference_image` | IMAGE | Hayır | - | Ek koşullama için isteğe bağlı referans görüntüsü |

**Not:** `control_video` sağlandığında, belirtilen genişlik ve yüksekliğe uyacak şekilde yükseltilecektir. `control_masks` sağlanırsa, kontrol videosunun boyutlarıyla eşleşmelidir. `reference_image` sağlandığında VAE aracılığıyla kodlanır ve gizli diziye başa eklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Video kontrol verileri uygulanmış pozitif koşullama |
| `negative` | CONDITIONING | Video kontrol verileri uygulanmış negatif koşullama |
| `latent` | LATENT | Video oluşturma için hazır boş gizli tensör |
| `trim_latent` | INT | Referans görüntüsü kullanıldığında kırpılacak gizli kare sayısı |

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
