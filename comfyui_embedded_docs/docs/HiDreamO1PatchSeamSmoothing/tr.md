# HiDream-O1 Yama Dikiş Yumuşatma

Bu düğüm, örnekleme sürecinin sonraki kısmında modelin çıktısını birden çok kaydırılmış yama ızgarası konumu boyunca ortalayarak HiDream-O1 modeli tarafından üretilen görüntülerdeki görünür dikişleri azaltır. Modeli hafifçe farklı görüntü hizalamalarıyla birkaç kez çalıştırır ve sonuçları birbiriyle harmanlar; bu, yama sınırlarında ortaya çıkabilen ızgara benzeri yapaylıkların giderilmesine yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikiş yumuşatmanın uygulanacağı model. | MODEL | Evet | - |
| `başlangıç_yüzdesi` | Harmanlamanın AÇILDIĞI örnekleme ilerlemesi (0=başlangıç, 1=bitiş). varsayılan: 0.8 | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `bitiş_yüzdesi` | Harmanlamanın KAPANDIĞI örnekleme ilerlemesi. varsayılan: 1.0 | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `desen` | Kaydırma düzeni. `single_shift`: doğal yama ızgarasında bir geçiş + diğerleri kaydırılmış. `symmetric`: tüm geçişler ızgara dışında, kaydırmalar orijin etrafında bölünür. varsayılan: "single_shift" | COMBO | Evet | `"single_shift"`<br>`"symmetric"` |
| `geçişler` | Etkin adım başına geçiş sayısı. `2`/`4` = sabit. `ramp_*`: örnekleme sona yaklaştıkça geçiş sayısı artar (dikişlerin en görünür olduğu yerlerde daha fazla yumuşatma). varsayılan: "2" | COMBO | Evet | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `karıştırma` | `average`: eşit ağırlıklı ortalama. `window`: her geçişi kendi yama sınırlarından uzakta tercih eden Hann pencereli ağırlıklandırma. `median`: piksel başına medyan, sarmalama kaynaklı aykırı geçişleri reddeder. varsayılan: "average" | COMBO | Evet | `"average"`<br>`"window"`<br>`"median"` |
| `güç` | Doğal ızgara tahmini (0) ile ortalaması alınmış sonuç (1) arasında enterpolasyon. varsayılan: 1.0 | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

**Parametre Kısıtlamalarına İlişkin Not:**
- `strength` 0.0 veya daha azsa ya da `end_percent`, `start_percent` değerinden küçük veya ona eşitse yumuşatma etkisi uygulanmaz. Bu durumlarda düğüm, modeli değiştirilmemiş olarak döndürür.
- `passes` parametresinin rampa seçenekleri (`ramp_2_4`, `ramp_2_4_8`) yalnızca `end_percent`, `start_percent` değerinden büyük olduğunda anlamlıdır; çünkü örnekleme bu aralıkta ilerledikçe geçiş sayısı artar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Dikiş yumuşatma sarmalayıcısı uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/tr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
