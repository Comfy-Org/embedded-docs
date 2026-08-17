# HiDream-O1 Yama Dikiş Yumuşatma

Bu node, HiDream-O1 modeli tarafından üretilen görüntülerdeki görünür dikiş izlerini (seam) azaltır. Bunu, örnekleme sürecinin sonraki kısmında modelin çıktısını birden çok kaydırılmış patch-grid konumunda ortalayarak yapar. Modeli, görüntü hizalamaları hafifçe farklı olan birkaç kez çalıştırıp sonuçları harmanlayarak çalışır; bu, patch sınırlarında oluşabilecek ızgara benzeri yapaylıkların (artifact) giderilmesine yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikiş yumuşatma sarmalayıcısının uygulanacağı HiDream-O1 modeli. | MODEL | Evet | - |
| `start_percent` | Harmanlamanın devreye girdiği örnekleme ilerlemesi (0=başlangıç, 1=bitiş) (varsayılan: 0.8). | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |
| `end_percent` | Harmanlamanın kapatıldığı örnekleme ilerlemesi (varsayılan: 1.0). | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |
| `pattern` | Kaydırma düzeni. `single_shift`: doğal patch ızgarasında bir geçiş artı diğerlerinin dengelenmesi. `symmetric`: tüm geçişler ızgaranın dışında, kaydırmalar orijin çevresinde bölünmüş (varsayılan: `"single_shift"`). | COMBO | Evet | `"single_shift"`<br>`"symmetric"` |
| `passes` | Kapılı adım başına geçiş sayısı. `2`/`4` = sabit. `ramp_*`: örnekleme sona yaklaştıkça geçiş sayısı artar (dikişlerin en görünür olduğu yerlerde daha fazla yumuşatma) (varsayılan: `"2"`). | COMBO | Evet | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`: eşit ağırlıklı ortalama. `window`: her geçişi kendi patch sınırlarından uzağa göre önceliklendiren Hann pencereli ağırlıklandırma. `median`: piksel bazında medyan, sarmalayıcı dışı (wraparound) aykırı geçişleri reddeder (varsayılan: `"average"`). | COMBO | Evet | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Doğal ızgara tahmini (0) ile ortalamalanmış sonuç (1) arasındaki enterpolasyon (varsayılan: 1.0). | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |

**Kısıtlamalara ilişkin notlar:**

- `strength` 0.0 veya daha düşükse veya `end_percent`, `start_percent` değerinden küçük veya eşitse yumuşatma efekti uygulanmaz; bu durumlarda düğüm modeli değiştirmeden döndürür.
- `passes` için kademeli (ramp) seçenekleri (`ramp_2_4`, `ramp_2_4_8`), kapılı aralık içinde örnekleme `end_percent` değerine doğru ilerledikçe geçiş sayısını artırır; bu nedenle yalnızca `start_percent` ve `end_percent` boş olmayan bir aralık tanımladığında anlamlıdırlar.
- Ortalamalanmış sonuç, modele yalnızca görüntü kenarlarından uzakta geri harmanlanır: bir maske, her kenar boyunca 32 piksellik şeritte orijinal tahmini (4 piksellik tüy geçişiyle) koruyarak kaydırılmış geçişlerin neden olduğu sarmalayıcı dışı (wraparound) kirlenmesini önler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Patch dikiş yumuşatma sarmalayıcısı uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/tr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
