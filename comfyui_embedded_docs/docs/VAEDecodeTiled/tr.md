# VAE Kod Çözme (Döşemeli)

VAEDecodeTiled düğümü, büyük görüntüleri verimli bir şekilde işlemek için döşemeli (tiled) bir yaklaşım kullanarak latent temsilleri görüntülere çözer. Girişi daha küçük parçalar halinde işleyerek görüntü kalitesini korurken bellek kullanımını yönetir. Düğüm ayrıca, yumuşak geçişler için zamansal kareleri örtüşmeli öbekler halinde işleyerek video VAE'lerini de destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Görüntülere çözülecek latent temsil | LATENT | Evet | - |
| `vae` | Latent örnekleri çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `döşeme_boyutu` | İşleme için her bir parçanın boyutu (varsayılan: 512) | INT | Evet | 64-4096 (step: 32) |
| `örtüşme` | Bitişik parçalar arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (step: 32) |
| `zamansal_boyut` | Yalnızca video VAE'leri için kullanılır: Aynı anda çözülecek çerçeve sayısı (varsayılan: 64) | INT | Evet | 8-4096 (step: 4) |
| `zamansal_örtüşme` | Yalnızca video VAE'leri için kullanılır: Örtüşecek çerçeve sayısı (varsayılan: 8) | INT | Evet | 4-4096 (step: 4) |

**Not:** Düğüm, örtüşme değerleri pratik sınırları aşarsa bunları otomatik olarak ayarlar. `tile_size` değeri `overlap` değerinin 4 katından azsa, örtüşme, parça boyutunun dörtte birine düşürülür. Benzer şekilde, `temporal_size` değeri `temporal_overlap` değerinin 2 katından azsa, zamansal örtüşme yarıya indirilir. Düğüm ayrıca hem uzamsal hem de zamansal boyutlar için parça ve örtüşme boyutlarını hesaplarken VAE'nin dahili sıkıştırma oranlarını da hesaba katar. Giriş latenti, iç içe bir latent batch ise, batch içindeki yalnızca ilk öğe çözülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Latent temsilden üretilen çözülmüş görüntü veya görüntüler. Video latentleri çözülürken çıktı, bir dizi görüntü karesidir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
