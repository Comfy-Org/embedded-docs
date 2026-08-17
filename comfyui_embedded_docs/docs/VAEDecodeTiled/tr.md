# VAE Kod Çözme (Döşemeli)

The VAEDecodeTiled node, büyük görüntüleri verimli bir şekilde işlemek için döşemeli bir yaklaşım kullanarak gizli temsilleri görüntülere dönüştürür. Girdiyi daha küçük döşemeler halinde işleyerek bellek kullanımını yönetir ve görüntü kalitesini korur. Düğüm ayrıca video VAE'lerini de destekler; zamansal kareleri, yumuşak geçişler için örtüşmeli parçalar halinde işler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Görüntülere dönüştürülecek gizli temsil | LATENT | Evet | - |
| `vae` | Gizli örnekleri çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `tile_size` | İşleme için her bir döşemenin boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 32) |
| `overlap` | Bitişik döşemeler arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `temporal_size` | Yalnızca video VAE'lerinde kullanılır: Bir seferde çözülecek kare sayısı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `temporal_overlap` | Yalnızca video VAE'lerinde kullanılır: Örtüştürülecek kare sayısı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** Düğüm, örtüşme değerleri pratik sınırları aşarsa bunları otomatik olarak ayarlar. `tile_size`, `overlap` değerinin 4 katından azsa, örtüşme döşeme boyutunun dörtte birine düşürülür. Benzer şekilde, `temporal_size`, `temporal_overlap` değerinin iki katından azsa, zamansal örtüşme yarıya indirilir. Düğüm ayrıca hem uzamsal hem de zamansal boyutlar için döşeme ve örtüşme boyutlarını hesaplarken VAE'nin iç sıkıştırma oranlarını da dikkate alır. Zamansal sıkıştırması olmayan VAE'lerde (video olmayan VAE'ler), `temporal_size` ve `temporal_overlap` parametreleri yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Gizli temsilden üretilen çözülmüş görüntü veya görüntüler. Video gizli temsilleri çözülürken, çözülen tüm kareler tek bir görüntü listesinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
