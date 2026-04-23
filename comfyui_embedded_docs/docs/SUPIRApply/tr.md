> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/tr.md)

SUPIRApply düğümü, bir SUPIR model yamasını bir difüzyon modeline uygular. Bu yamayı kullanarak modelin davranışını değiştirir ve örnekleme işlemi sırasında bir girdi görüntüsünden gelen yönlendirmeyi dahil etmesini sağlar. Düğüm ayrıca bu yönlendirmenin gücünü zaman içinde ayarlamak için kontroller sağlar ve orijinal girdiye olan bağlılığı korumaya yardımcı olan isteğe bağlı bir özellik içerir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | SUPIR yamasının uygulanacağı temel difüzyon modeli. |
| `model_patch` | MODELPATCH | Evet | - | Modeli değiştirmek için ağırlıkları ve yapılandırmayı içeren SUPIR model yaması. |
| `vae` | VAE | Evet | - | Girdi görüntüsünü bir gizli temsile kodlamak için kullanılan VAE (Değişken Otomatik Kodlayıcı). |
| `image` | IMAGE | Evet | - | Üretim sürecini yönlendirmek için kullanılan girdi görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır. |
| `strength_start` | FLOAT | Hayır | 0.0 - 10.0 | Örneklemenin başlangıcındaki (yüksek sigma) kontrol gücü. Görüntü yönlendirmesinin etkisi bu değerle başlar. (varsayılan: 1.0) |
| `strength_end` | FLOAT | Hayır | 0.0 - 10.0 | Örneklemenin sonundaki (düşük sigma) kontrol gücü. Başlangıçtan itibaren doğrusal olarak enterpole edilir. Görüntü yönlendirmesinin etkisi bu değerle biter. (varsayılan: 1.0) |
| `restore_cfg` | FLOAT | Hayır | 0.0 - 20.0 | Gürültü giderilmiş çıktıyı girdi gizli temsiline doğru çeker. Daha yüksek = girdiye daha güçlü bağlılık. Devre dışı bırakmak için 0. (varsayılan: 4.0) |
| `restore_cfg_s_tmin` | FLOAT | Hayır | 0.0 - 1.0 | restore_cfg'nin devre dışı bırakıldığı sigma eşiği. (varsayılan: 0.05) |

*Not:* `image` girdisi yalnızca RGB kanallarını çıkarmak için işlenir. Alfa kanalına sahip bir görüntü sağlanırsa, alfa kanalı yok sayılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `model` | MODEL | SUPIR yaması uygulanmış ve gerekli ek post-CFG işlevleri yapılandırılmış difüzyon modeli. |