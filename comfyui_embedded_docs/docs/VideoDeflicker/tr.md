# Video Deflicker

İşlenmiş bir videodan zamansal titremeyi kaldırır, böylece her kare kendi detayını korurken komşularının hareketini takip eder. Büyütüldükten veya kare kare işlendikten sonra titreşen görüntüler için tasarlanmıştır: optik akış modelini ve titreyen kareleri ve isteğe bağlı olarak kaynağın kararlı bir kopyasını kılavuz olarak bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `optical_flow` | Load Optical Flow Model düğümünden optik akış modeli (torchvision RAFT-large). | OPTICAL_FLOW | Evet | - |
| `images` | Sabitlenecek titreyen kareler, örneğin büyütülmüş veya kare kare işlenmiş bir video. | IMAGE | Evet | - |
| `guide` | Hareketini takip etmek için kararlı kaynak kareleri, herhangi bir çözünürlükte. Varsayılan olarak `images`'dır, bu daha az titreme kaldırır. Hareket telafisinden sonraki ardışık kılavuz kareleri arasındaki farklar da yumuşatma ağırlığını etkiler: kılavuz, akışın açıklayamadığı biçimde değişiyorsa hareket tahmini doğru olsa bile yumuşatma azalır. | IMAGE | Hayır | - |
| `strength` | Her karenin komşularını ne kadar güçlü takip ettiği (varsayılan: 1.0). Daha yüksek değerler daha fazla titreme kaldırır ve daha fazla ince detayı yumuşatır; 0, kareleri değiştirmeden döndürür. | FLOAT | Evet | 0.0 ile 100.0 arası (adım: 0.1) |
| `direction` | Geçişin yönü. `bidirectional` ileri ve geri geçişin ortalamasını alır, bu hareketin gerisinde kalmayı önler; `forward` tek bir geçiş çalıştırır. (varsayılan: `bidirectional`) | COMBO | Evet | `"bidirectional"`<br>`"forward"` |
| `threshold` | Bir kare ile hareketi telafi edilmiş komşusu arasındaki bu değerden büyük değişiklikler gerçek olarak kabul edilir ve daha az yumuşatılır (varsayılan: 0.1). 0, her değişikliği aynı şekilde yumuşatır. | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

**Notlar:**

- Optik akış kılavuzun küçültülmüş bir kopyası üzerinde hesaplanır, bu yüzden `images` ile aynı boyutta olması gerekmez; kılavuzun pikselleri çıktıya karışmaz.
- `images` ile `guide` arasından kısa olanın ötesindeki kareler işlenmez. `guide` daha kısaysa kalan kareler değişmeden döner.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Titremesi giderilmiş kareler, `images` ile aynı boyut ve kare sayısına sahip. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/tr.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`
