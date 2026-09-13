# WanVace'denVideoya

WanVaceToVideo düğümü, VACE kontrollü video üretim modelleri için video koşullandırma verilerini hazırlar. Pozitif ve negatif koşullandırmayı isteğe bağlı kontrol videosu, kontrol maskeleri ve referans görüntüsüyle birleştirir, bunları bir VAE üzerinden kodlar ve güncellenmiş koşullandırma, boş bir latent tensörü ve bir trim değeri çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Üretimi yönlendirmek için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION |
| `height` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION |
| `length` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ile MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `strength` | VACE kontrolü için koşul gücü (varsayılan: 1.0, adım: 0.01). Bu bir LoRA gücü değildir. LoRA ağırlıkları ayrı LoRA düğümleri aracılığıyla uygulanır. | FLOAT | Evet | 0.0 ile 1000.0 |
| `control_video` | Kontrol koşullandırması için isteğe bağlı girdi videosu. Sağlanmazsa otomatik olarak nötr gri bir video oluşturulur. | IMAGE | Hayır | - |
| `control_masks` | Kontrol videosunun hangi bölümlerinin etkin olduğunu belirleyen isteğe bağlı maskeler. Sağlanmazsa tam beyaz bir maske kullanılır. | MASK | Hayır | - |
| `reference_image` | Ek koşullandırma için isteğe bağlı referans görüntüsü. Sağlandığında kodlanır ve latent dizisinin başına eklenir. Yalnızca ilk görüntü kullanılır. | IMAGE | Hayır | - |

**Not:** `control_video` sağlandığında, `length` kareye kırpılır ve belirtilen `width` ve `height` değerlerine ölçeklendirilir; `length` değerinden daha az karesi varsa, eksik kareler nötr gri (değer 0.5) ile doldurulur. Sağlanmadığında, otomatik olarak `length` karelik nötr gri bir video oluşturulur. `control_masks` belirtilen `width` ve `height` değerlerine ölçeklendirilir, `length` kareye kırpılır ve daha kısaysa 1.0 değeriyle doldurulur. Maske, kontrol videosunu etkin olmayan ve reaktif bölümlere ayırır; her biri VAE ile kodlanır ve kanal boyutu boyunca birleştirilir; maske ayrıca latent çözünürlüğe alt örneklenir. `reference_image` sağlandığında, ilk görüntüsü VAE ile kodlanır ve latent dizisinin başına eklenir ve `trim_latent`, eklenen latent kare sayısını bildirir. Latent kare sayısı `((length - 1) // 4) + 1` olarak hesaplanır ve latent uzamsal boyutları `height / 8` ve `width / 8` olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış pozitif koşullandırma | CONDITIONING |
| `negative` | Video kontrol verileri (vace_frames, vace_mask, vace_strength) uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | [batch_size, 16, latent_length, height/8, width/8] şeklinde video üretimi için hazır boş latent tensörü | LATENT |
| `trim_latent` | Referans görüntüsü kullanıldığında kırpılacak latent kare sayısı; referans görüntüsü sağlanmadıysa 0 | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
