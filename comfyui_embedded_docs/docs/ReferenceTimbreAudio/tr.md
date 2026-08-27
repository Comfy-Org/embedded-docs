# ReferenceTimbreAudio

Bu düğüm, "ace step 1.5" sürecinde kullanılmak üzere bir referans ses tınısı ayarlar. Bir conditioning girdisi ve isteğe bağlı olarak bir sesin latent temsilini alır; ardından bu latent veriyi conditioning'e ekleyerek iş akışındaki sonraki düğümler tarafından kullanılmasını sağlar. Bu düğüm şu anda deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Referans ses bilgisinin ekleneceği conditioning verisi. | CONDITIONING | Evet |  |
| `latent` | Referans sesin isteğe bağlı latent temsili. Sağlandığında, örnekleri conditioning'e eklenir ve referans ses tınısı latentleri olarak kullanılabilir. | LATENT | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | İsteğe bağlı `latent` girdisi sağlandıysa, artık referans ses tınısı latentlerini içeren değiştirilmiş conditioning verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
