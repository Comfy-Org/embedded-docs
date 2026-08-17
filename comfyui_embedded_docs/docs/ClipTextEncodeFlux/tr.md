# CLIPMetinKodlamaFlux

`CLIPTextEncodeFlux`, Flux mimarisi için tasarlanmış bir metin kodlama düğümüdür. İki ayrı metin girdisini farklı kodlayıcılar olan CLIP-L ve T5XXL aracılığıyla işler ve bunları bir guidance (yönlendirme) ölçeğiyle birleştirerek görüntü üretimi için birleşik bir koşullandırma çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Flux mimarisini destekleyen, hem CLIP-L hem de T5XXL kodlayıcılarını içeren bir CLIP modeli. | CLIP | Evet | - |
| `clip_l` | CLIP-L kodlayıcı tarafından işlenen metin girdisi. Stil veya tema gibi kısa anahtar kelime açıklamaları için uygundur. Çok satırlı girdi ve dinamik promptları destekler. | STRING | Evet | - |
| `t5xxl` | T5XXL kodlayıcı tarafından işlenen metin girdisi. Karmaşık sahneleri ve detayları ifade eden ayrıntılı doğal dil açıklamaları için uygundur. Çok satırlı girdi ve dinamik promptları destekler. | STRING | Evet | - |
| `guidance` | Metin koşullarının üretim süreci üzerindeki etkisini kontrol eder. Daha yüksek değerler, metne daha sıkı bağlılık anlamına gelir. Varsayılan: 3.5. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Her iki kodlayıcıdan gelen birleştirilmiş embedding'leri ve guidance değerini içerir; koşullu görüntü üretimi için kullanılır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/tr.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
