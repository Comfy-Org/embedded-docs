# Wan22FunControlToVideo

The Wan22FunControlToVideo düğümü, Wan video modeliyle video oluşturmak için koşullandırma verilerini ve boş bir latent tensörünü hazırlar. İsteğe bağlı referans görüntülerini ve kontrol videolarını latent uzaya kodlar, bunları pozitif ve negatif koşullandırmaya ekler ve istenen video için doğru uzamsal ve zamansal boyutlara sahip sıfırlarla doldurulmuş bir latent tensör oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Video oluşturmayı yönlendirmek için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `ref_image` | Oluşturma için görsel rehberlik sağlayan isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Oluşturma sürecini yönlendiren isteğe bağlı kontrol videosu | IMAGE | Hayır | - |

**Not:** `length` parametresi 4 karelik adımlarla işlenir ve düğüm, latent uzayı oluştururken zamansal ölçeklemeyi otomatik olarak uygular. `ref_image` sağlandığında yalnızca ilk karesi kodlanır (`width` x `height` boyutuna yeniden boyutlandırılır) ve referans latentleri olarak koşullandırmaya eklenir. `control_video` sağlandığında `length` karesine kısaltılır, yeniden boyutlandırılır, kodlanır ve koşullandırma tarafından kullanılan birleştirilmiş latent içine yerleştirilir. Birleştirilmiş latent, kanal boyutu boyunca çoğaltılır ve kanal düzeni VAE'nin latent kanal sayısına bağlıdır (48 kanal Wan 2.2 biçimini, aksi halde Wan 2.1 biçimini kullanır). `start_image` parametresine yürütme mantığında başvurulur, ancak düğümün girdi şemasında gösterilmez; bu nedenle düğüm arayüzünden ayarlanamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video'ya özgü latent verileri eklenmiş pozitif koşullandırma; birleştirilmiş latent, maske ve isteğe bağlı referans latentlerini içerir | CONDITIONING |
| `negative` | Video'ya özgü latent verileri eklenmiş negatif koşullandırma; birleştirilmiş latent, maske ve isteğe bağlı referans latentlerini içerir | CONDITIONING |
| `latent` | Video oluşturma için hazırlanmış boş latent tensör; batch boyutu, latent kanalları, uzunluk, yükseklik ve genişliğe göre boyutlandırılır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
