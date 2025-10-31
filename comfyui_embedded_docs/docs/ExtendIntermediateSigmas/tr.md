> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/tr.md)

ExtendIntermediateSigmas düğümü, mevcut bir sigma değerleri dizisini alır ve aralarına ek ara sigma değerleri ekler. Kaç tane ek adım ekleneceğini, enterpolasyon için boşluklandırma yöntemini ve sigma dizisi içinde uzatmanın nerede gerçekleşeceğini kontrol etmek için isteğe bağlı başlangıç ve bitiş sigma sınırlarını belirtmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Evet | - | Ara değerlerle genişletilecek giriş sigma dizisi |
| `steps` | INT | Evet | 1-100 | Mevcut sigmalar arasına eklenecek ara adım sayısı (varsayılan: 2) |
| `start_at_sigma` | FLOAT | Evet | -1.0 - 20000.0 | Uzatma için üst sigma sınırı - yalnızca bu değerin altındaki sigmaları genişletir (varsayılan: -1.0, bu sonsuz anlamına gelir) |
| `end_at_sigma` | FLOAT | Evet | 0.0 - 20000.0 | Uzatma için alt sigma sınırı - yalnızca bu değerin üstündeki sigmaları genişletir (varsayılan: 12.0) |
| `spacing` | COMBO | Evet | "linear"<br>"cosine"<br>"sine" | Ara sigma değerlerinin aralıklı yerleştirilmesi için enterpolasyon yöntemi |

**Not:** Düğüm yalnızca, hem mevcut sigma değerinin `start_at_sigma` değerinden küçük veya eşit olduğu hem de `end_at_sigma` değerinden büyük veya eşit olduğu mevcut sigma çiftleri arasına ara sigmalar ekler. `start_at_sigma` -1.0 olarak ayarlandığında, bu sonsuz olarak kabul edilir, yani yalnızca `end_at_sigma` alt sınırı uygulanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Ek ara değerlerin eklendiği genişletilmiş sigma dizisi |