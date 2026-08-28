# AraSigmalarıGenişlet

ExtendIntermediateSigmas düğümü, mevcut bir sigma değerleri dizisini alır ve aralarına ek ara sigma değerleri yerleştirir. Kaç ek adım ekleneceğini, enterpolasyonda kullanılacak aralıklandırma yöntemini ve uzatmanın sigma dizisi içinde nerede gerçekleşeceğini kontrol etmek için isteğe bağlı başlangıç ve bitiş sigma sınırlarını belirlemenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Ara değerlerle genişletilecek giriş sigma dizisi | SIGMAS | Evet | - |
| `adımlar` | Mevcut sigma çiftlerinin her biri arasına eklenen ara sigma değerlerinin sayısını kontrol eder. İki sigma arasındaki aralık `steps` parçaya bölünür ve her çift için `steps - 1` yeni değer üretilir (varsayılan: 2, her çift için bir değer ekler) | INT | Evet | 1 ila 100 |
| `sigma_başlangıcı` | Uzatma için üst sigma sınırı - yalnızca bu değerin altındaki sigmaları genişletir (varsayılan: -1.0, sonsuzluk anlamına gelir) | FLOAT | Evet | -1.0 ila 20000.0 |
| `sigma_bitişi` | Uzatma için alt sigma sınırı - yalnızca bu değerin üzerindeki sigmaları genişletir (varsayılan: 12.0) | FLOAT | Evet | 0.0 ila 20000.0 |
| `aralık` | Ara sigma değerlerini aralıklandırmak için enterpolasyon yöntemi (varsayılan: "linear") | COMBO | Evet | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Not:** Düğüm, ara sigmaları yalnızca mevcut sigma değeri `start_at_sigma` değerinden küçük veya eşit ve `end_at_sigma` değerinden büyük veya eşit olan sigma çiftleri arasına ekler. `start_at_sigma` -1.0 olarak ayarlandığında sonsuzluk olarak kabul edilir; bu durumda yalnızca `end_at_sigma` alt sınırı uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Ek ara değerler eklenmiş genişletilmiş sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
