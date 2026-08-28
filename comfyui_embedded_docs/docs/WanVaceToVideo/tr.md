# WanVace'denVideoya

WanVaceToVideo düğümü, video üretim modelleri için video koşullandırma verilerini hazırlar. İsteğe bağlı bir kontrol videosu, maskeler ve referans görselin yanı sıra pozitif ve negatif koşullandırma girdilerini alır ve bunları video üretimini yönlendiren latent temsillere kodlar. Düğüm, video modelleri için uygun koşullandırma yapısını oluşturmak amacıyla yükseltme, dolgulama, maskeleme ve VAE kodlama işlemlerini yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretimi yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Üretimi yönlendirmek için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `güç` | VACE kontrolü için koşul gücü (varsayılan: 1.0, adım: 0.01). Bu bir LoRA gücü değildir. LoRA ağırlıkları ayrı LoRA düğümleri aracılığıyla uygulanır. | FLOAT | Evet | 0.0 ile 1000.0 |
| `kontrol_videosu` | Kontrol koşullandırması için kullanılan isteğe bağlı girdi videosu. Sağlanmazsa, otomatik olarak nötr gri bir video oluşturulur. | IMAGE | Hayır | - |
| `kontrol_maskeleri` | Kontrol videosunun hangi bölümlerinin etkin olduğunu belirleyen isteğe bağlı maskeler. Sağlanmazsa, tamamen beyaz bir maske kullanılır. | MASK | Hayır | - |
| `referans_görüntüsü` | Ek koşullandırma için isteğe bağlı referans görseli. Sağlandığında kodlanır ve latent dizilimin başına eklenir. | IMAGE | Hayır | - |

**Not:** `control_video` sağlandığında, `length` kareye kırpılır ve belirtilen `width` ve `height` değerlerine yükseltilir; `length` değerinden daha az karesi varsa, eksik kareler nötr gri (0.5 değeri) ile doldurulur. Sağlanmadığında, otomatik olarak `length` karelik nötr gri bir video oluşturulur. `control_masks`, belirtilen `width` ve `height` değerlerine yükseltilir, `length` kareye kırpılır ve daha kısaysa 1.0 değeri ile doldurulur. Maske, kontrol videosunu etkin olmayan ve tepkisel bölümlere ayırır; her biri VAE ile kodlanır ve kanal boyutu boyunca birleştirilir; maske ayrıca latent çözünürlüğe alt örneklenir. `reference_image` sağlandığında, VAE ile kodlanır ve latent dizilimin başına eklenir. Latent kare sayısı `((length - 1) // 4) + 1` olarak hesaplanır ve latent uzamsal boyutları `height / 8` ve `width / 8` değerleridir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış pozitif koşullandırma | CONDITIONING |
| `negatif` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış negatif koşullandırma | CONDITIONING |
| `gizli` | [batch_size, 16, latent_length, height/8, width/8] boyutlarıyla video üretimi için hazır boş latent tensör | LATENT |
| `gizliyi_kırp` | Referans görsel kullanıldığında kırpılacak latent kare sayısı; referans görsel sağlanmazsa 0 | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
