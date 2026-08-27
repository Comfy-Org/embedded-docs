# HiDream-O1 Yama Dikiş Yumuşatma

Bu düğüm, HiDream-O1 modeli tarafından üretilen görüntülerde görünür dikiş izlerini azaltır. Bunu, örnekleme sürecinin sonraki bölümünde modelin çıktısını birden çok kaydırılmış doku parçası ızgarası konumunda ortalamayı alarak yapar. Modeli, görüntü hizalamasında küçük farklarla birkaç kez çalıştırır ve sonuçları birbirine karıştırarak doku parçası sınırlarında oluşabilecek ızgara benzeri yapaylıkların giderilmesine yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikiş yumuşatma uygulanacak HiDream-O1 modeli. | MODEL | Evet | - |
| `başlangıç_yüzdesi` | Yumuşatma etkisinin devreye girdiği örnekleme ilerlemesi (0=başlangıç, 1=bitiş) (varsayılan: 0.8). | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `bitiş_yüzdesi` | Yumuşatma etkisinin kapandığı örnekleme ilerlemesi (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `desen` | Kaydırılmış ızgara konumlarının düzeni. `single_shift`: doğal doku parçası ızgarasında bir geçiş ve diğerleri ofsetli. `symmetric`: tüm geçişler ızgaranın dışındadır; kaydırmalar orijin çevresinde bölünmüştür (varsayılan: `"single_shift"`). | COMBO | Evet | `"single_shift"`<br>`"symmetric"` |
| `geçişler` | Kapılı adım başına düşen geçiş sayısı (model çalıştırma sayısı). `2` ve `4` sabit sayılardır. `ramp_2_4` ve `ramp_2_4_8`, örnekleme sona yaklaştıkça geçiş sayısını artırarak dikiş izlerinin en görünür olduğu yerlerde daha fazla yumuşatma sağlar (varsayılan: `"2"`). | COMBO | Evet | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `karıştırma` | Her geçişten elde edilen sonuçların birleştirilmesinde kullanılan yöntem. `average`: tüm geçişlerin eşit ağırlıklı ortalaması. `window`: her geçişin merkezine daha fazla ağırlık veren bir Hann penceresi kullanarak sınır yapaylıklarını azaltır. `median`: piksel başına medyanı alır; bu, sarmadan kaynaklanan aykırı geçişleri eleyebilir (varsayılan: `"average"`). | COMBO | Evet | `"average"`<br>`"window"`<br>`"median"` |
| `güç` | Orijinal model çıktısı (0.0) ile tamamen yumuşatılmış sonuç (1.0) arasındaki enterpolasyonu kontrol eder (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

**Parametre Kısıtlamalarına İlişkin Not:**

- `strength` 0.0 veya daha küçükse ya da `end_percent`, `start_percent` değerine eşit veya daha küçükse yumuşatma etkisi uygulanmaz. Bu durumlarda düğüm modeli değiştirilmeden döndürür.
- `passes` parametresinin rampa seçenekleri (`ramp_2_4`, `ramp_2_4_8`) yalnızca `start_percent` ve `end_percent` bir aralık tanımladığında anlamlıdır; çünkü bu aralıkta örnekleme ilerledikçe geçiş sayısı artar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Dikiş yumuşatma sarmalayıcısı uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/tr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
