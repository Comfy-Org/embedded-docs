# GelişmişÖzelÖrnekleyici

SamplerCustomAdvanced düğümü, özel gürültü, yönlendirme ve örnekleme yapılandırmaları kullanarak gelişmiş gizli alan örneklemesi gerçekleştirir. Özelleştirilebilir gürültü üretimi ve sigma çizelgeleri ile yönlendirilmiş bir örnekleme süreci boyunca bir gizli görüntüyü işler ve hem nihai örneklenmiş çıktıyı hem de mevcut olduğunda gürültüden arındırılmış bir sürümünü üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `gürültü` | Örnekleme süreci için ilk gürültü desenini ve tohumu sağlayan gürültü üreteci | NOISE | Evet | - |
| `rehber` | Örnekleme sürecini istenen çıktılara yönlendiren yönlendirme modeli | GUIDER | Evet | - |
| `örnekleyici` | Üretim sırasında gizli alanda nasıl gezinileceğini tanımlayan örnekleme algoritması | SAMPLER | Evet | - |
| `sigmalar` | Örnekleme adımları boyunca gürültü seviyelerini kontrol eden sigma çizelgesi | SIGMAS | Evet | - |
| `gizli_görüntü` | Örnekleme için başlangıç noktası olarak hizmet eden ilk gizli temsil | LATENT | Evet | - |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Örnekleme sürecini tamamladıktan sonraki nihai örneklenmiş gizli temsil | LATENT |
| `denoised_output` | Mevcut olduğunda çıktının gürültüden arındırılmış bir sürümü, aksi takdirde çıktı ile aynı değeri döndürür | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `bf711ecc0684ad04babe5c63a246195f358204d203e836587a90feff742929a3`
