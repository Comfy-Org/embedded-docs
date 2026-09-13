# FluxKontext Çoklu Referans Gizli Yöntemi

FluxKontextMultiReferenceLatentMethod düğümü, koşullandırma verisini içinde seçilen bir referans latent yöntemini saklayarak günceller. Saklanan yöntem, daha sonraki üretim adımlarında referans latentleri işlenirken kullanılır. Bu düğüm deneysel olarak işaretlenmiştir ve Flux koşullandırma sistemine aittir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Referans latent yöntemiyle değiştirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `reference_latents_method` | Referans latent işleme için kullanılan yöntem. "uxo" veya "uso" içeren bir değer seçilirse, saklanmadan önce "uxo" olarak dönüştürülür. Bu parametre gelişmiş olarak işaretlenmiştir. | COMBO | Evet | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Referans latent yöntemi uygulanmış değiştirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/tr.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
