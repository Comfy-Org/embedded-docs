# SUPIRApply

SUPIRApply düğümü, bir difüzyon modeline SUPIR model yaması uygular. Yamayı kullanarak modelin davranışını değiştirir ve örnekleme işlemi sırasında bir girdi görüntüsünden gelen yönlendirmeyi dahil etmesine olanak tanır. Düğüm ayrıca bu yönlendirmenin gücünü zaman içinde ayarlamak için kontroller sağlar ve orijinal girdiye sadakati korumaya yardımcı olan isteğe bağlı bir özellik içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SUPIR yamasının uygulanacağı temel difüzyon modeli. | MODEL | Evet | - |
| `model_patch` | Modeli değiştirmek için ağırlıkları ve yapılandırmayı içeren SUPIR model yaması. | MODELPATCH | Evet | - |
| `vae` | Girdi görüntüsünü bir latent temsile kodlamak için kullanılan VAE (Varyasyonel Otomatik Kodlayıcı). | VAE | Evet | - |
| `image` | Üretim sürecini yönlendirmek için kullanılan girdi görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır. | IMAGE | Evet | - |
| `strength_start` | Örneklemenin başlangıcındaki (yüksek sigma) kontrol gücü. Görüntü yönlendirmesinin etkisi bu değerde başlar. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `strength_end` | Örneklemenin sonundaki (düşük sigma) kontrol gücü. Başlangıçtan itibaren doğrusal olarak enterpole edilir. Görüntü yönlendirmesinin etkisi bu değerde sona erer. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `restore_cfg` | Gürültü giderilmiş çıktıyı girdi latentine doğru çeker. Daha yüksek = girdiye daha güçlü sadakat. Devre dışı bırakmak için 0. (varsayılan: 4.0) | FLOAT | Hayır | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | restore_cfg'nin devre dışı bırakıldığı sigma eşiği. (varsayılan: 0.05) | FLOAT | Hayır | 0.0 - 1.0 |

*Not:* `image` girdisi yalnızca RGB kanallarını çıkarmak için işlenir. Alfa kanalı olan bir görüntü sağlanırsa, alfa kanalı yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | SUPIR yaması uygulanmış ve ek post-CFG işlevleri yapılandırılmış difüzyon modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/tr.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
