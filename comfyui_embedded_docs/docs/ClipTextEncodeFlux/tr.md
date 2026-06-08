`CLIPTextEncodeFlux`, Flux mimarisi için tasarlanmış gelişmiş bir metin kodlama düğümüdür. İki ayrı metin girdisini farklı kodlayıcılar (CLIP-L ve T5XXL) aracılığıyla işler ve bunları bir yönlendirme ölçeği ile birleştirerek görüntü üretimi için birleşik bir koşullandırma çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Flux mimarisini destekleyen, hem CLIP-L hem de T5XXL kodlayıcılarını içeren bir CLIP modeli. | CLIP | Evet | - |
| `clip_l` | CLIP-L kodlayıcı tarafından işlenen metin girdisi. Stil veya tema gibi kısa anahtar kelime açıklamaları için uygundur. Çok satırlı girdi ve dinamik istemleri destekler. | STRING | Evet | - |
| `t5xxl` | T5XXL kodlayıcı tarafından işlenen metin girdisi. Karmaşık sahneleri ve detayları ifade eden ayrıntılı doğal dil açıklamaları için uygundur. Çok satırlı girdi ve dinamik istemleri destekler. | STRING | Evet | - |
| `rehberlik` | Metin koşullarının üretim süreci üzerindeki etkisini kontrol eder. Daha yüksek değerler, metne daha sıkı bağlılık anlamına gelir. Varsayılan: 3.5. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Her iki kodlayıcıdan gelen birleştirilmiş gömme vektörlerini ve yönlendirme parametresini içerir. Koşullu görüntü üretimi için kullanılır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/tr.md)

---
**Source fingerprint (SHA-256):** `f168610123410a44f9c5c5c18773603bd47bc7b44b21e65910a6026f86d7eb04`
