# WanVace'denVideoya

WanVaceToVideo düğümü, video oluşturma modelleri için video koşullama verilerini işler. Pozitif ve negatif koşullama girdilerini video kontrol verileriyle birlikte alır ve video oluşturma için gizli temsiller hazırlar. Düğüm, video modelleri için uygun koşullama yapısını oluşturmak amacıyla video yükseltme, maskeleme ve VAE kodlama işlemlerini gerçekleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturmayı yönlendirmek için pozitif koşullama girdisi | CONDITIONING | Evet | - |
| `negatif` | Oluşturmayı yönlendirmek için negatif koşullama girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `güç` | Video koşullaması için kontrol gücü (varsayılan: 1,0, adım: 0,01) | FLOAT | Evet | 0,0 ila 1000,0 |
| `kontrol_videosu` | Kontrol koşullaması için isteğe bağlı video girdisi | IMAGE | Hayır | - |
| `kontrol_maskeleri` | Videonun hangi bölümlerinin değiştirileceğini kontrol etmek için isteğe bağlı maskeler | MASK | Hayır | - |
| `referans_görüntüsü` | Ek koşullama için isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |

**Not:** `control_video` sağlandığında, belirtilen genişlik ve yüksekliğe uyacak şekilde yükseltilecektir. `control_masks` sağlanırsa, kontrol videosunun boyutlarıyla eşleşmelidir. `reference_image` sağlandığında VAE aracılığıyla kodlanır ve gizli diziye başa eklenir.


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video kontrol verileri uygulanmış pozitif koşullama | CONDITIONING |
| `negative` | Video kontrol verileri uygulanmış negatif koşullama | CONDITIONING |
| `latent` | Video oluşturma için hazır boş gizli tensör | LATENT |
| `trim_latent` | Referans görüntüsü kullanıldığında kırpılacak gizli kare sayısı | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
