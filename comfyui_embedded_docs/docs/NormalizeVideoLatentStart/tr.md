# NormalizeVideoLatentStart

Bu düğüm, bir video latentinin ilk birkaç karesini, kendilerinden sonra gelen karelere daha çok benzemeleri için ayarlar. Videonun ilerleyen kısımlarındaki bir referans kare kümesinden ortalama ve varyasyonu hesaplar ve aynı özellikleri başlangıç karelerine uygular. Bu, başlangıç kareleri ile videonun geri kalanı arasındaki farkları azaltmaya yardımcı olur ve daha yumuşak, daha tutarlı bir geçiş oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İşlenecek video latent temsili. | LATENT | Evet | - |
| `start_frame_count` | Başlangıçtan itibaren sayılan, normalleştirilecek latent kare sayısı (varsayılan: 4). | INT | Evet | 1 - 16384 (maksimum çözünürlük) |
| `reference_frame_count` | Başlangıç karelerinden sonra referans olarak kullanılacak latent kare sayısı (varsayılan: 5). | INT | Evet | 1 - 16384 (maksimum çözünürlük) |

**Not:** Referans kareler, `start_frame_count` karelerinden hemen sonra başlayarak alınır. Kullanılabilir kare sayısı, `reference_frame_count` değerinin istediğinden azsa düğüm, mevcut olduğu kadarını kullanır (latent toplam kare sayısından en fazla bir eksik). Video latentinde yalnızca 1 kare varsa normalleştirme yapılmaz ve orijinal latent değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Başlangıç kareleri normalleştirilmiş işlenmiş video latent temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
