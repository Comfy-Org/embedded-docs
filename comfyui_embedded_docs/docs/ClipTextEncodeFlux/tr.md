# ClipTextEncodeFlux

`CLIPTextEncodeFlux`, Flux mimarisi için tasarlanmış bir metin kodlama düğümüdür. İki ayrı metin girdisini farklı kodlayıcılar (CLIP-L ve T5XXL) aracılığıyla işler ve bunları bir guidance ölçeğiyle birleştirerek görüntü üretimi için birleşik bir koşullama çıktısı üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Flux mimarisini destekleyen, hem CLIP-L hem de T5XXL kodlayıcılarını içeren bir CLIP modeli. | CLIP | Evet | - |
| `clip_l` | CLIP-L kodlayıcısı tarafından işlenen metin girdisi. Stil veya tema gibi kısa anahtar sözcük açıklamaları için uygundur. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | - |
| `t5xxl` | T5XXL kodlayıcısı tarafından işlenen metin girdisi. Karmaşık sahneleri ve ayrıntıları ifade eden ayrıntılı doğal dil açıklamaları için uygundur. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | - |
| `rehberlik` | Metin koşullarının üretim süreci üzerindeki etkisini kontrol eder. Daha yüksek değerler, metne daha sıkı uyulması anlamına gelir. Varsayılan: 3.5. 0.1'lik artışlarla ayarlanabilir. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Her iki kodlayıcıdan gelen birleştirilmiş gömme vektörlerini ve `guidance` parametresini içerir; koşullu görüntü üretimi için kullanılır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeFlux/tr.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
