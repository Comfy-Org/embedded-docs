# WanVace'denVideoya

WanVaceToVideo düğümü, video üretim modelleri için video koşullandırma verilerini işler. Pozitif ve negatif koşullandırma girdilerini video kontrol verileriyle birlikte alır ve video üretimi için latent temsiller hazırlar. Düğüm, video modelleri için uygun koşullandırma yapısını oluşturmak üzere video ölçekleme, maskeleme ve VAE kodlama işlemlerini yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Üretimi yönlendirmek için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `height` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `length` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `strength` | VACE kontrolü için koşullandırma gücü (varsayılan: 1.0, adım: 0.01). Bu bir LoRA gücü değildir. LoRA ağırlıkları ayrı LoRA düğümleri aracılığıyla uygulanır. | FLOAT | Evet | 0.0 ila 1000.0 |
| `control_video` | Kontrol koşullandırması için isteğe bağlı girdi videosu. Sağlanmazsa, otomatik olarak nötr gri bir video oluşturulur. Sağlandığında, `width` × `height` boyutuna ölçeklenir ve ilk `length` kareyle sınırlandırılır; daha az kareye sahipse, eksik kareler nötr gri ile doldurulur. | IMAGE | Hayır | - |
| `control_masks` | Videonun hangi bölümlerinin değiştirileceğini kontrol etmek için isteğe bağlı maskeler. Sağlanmazsa, tamamen beyaz bir maske kullanılır. Sağlandığında, maske `width` × `height` boyutuna ölçeklenir, `length` kareyle sınırlandırılır ve daha az kareye sahipse beyaz ile doldurulur. | MASK | Hayır | - |
| `reference_image` | Ek koşullandırma için isteğe bağlı referans görüntüsü. Sağlandığında, `width` × `height` boyutuna ölçeklenir, VAE tarafından kodlanır ve latent dizinin başına eklenir. | IMAGE | Hayır | - |

**Not:** `control_video` sağlandığında, belirtilen `width` ve `height` değerlerine ölçeklenir. `control_masks` sağlanırsa, aynı boyutlara ölçeklenir. `reference_image` sağlandığında VAE aracılığıyla kodlanır ve latent dizinin başına eklenir. `length` parametresi kare sayısını belirler ve latent uzunluk `((length - 1) // 4) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış pozitif koşullandırma | CONDITIONING |
| `negative` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | Video üretimi için hazır, [batch_size, 16, latent_length, height/8, width/8] şeklinde boş latent tensörü | LATENT |
| `trim_latent` | Referans görüntüsü kullanıldığında kırpılacak latent kare sayısı (referans görüntüsü sağlanmazsa 0) | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
