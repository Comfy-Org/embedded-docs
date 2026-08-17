# FluxKontext Çoklu Referans Gizli Yöntemi

FluxKontextMultiReferenceLatentMethod düğümü, belirli bir referans latent yöntemini ayarlayarak conditioning verisini değiştirir. Seçilen yöntemi conditioning girdisine ekler ve bu, sonraki üretim adımlarında referans latentlerin nasıl işleneceğini etkiler. Bu düğüm deneysel olarak işaretlenmiştir ve Flux conditioning sisteminin bir parçasıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Referans latent yöntemiyle değiştirilecek conditioning verisi | CONDITIONING | Evet | - |
| `reference_latents_method` | Referans latent işleme için kullanılacak yöntem. "uxo" veya "uso" seçilirse, "uxo"ya dönüştürülür. Bu parametre gelişmiş olarak işaretlenmiştir. | COMBO | Evet | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Referans latent yöntemi uygulanmış değiştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/tr.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
