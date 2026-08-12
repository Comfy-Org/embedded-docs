# WanAnimate2ToVideo

WanAnimate2ToVideo, bir referans görüntüsündeki karakteri, ayrı bir poz videosundan yüz ifadelerini, vücut hareketlerini ve el jestlerini aktararak canlandırır. Video üretim örnekleyicisinin animasyonu oluşturmak için kullandığı koşullandırma verilerini ve bir başlangıç latentini oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Video üretimi için pozitif koşullandırma. | CONDITIONING | Evet | Yok |
| `negative` | Video üretimi için negatif koşullandırma. | CONDITIONING | Evet | Yok |
| `vae` | Referans görüntüsünü ve video karelerini latent uzaya kodlamak için kullanılan VAE. | VAE | Evet | Yok |
| `width` | Çıktı videosunun piksel cinsinden genişliği. (varsayılan: 832) | INT | Evet | 16 ile MAX_RESOLUTION (adım 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği. (varsayılan: 480) | INT | Evet | 16 ile MAX_RESOLUTION (adım 16) |
| `length` | Oluşturulacak kare sayısı. (varsayılan: 81) | INT | Evet | 1 ile MAX_RESOLUTION (adım 4) |
| `batch_size` | Aynı anda oluşturulacak video sayısı. (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `reference_image` | Canlandırılacak karakter. Belirtilmezse siyah bir görüntü kullanılır. | IMAGE | Hayır | Yok |
| `pose_video` | Hareketi referans karaktere aktarılan video. Kare sayısı `length` değerinden azsa, eksik kareleri doldurmak için son kare tekrarlanır. | IMAGE | Hayır | Yok |
| `clip_vision_output` | Referans görüntüsünün CLIP vision çıktısı. | CLIP_VISION_OUTPUT | Hayır | Yok |
| `positive_pose` | Poz videosu dalı için istem; karakteri değil hareketi tanımlar. Varsayılan olarak `positive` değerini alır. Hem koşullu hem koşulsuz geçişlerde kullanılır. | CONDITIONING | Hayır | Yok |
| `clip_vision_output_pose` | Poz videosunun ilk karesinin CLIP vision çıktısı. Varsayılan olarak `clip_vision_output` değerini alır. | CLIP_VISION_OUTPUT | Hayır | Yok |
| `continue_motion` | Zamansal tutarlılık için devam ettirilecek önceki hareket dizisi. Bu dizinin yalnızca son karesi başlangıç hareket karesi olarak kullanılır. | IMAGE | Hayır | Yok |
| `video_frame_offset` | Poz videosunda atlanacak kare sayısı. Uzatma yaparken önceki düğümün `video_frame_offset` çıktısına bağlayın. (varsayılan: 0) | INT | Evet | 0 ile MAX_RESOLUTION |
| `pose_strength` | Poz videosunun hareket üzerindeki etkisini ölçekler. 1.0 eğitilmiş davranıştır; altı uyumu zayıflatır, üstü güçlendirir. 0.0 etkisini susturur ancak tamamen kaldırmaz. (varsayılan: 1.0) | FLOAT | Evet | 0.00 ile 10.00 (adım 0.01) |
| `pose_start_percent` | Poz etkisinin başladığı örnekleme yüzdesi. Pencerenin dışında poz dalı tamamen atlanır, bu da o adımları hızlandırır. (varsayılan: 0.0) | FLOAT | Evet | 0.00 ile 1.00 (adım 0.01) |
| `pose_end_percent` | Poz etkisinin bittiği örnekleme yüzdesi. Hareket çoğunlukla erken oluşur, bu nedenle ör. 0.7 koreografiyi korurken ince ayrıntıları gevşetebilir. (varsayılan: 1.0) | FLOAT | Evet | 0.00 ile 1.00 (adım 0.01) |
| `reference_image_strength` | Oluşturulan karelerin referans görüntüsünün latent karesine ne kadar güçlü odaklanacağını ölçekler. 1.0'ın altı kimlik/görünüm uyumunu gevşetir (ör. istemin yeniden stilize etmesine izin vermek için), üstü ise sürüklenmeye karşı sıkılaştırır. (varsayılan: 1.0) | FLOAT | Evet | 0.00 ile 10.00 (adım 0.01) |

**Doğrulama notları:**

- `pose_start_percent`, `pose_end_percent` değerinden büyük olmamalıdır; aksi takdirde düğüm bir ValueError yükseltir.
- `pose_video` sağlanırsa, kare sayısı `video_frame_offset` değerinden büyük olmalıdır; aksi takdirde düğüm bir ValueError yükseltir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Örnekleme için pozitif koşullandırma; referans görüntüsü, maske ve isteğe bağlı poz verisi eklenmiş. | CONDITIONING |
| `negative` | Örnekleme için negatif koşullandırma; aynı referans görüntüsü, maske ve isteğe bağlı poz verisi eklenmiş. | CONDITIONING |
| `latent` | Video örnekleyicisi için sıfırlarla doldurulmuş başlangıç latenti; kod çözmeden önce ilk `trim_latent` kare kaldırılmalıdır. | LATENT |
| `trim_latent` | Kod çözmeden önce kırpılması gereken latent kare sayısı. | INT |
| `trim_image` | Bir video uzatılırken örtüşen görüntü karelerinin sayısı. | INT |
| `video_frame_offset` | Poz videosunda atlanacak kare sayısı; ayarlanmış giriş ofseti ile oluşturulan kare sayısının toplamına eşittir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
