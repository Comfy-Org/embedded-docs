# VAE Kod Çözme (Döşemeli)

VAEDecodeTiled düğümü, büyük görüntüleri verimli bir şekilde işlemek için döşemeli bir yaklaşım kullanarak latent temsilleri görüntülere çözer. Bellek kullanımını yönetirken görüntü kalitesini korumak için girdiyi daha küçük döşemeler halinde işler. Düğüm ayrıca, yumuşak geçişler için zamansal kareleri örtüşmeli parçalar halinde işleyerek video VAE'lerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Görüntülere çözülecek latent temsil | LATENT | Evet | - |
| `vae` | Latent örnekleri çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `döşeme_boyutu` | İşleme için her döşemenin boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 32) |
| `örtüşme` | Bitişik döşemeler arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `zamansal_boyut` | Yalnızca video VAE'leri için kullanılır: Bir seferde çözülecek kare miktarı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `zamansal_örtüşme` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare miktarı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** `tile_size`, `overlap`, `temporal_size` ve `temporal_overlap` girdileri gelişmiş ayarlar olarak işaretlenmiştir.

**Not:** Düğüm, pratik sınırları aşmaları durumunda örtüşme değerlerini otomatik olarak ayarlar. Eğer `tile_size`, `overlap` değerinin 4 katından küçükse, örtüşme döşeme boyutunun dörtte birine düşürülür. Benzer şekilde, eğer `temporal_size`, `temporal_overlap` değerinin iki katından küçükse, zamansal örtüşme yarıya indirilir. Düğüm ayrıca hem uzamsal hem de zamansal boyutlar için döşeme ve örtüşme boyutlarını hesaplarken VAE'nin dahili sıkıştırma oranlarını dikkate alır. Girdi latent iç içe bir latent toplu işiyse, toplu işteki yalnızca ilk öğe çözülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Latent temsilden oluşturulan çözülmüş görüntü veya görüntüler. Video latentleri çözülürken çıktı, bir görüntü kareleri dizisidir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
