# NormalizeVideoLatentStart

Bu düğüm, bir video gizilinin (latent) ilk birkaç karesini, sonraki karelere daha çok benzeyecek şekilde ayarlar. Videoda daha sonraki bir dizi referans karesinden ortalama ve varyansı hesaplar ve bu özellikleri başlangıç karelerine uygular. Bu, videonun başlangıcında daha yumuşak ve tutarlı bir görsel geçiş oluşturmaya yardımcı olur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İşlenecek video gizil temsili. | LATENT | Evet | - |
| `start_frame_count` | Başlangıçtan itibaren sayılarak normalleştirilecek gizil kare sayısı (varsayılan: 4). | INT | Evet | 1 ila 16384 |
| `reference_frame_count` | Başlangıç karelerinden sonra referans olarak kullanılacak gizil kare sayısı (varsayılan: 5). | INT | Evet | 1 ila 16384 |

**Not:** `reference_frame_count` değeri, başlangıç karelerinden sonra kullanılabilir kare sayısıyla otomatik olarak sınırlanır. Video gizili yalnızca 1 kare uzunluğundaysa, herhangi bir normalleştirme yapılmaz ve orijinal gizil değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Başlangıç kareleri normalleştirilmiş, işlenmiş video gizili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`
