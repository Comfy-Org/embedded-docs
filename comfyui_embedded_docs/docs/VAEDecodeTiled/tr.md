> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/tr.md)

VAEDecodeTiled düğümü, büyük görüntüleri verimli bir şekilde işlemek için karo yaklaşımını kullanarak gizli temsilleri görüntülere dönüştürür. Girdiyi, görüntü kalitesini korurken bellek kullanımını yönetmek için daha küçük karolar halinde işler. Düğüm ayrıca, akıcı geçişler için örtüşmeli parçalar halinde zamansal kareleri işleyerek video VAE'lerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | Görüntülere dönüştürülecek gizli temsil |
| `vae` | VAE | Evet | - | Gizli örnekleri dönüştürmek için kullanılan VAE modeli |
| `döşeme_boyutu` | INT | Evet | 64-4096 (adım: 32) | İşleme için her bir karonun boyutu (varsayılan: 512) |
| `örtüşme` | INT | Evet | 0-4096 (adım: 32) | Bitişik karolar arasındaki örtüşme miktarı (varsayılan: 64) |
| `zamansal_boyut` | INT | Evet | 8-4096 (adım: 4) | Sadece video VAE'leri için kullanılır: Aynı anda dönüştürülecek kare miktarı (varsayılan: 64) |
| `zamansal_örtüşme` | INT | Evet | 4-4096 (adım: 4) | Sadece video VAE'leri için kullanılır: Örtüştürülecek kare miktarı (varsayılan: 8) |

**Not:** Düğüm, örtüşme değerleri pratik sınırları aştığında bunları otomatik olarak ayarlar. Eğer `tile_size`, `overlap` değerinin 4 katından az ise, örtüşme karo boyutunun dörtte birine indirilir. Benzer şekilde, eğer `temporal_size`, `temporal_overlap` değerinin iki katından az ise, zamansal örtüşme yarıya indirilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Gizli temsilden oluşturulan dönüştürülmüş görüntü veya görüntüler |