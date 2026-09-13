# ReferenceTimbreAudio

Bu düğüm, "ace step 1.5" işlemi için referans sesi ayarlar. Bir `conditioning` girdisi ve isteğe bağlı olarak sesin bir latent gösterimini alır, ardından bu latent verisini conditioning'e ekler; böylece sonraki düğümler bunu referans ses tını latentleri olarak kullanabilir. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Referans ses bilgisinin ekleneceği conditioning verisi. | CONDITIONING | Evet |  |
| `latent` | Referans sesin isteğe bağlı latent gösterimi (varsayılan: None). Sağlandığında, örnekleri conditioning'e referans ses tını latentleri olarak eklenir. | LATENT | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Değiştirilmiş conditioning verisi; isteğe bağlı `latent` girdisi sağlanmışsa artık referans ses tını latentlerini içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
