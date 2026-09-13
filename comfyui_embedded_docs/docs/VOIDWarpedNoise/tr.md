# VOIDWarpedNoise

VOID video iyileştirme sürecinin ikinci geçişi için zamansal olarak ilişkili gürültü üretir. Pass 1 çıktı videosunu alır ve Gauss gürültüsünü optik akış vektörleri boyunca büker; böylece gürültü video içeriğiyle tutarlı biçimde hareket eder. Ortaya çıkan bükülmüş gürültü, Pass 2 için başlangıç latent'i olarak kullanılır ve bu, nihai çıktıda zamansal tutarlılığı iyileştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `optical_flow` | OpticalFlowLoader'dan alınan optik akış modeli (RAFT-large). | OPTICAL_FLOW | Evet | - |
| `video` | Pass 1 çıktı video kareleri [T, H, W, 3]. | IMAGE | Evet | - |
| `width` | Piksel cinsinden hedef genişlik (varsayılan: 672). Gürültü üretilmeden önce giriş videosu bu genişliğe ölçeklenir ve latent genişliği width ÷ 8 olarak türetilir. | INT | Evet | 16 to MAX_RESOLUTION (adım: 8) |
| `height` | Piksel cinsinden hedef yükseklik (varsayılan: 384). Gürültü üretilmeden önce giriş videosu bu yüksekliğe ölçeklenir ve latent yüksekliği height ÷ 8 olarak türetilir. | INT | Evet | 16 to MAX_RESOLUTION (adım: 8) |
| `length` | Piksel kare sayısı. `latent_t` değerini çift yapmak için aşağı yuvarlanır (patch_size_t=2 gereksinimi), örn. 49, 45 olur (varsayılan: 45). | INT | Evet | 1 to MAX_RESOLUTION (adım: 1) |
| `batch_size` | Üretilecek özdeş bükülmüş gürültü dizisi sayısı (varsayılan: 1). Üretilen gürültü, batch boyutu boyunca bu sayı kadar tekrarlanır. | INT | Evet | 1 ile 64 |

**`length` parametresiyle ilgili not:** `length` değeri, CogVideoX-Fun-V1.5 modelinin `patch_size_t=2` kısıtı gereği, çift `latent_t` boyutu üreten en yakın değere otomatik olarak aşağı yuvarlanır (örneğin, 49, 45 olur). Bu yuvarlama gerçekleştiğinde düğüm bir uyarı kaydeder. Ayarlanan `length` değerinin ötesindeki kareler yok sayılır ve gürültü, ortaya çıkan latent kare sayısına yeniden örneklenir.

**`width` ve `height` ile ilgili not:** Bu değerler hem gelen video karelerini yeniden boyutlandırmak (çift doğrusal, merkez kırpma) hem de nihai latent çözünürlüğünü belirlemek (8'e bölünür) için kullanılır. Üretilen gürültü istenen latent boyutuyla eşleşmezse, sığacak şekilde yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `warped_noise` | VOID Pass 2'de başlangıç latent'i olarak kullanıma hazır, optik akışla bükülmüş Gauss gürültüsü içeren 5 boyutlu tensör (B, C, T, H, W). | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/tr.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
