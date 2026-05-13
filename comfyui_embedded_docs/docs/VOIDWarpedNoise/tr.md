> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/tr.md)

## Genel Bakış

VOID video iyileştirme sürecinin ikinci geçişi için zamansal olarak ilişkili gürültü üretir. Pass 1'den gelen çıktı videosunu alır ve Gauss gürültüsünü optik akış vektörleri boyunca bükerek, video içeriğiyle tutarlı bir şekilde hareket eden gürültü oluşturur. Bu bükülmüş gürültü, Pass 2 için başlangıç gizli uzayı olarak kullanılır ve nihai çıktıda zamansal tutarlılığı artırır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `optical_flow` | MODEL | Evet | - | OpticalFlowLoader'dan (RAFT-large) gelen optik akış modeli. |
| `video` | IMAGE | Evet | - | Pass 1 çıktı video kareleri [T, H, W, 3]. |
| `width` | INT | Evet | 16 ile MAX_RESOLUTION (adım 8) | Çıktı gizli uzayının genişliği (varsayılan: 672). |
| `height` | INT | Evet | 16 ile MAX_RESOLUTION (adım 8) | Çıktı gizli uzayının yüksekliği (varsayılan: 384). |
| `length` | INT | Evet | 1 ile MAX_RESOLUTION (adım 1) | Piksel kare sayısı. latent_t'yi çift yapmak için aşağı yuvarlanır (patch_size_t=2 gereksinimi), örn. 49 → 45 (varsayılan: 45). |
| `batch_size` | INT | Evet | 1 ile 64 | Oluşturulacak özdeş gürültü dizisi sayısı (varsayılan: 1). |

**`length` parametresi hakkında not:** `length` değeri, çift `latent_t` boyutu üreten en yakın geçerli değere otomatik olarak aşağı yuvarlanır. Bu, CogVideoX-Fun-V1.5 modelinin `patch_size_t=2` kısıtlaması nedeniyle gereklidir. Yuvarlama işlemi gerçekleştiğinde bir uyarı kaydedilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `warped_noise` | LATENT | Optik akışla bükülmüş Gauss gürültüsü içeren 5B tensör (B, C, T, H, W), VOID Pass 2'de başlangıç gizli uzayı olarak kullanılmaya hazırdır. |

---
**Source fingerprint (SHA-256):** `a0f986e54bcc6c455220f89f5d840585a9eae081e522ea11e0ce37ab46821bd9`
