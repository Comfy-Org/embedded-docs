# ARVideoI2V

## Genel Bakış

Bu düğüm, Causal Forcing veya Self-Forcing kullanan AR (Otoregresif) video modelleri için görüntüden videoya üretim kurulumu hazırlar. Başlangıç görüntüsünü bir VAE ile gizli uzaya kodlar ve modelin transformer seçeneklerinde saklar; böylece video örnekleme süreci, gürültü gidermeden önce KV önbelleğini tohumlayabilir. Aynı metinden videoya model kontrol noktasını kullanır, bu nedenle ayrı bir görüntüden videoya mimarisi gerekmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak AR video modeli. | MODEL | Evet | - |
| `vae` | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `başlangıç_görseli` | Üretilen videonun ilk karesi olarak kullanılacak başlangıç görüntüsü. Girdi kümesindeki yalnızca ilk görüntü kullanılır ve yalnızca RGB kanalları kodlanır. | IMAGE | Evet | - |
| `genişlik` | Üretilen video karelerinin genişliği (varsayılan: 832). | INT | Evet | 16 ile 8192 (step: 16) |
| `yükseklik` | Üretilen video karelerinin yüksekliği (varsayılan: 480). | INT | Evet | 16 ile 8192 (step: 16) |
| `uzunluk` | Üretilen videodaki toplam kare sayısı (varsayılan: 81). | INT | Evet | 1 ile 1024 (step: 4) |
| `toplu_boyut` | Tek bir kümede üretilecek video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ile 64 |

Not: Başlangıç görüntüsü, kodlanmadan önce belirtilen `width` ve `height` değerlerine yeniden boyutlandırılır. Gizli zamansal boyut `((length - 1) // 4) + 1` olarak hesaplanır ve gizli uzamsal boyutlar `height / 8` ve `width / 8` olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Başlangıç görüntüsü kodlanmış ve transformer seçeneklerinde (`ar_config.initial_latent`) saklanmış modelin kopyası. Örnekleyici, gürültü gidermeden önce KV önbelleğini tohumlamak için bunu kullanır. | MODEL |
| `LATENT` | Boyutları `[batch_size, 16, lat_t, height // 8, width // 8]` olan sıfır dolu bir gizli tensör; burada `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/tr.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
