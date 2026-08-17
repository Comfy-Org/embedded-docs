# ReferenceTimbreAudio

Bu düğüm, "ace step 1.5" işleminde kullanılmak üzere bir referans ses tınısı ayarlar. Bir conditioning girdisi ve sesin isteğe bağlı bir latent temsilini alır, ardından bu latent verisini conditioning'e ekler; böylece iş akışındaki sonraki düğümler bunu referans ses olarak kullanabilir. Eğer latent sağlanmazsa, conditioning değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Referans ses bilgisinin ekleneceği conditioning verisi. | CONDITIONING | Evet |  |
| `latent` | Referans sesin isteğe bağlı latent temsili. Sağlandığında, örnekleri conditioning'e eklenir. | LATENT | Hayır |  |

`latent` sağlandığında, örnekleri conditioning'in referans ses tınısı latentlerine eklenir. Eğer `latent` sağlanmazsa, orijinal conditioning değiştirilmeden iletilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | İsteğe bağlı `latent` girdisi sağlandıysa artık referans ses tınısı latentlerini içeren değiştirilmiş conditioning verisi. Eğer latent sağlanmazsa, orijinal conditioning değiştirilmeden döndürülür. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
