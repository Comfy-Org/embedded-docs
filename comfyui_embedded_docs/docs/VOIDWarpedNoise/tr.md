# VOIDWarpedNoise

VOID video iyileştirme sürecinin ikinci geçişi için zamansal olarak ilişkili gürültü üretir. Pass 1'den çıkan videoyu alır ve Gaussian gürültüsünü optik akış vektörleri boyunca çarpıtır, video içeriğiyle tutarlı hareket eden gürültü oluşturur. Bu çarpıtılmış gürültü, Pass 2 için başlangıç latent'i olarak kullanılır ve nihai çıktıda zamansal tutarlılığı artırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `optical_flow` | OpticalFlowLoader (RAFT-large) kaynaklı optik akış modeli. | OPTICAL_FLOW | Evet | - |
| `video` | Pass 1 çıktısı video kareleri [T, H, W, 3]. | IMAGE | Evet | - |
| `width` | Çıktı latent'inin genişliği (varsayılan: 672). | INT | Evet | 16 to MAX_RESOLUTION (step 8) |
| `height` | Çıktı latent'inin yüksekliği (varsayılan: 384). | INT | Evet | 16 to MAX_RESOLUTION (step 8) |
| `length` | Piksel kare sayısı. latent_t'nin çift olması için aşağı yuvarlanır (patch_size_t=2 gereksinimi), örn. 49 → 45 (varsayılan: 45). | INT | Evet | 1 to MAX_RESOLUTION (step 1) |
| `batch_size` | Oluşturulacak özdeş gürültü dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ile 64 |

**`length` parametresi hakkında not:** `length` değeri, çift bir `latent_t` boyutu üreten en yakın geçerli değere otomatik olarak aşağı yuvarlanır. Bu, CogVideoX-Fun-V1.5 modelinin `patch_size_t=2` kısıtlaması tarafından gerektirilir. Yuvarlama gerçekleştiğinde bir uyarı kaydedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `warped_noise` | Optik akışla çarpıtılmış Gaussian gürültüsü içeren 5D tensör (B, C, T, H, W), VOID Pass 2'de başlangıç latent'i olarak kullanıma hazır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/tr.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
