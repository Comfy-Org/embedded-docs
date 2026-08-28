# Wan22FunControlToVideo

Wan22FunControlToVideo düğümü, Wan video modeli ile video üretimi için koşullandırma verilerini ve boş bir latent tensörü hazırlar. İsteğe bağlı referans görüntülerini ve kontrol videolarını gizli uzaya kodlar, bunları pozitif ve negatif koşullandırmaya ekler ve istenen video için doğru uzamsal ve zamansal boyutlara sahip sıfırlarla doldurulmuş bir latent tensörü oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Video üretimini yönlendirmek için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `ref_image` | Üretim için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Üretim sürecini yönlendiren isteğe bağlı kontrol videosu | IMAGE | Hayır | - |

**Not:** `length` parametresi 4 karelik adımlarla işlenir ve düğüm, gizli uzayı oluştururken otomatik olarak zamansal ölçekleme uygular. `ref_image` sağlandığında yalnızca ilk karesi kodlanır ve referans latentleri olarak koşullandırmaya eklenir. `control_video` sağlandığında `length` kareye kırpılır, kodlanır ve koşullandırma tarafından kullanılan concat latent içine yerleştirilir. `start_image` parametresi yürütme mantığında başvurulur ancak düğümün girdi şemasında bulunmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Videoya özgü latent veriler eklenmiş pozitif koşullandırma; concat latent, maske ve isteğe bağlı referans latentlerini içerir | CONDITIONING |
| `negative` | Videoya özgü latent veriler eklenmiş negatif koşullandırma; concat latent, maske ve isteğe bağlı referans latentlerini içerir | CONDITIONING |
| `latent` | Video üretimi için hazırlanmış boş latent tensörü; batch boyutu, latent kanalları, uzunluk, yükseklik ve genişliğe göre boyutlandırılır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
