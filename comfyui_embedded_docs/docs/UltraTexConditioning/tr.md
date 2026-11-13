# UltraTex Conditioning

FLUX.2 Klein 9B'yi UltraTex LoRA ile koşullandırarak bir referans görüntünün görünümünü bir mesh üzerine boyar, görünüm başına bir görüntü olarak. Görünümleri Render Mesh ile `world normal` modunda, 4'lü ve üst-alt kutuplu bir Create Camera Orbit kullanarak oluşturun ve sonucu Bake Texture From Views ile fırınlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Metin koşullandırma. UltraTex boş bir istemle eğitilmiştir. | CONDITIONING | Evet | - |
| `vae` | Normalleri, görünümleri ve referansı kodlamak için kullanılan VAE. | VAE | Evet | - |
| `normals` | Render Mesh `world normal` görüntüleri: 6 kanonik görünüm veya 4 yan görünüm. | IMAGE | Evet | - |
| `masks` | Aynı görünümlerin Render Mesh maskeleri, görünüm başına bir tane. | MASK | Evet | - |
| `reference` | Nesnenin görünmesi gerektiği hali, ön kamera tarafından görüldüğü şekliyle. | IMAGE | Evet | - |
| `reference_mask` | Referansın nesne maskesi, nesne için beyaz. Varsayılan: tamamen beyaz. | MASK | Hayır | - |
| `extra_views` | Daha fazla referans: nesnenin diğer görünümlerden görüldüğü hali, her biri referansın ön görünüme bağlı olduğu gibi kendi görünümüne bağlıdır. Varsayılan: `"off"`. | DYNAMIC_COMBO | Evet | `"off"`<br>`"on"` |

### Ekstra Görünümler "on" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `right` | Nesnenin sağ görünümden görüldüğü hali. | IMAGE | Hayır | - |
| `back` | Nesnenin arka görünümden görüldüğü hali. | IMAGE | Hayır | - |
| `left` | Nesnenin sol görünümden görüldüğü hali. | IMAGE | Hayır | - |
| `top` | Nesnenin üst görünümden görüldüğü hali. | IMAGE | Hayır | - |
| `bottom` | Nesnenin alt görünümden görüldüğü hali. | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Görünüm ızgarasını, referans latentlerini ve UltraTex'in ihtiyaç duyduğu token maskelerini taşıyan koşullandırma. | CONDITIONING |

Not: `normals` ya 6 kanonik görünümü (Create Camera Orbit'te `count` 4 ve `poles` üst ve alt) ya da 4 yan görünümü içermelidir ve `masks` görünüm sayısıyla eşleşmelidir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
