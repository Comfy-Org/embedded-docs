# SUPIRApply

SUPIRApply düğümü, bir SUPIR model yamasını bir difüzyon modeline uygular. Yama, örnekleme işlemi sırasında bir giriş görüntüsünden gelen yönlendirmeyi modele dahil etmesine olanak tanıyacak şekilde modelin davranışını değiştirmek için kullanılır. Düğüm ayrıca bu yönlendirmenin gücünü zaman içinde ayarlamak için kontroller sunar ve özgün girişe sadakati korumaya yardımcı olacak isteğe bağlı bir özellik içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SUPIR yamasının uygulanacağı temel difüzyon modeli. | MODEL | Evet | - |
| `model_patch` | Modeli değiştirmeye yönelik ağırlıkları ve yapılandırmayı içeren SUPIR model yaması. | MODEL_PATCH | Evet | - |
| `vae` | Giriş görüntüsünü gizli bir temsile kodlamak için kullanılan VAE (Variational Autoencoder). | VAE | Evet | - |
| `image` | Üretim sürecini yönlendirmek için kullanılan giriş görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır. | IMAGE | Evet | - |
| `strength_start` | Örneklemenin başlangıcındaki (yüksek sigma) kontrol gücü. Görüntü yönlendirmesinin etkisi bu değerde başlar. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `strength_end` | Örneklemenin sonundaki (düşük sigma) kontrol gücü. Başlangıçtan doğrusal olarak enterpole edilir. Görüntü yönlendirmesinin etkisi bu değerde sona erer. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `restore_cfg` | Gürültüden arındırılmış çıktıyı giriş latentine doğru çeker. Daha yüksek değer, girişe daha güçlü sadakat anlamına gelir. Devre dışı bırakmak için 0. (varsayılan: 4.0, gelişmiş ayar) | FLOAT | Evet | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Altında `restore_cfg`'nin devre dışı bırakıldığı sigma eşiği. (varsayılan: 0.05, gelişmiş ayar) | FLOAT | Evet | 0.0 - 1.0 |

*Not:* `image` girişi, yalnızca RGB kanallarını çıkaracak şekilde işlenir. Alfa kanalı olan bir görüntü sağlanırsa, alfa kanalı yok sayılır.

*Not:* SUPIR model yaması gürültü giderme kodlayıcısı ağırlıkları sağlıyorsa, giriş görüntüsü normal VAE kodlayıcısı yerine bu ağırlıklarla kodlanır.

*Not:* `restore_cfg` yalnızca 0'dan büyük bir değere ayarlandığında etkili olur. 0 olarak ayarlanması, geri yükleme sonrası işlemeyi tamamen devre dışı bırakır. Etkin olduğunda, düzeltme yalnızca geçerli sigma değeri `restore_cfg_s_tmin` değerinin üzerindeyken uygulanır.

*Not:* Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | SUPIR yaması uygulanmış ve CFG sonrası ek işlevleri yapılandırılmış giriş modelinin klonlanmış bir kopyası. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/tr.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
