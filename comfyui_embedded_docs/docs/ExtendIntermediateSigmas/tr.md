> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/tr.md)

ExtendIntermediateSigmas düğümü, mevcut bir sigma değerleri dizisini alır ve bunların arasına ek ara sigma değerleri ekler. Kaç adet ekstra adım ekleneceğini, enterpolasyon için aralık yöntemini ve sigma dizisinde uzatmanın gerçekleşeceği yeri kontrol etmek için isteğe bağlı başlangıç ve bitiş sigma sınırlarını belirlemenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `sigmalar` | SIGMAS | Evet | - | Ara değerlerle genişletilecek giriş sigma dizisi |
| `adımlar` | INT | Evet | 1 ila 100 | Mevcut sigmalar arasına eklenecek ara adım sayısı (varsayılan: 2) |
| `sigma_başlangıcı` | FLOAT | Evet | -1,0 ila 20000,0 | Uzatma için üst sigma sınırı - yalnızca bu değerin altındaki sigmaları genişletir (varsayılan: -1,0, yani sonsuz) |
| `sigma_bitişi` | FLOAT | Evet | 0,0 ila 20000,0 | Uzatma için alt sigma sınırı - yalnızca bu değerin üzerindeki sigmaları genişletir (varsayılan: 12,0) |
| `aralık` | COMBO | Evet | `"linear"`<br>`"cosine"`<br>`"sine"` | Ara sigma değerlerini aralıklandırmak için enterpolasyon yöntemi (varsayılan: "linear") |

**Not:** Düğüm, yalnızca mevcut sigma değerinin `start_at_sigma` değerine eşit veya daha küçük olduğu ve `end_at_sigma` değerine eşit veya daha büyük olduğu mevcut sigma çiftleri arasına ara sigmalar ekler. `start_at_sigma` değeri -1,0 olarak ayarlandığında sonsuz olarak kabul edilir, yani yalnızca `end_at_sigma` alt sınırı geçerlidir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sigmalar` | SIGMAS | Ek ara değerler eklenmiş genişletilmiş sigma dizisi |

---
**Source fingerprint (SHA-256):** `f51ed433fc38365334ff8e4072174dc04982a8a00770d07f544320a6863577c4`
