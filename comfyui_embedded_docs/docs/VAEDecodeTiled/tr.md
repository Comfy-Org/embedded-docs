# VAE Kod Çözme (Döşemeli)

VAEDecodeTiled düğümü, gizli temsilleri (latent representations) görüntülere dönüştürmek için döşemeli (tiled) bir yaklaşım kullanarak büyük görüntüleri verimli bir şekilde işler. Giriş verilerini daha küçük döşemeler halinde işleyerek bellek kullanımını yönetir ve görüntü kalitesini korur. Düğüm ayrıca, geçişlerin yumuşak olması için zamansal kareleri örtüşmeli parçalar halinde işleyerek video VAE'lerini de destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Görüntülere dönüştürülecek gizli temsil | LATENT | Evet | - |
| `vae` | Gizli örnekleri çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `döşeme_boyutu` | İşleme için her bir döşemenin boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 32) |
| `örtüşme` | Bitişik döşemeler arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `zamansal_boyut` | Yalnızca video VAE'leri için kullanılır: Bir seferde çözülecek kare sayısı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `zamansal_örtüşme` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare sayısı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** Düğüm, örtüşme değerleri pratik sınırları aşarsa bunları otomatik olarak ayarlar. `tile_size`, `overlap` değerinin 4 katından küçükse, örtüşme döşeme boyutunun dörtte birine düşürülür. Benzer şekilde, `temporal_size`, `temporal_overlap` değerinin iki katından küçükse, zamansal örtüşme yarıya indirilir. Düğüm ayrıca, hem uzamsal hem de zamansal boyutlar için döşeme ve örtüşme boyutlarını hesaplarken VAE'nin dahili sıkıştırma oranlarını da dikkate alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Gizli temsilden oluşturulan çözülmüş görüntü veya görüntüler | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `193d5cb219d66855ae581d3e4488b7b6ae3a45b735fb0f9f784fea1f5d466e46`
