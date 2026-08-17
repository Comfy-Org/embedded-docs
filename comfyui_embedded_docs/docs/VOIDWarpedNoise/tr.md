# VOIDWarpedNoise

VOID video iyileştirme sürecinin ikinci geçişi için zamansal olarak ilişkili gürültü üretir. Pass 1'den gelen çıktı videosunu alır ve Gauss gürültüsünü optik akış vektörleri boyunca çarpıtır; böylece video içeriğiyle tutarlı hareket eden gürültü oluşturur. Bu çarpıtılmış gürültü, Pass 2 için başlangıç latent'i olarak kullanılır ve nihai çıktıda zamansal tutarlılığı artırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `optical_flow` | OpticalFlowLoader'dan (RAFT-large) optik akış modeli. | OPTICAL_FLOW | Evet | - |
| `video` | Pass 1 çıktı video kareleri [T, H, W, 3]. | IMAGE | Evet | - |
| `width` | Çıktı latent'inin genişliği (varsayılan: 672). | INT | Evet | 16 ila MAX_RESOLUTION (adım 8) |
| `height` | Çıktı latent'inin yüksekliği (varsayılan: 384). | INT | Evet | 16 ila MAX_RESOLUTION (adım 8) |
| `length` | Piksel kare sayısı. latent_t'yi çift yapmak için aşağı yuvarlanır (patch_size_t=2 gereksinimi), örn. 49 → 45 (varsayılan: 45). | INT | Evet | 1 ila MAX_RESOLUTION (adım 1) |
| `batch_size` | Oluşturulacak özdeş gürültü dizilerinin sayısı (varsayılan: 1). | INT | Evet | 1 ila 64 |

**`length` parametresi hakkında not:** `length` değeri, çift bir `latent_t` boyutu üreten en yakın geçerli değere otomatik olarak aşağı yuvarlanır. Bu, CogVideoX-Fun-V1.5 modelinin `patch_size_t=2` kısıtı nedeniyle gereklidir. Yuvarlama gerçekleştiğinde bir uyarı günlüğe kaydedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `warped_noise` | Optik akış ile çarpıtılmış Gauss gürültüsü içeren 5B bir tensör (B, C, T, H, W); VOID Pass 2'de başlangıç latent'i olarak kullanılmaya hazırdır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/tr.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
