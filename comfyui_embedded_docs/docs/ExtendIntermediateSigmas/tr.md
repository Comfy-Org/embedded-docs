# AraSigmalarıGenişlet

ExtendIntermediateSigmas düğümü, mevcut bir sigma değerleri dizisini alır ve bunların arasına ek ara sigma değerleri ekler. Kaç ek adım ekleneceğini, interpolasyon için aralıklandırma yöntemini ve sigma dizisi içinde genişletmenin nerede gerçekleşeceğini kontrol eden isteğe bağlı başlangıç ve bitiş sigma sınırlarını belirtmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Ara değerlerle genişletilecek giriş sigma dizisi | SIGMAS | Evet | - |
| `adımlar` | Mevcut sigmaların her bir çifti arasına eklenecek ara sigma değerlerinin sayısını kontrol eder. İki sigma arasındaki aralık `steps` parçaya bölünür ve her çift için `steps - 1` yeni değer üretilir (varsayılan: 2, bu da her çift için bir değer ekler) | INT | Evet | 1 - 100 |
| `sigma_başlangıcı` | Genişletme için üst sigma sınırı. Yalnızca başlangıç sigması bu değerden küçük veya bu değere eşit olan sigma aralıkları genişletilir. -1.0 olarak ayarlandığında sonsuz olarak kabul edilir, yani üst sınır uygulanmaz. Varsayılan: -1.0 | FLOAT | Evet | -1.0 - 20000.0 |
| `sigma_bitişi` | Genişletme için alt sigma sınırı. Yalnızca başlangıç sigması bu değerden büyük veya bu değere eşit olan sigma aralıkları genişletilir. Varsayılan: 12.0 | FLOAT | Evet | 0.0 - 20000.0 |
| `aralık` | Ara sigma değerlerinin aralıklandırılması için interpolasyon yöntemi (varsayılan: "linear") | COMBO | Evet | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Not:** Düğüm, yalnızca başlangıç sigması `start_at_sigma` değerinden küçük veya bu değere eşit ve `end_at_sigma` değerinden büyük veya bu değere eşit olan sigma aralıkları için ara sigmalar ekler. `start_at_sigma` -1.0 olarak ayarlandığında sonsuz olarak kabul edilir, bu nedenle yalnızca `end_at_sigma` alt sınırı geçerli olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Ek ara değerler eklenmiş genişletilmiş sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
