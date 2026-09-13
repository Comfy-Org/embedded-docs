# ARVideoI2V

Bu düğüm, Causal Forcing veya Self-Forcing kullanan AR (Otoregresif) video modelleri için görüntüden videoya üretim kurulumu hazırlar. Başlangıç görüntüsünü bir VAE ile latent uzaya kodlar ve bunu modelin transformer seçeneklerinde saklar; böylece video örnekleme süreci, gürültü gidermeden önce KV önbelleğini başlatabilir. Aynı metinden videoya model kontrol noktasını kullanır, bu nedenle ayrı bir görüntüden videoya mimarisine gerek yoktur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak AR video modeli. | MODEL | Evet | - |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `başlangıç_görseli` | Oluşturulan videonun ilk karesi olarak hizmet edecek başlangıç görüntüsü. Girdi toplu işindeki yalnızca ilk görüntü kullanılır ve yalnızca RGB kanalları kodlanır. | IMAGE | Evet | - |
| `genişlik` | Oluşturulan video karelerinin genişliği (varsayılan: 832). | INT | Evet | 16 - 8192 (adım: 16) |
| `yükseklik` | Oluşturulan video karelerinin yüksekliği (varsayılan: 480). | INT | Evet | 16 - 8192 (adım: 16) |
| `uzunluk` | Oluşturulan videonun toplam kare sayısı (varsayılan: 81). | INT | Evet | 1 - 1024 (adım: 4) |
| `toplu_boyut` | Tek bir toplu işte oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 - 64 |

Not: Başlangıç görüntüsü, kodlanmadan önce belirtilen `width` ve `height` değerlerine yeniden boyutlandırılır. Latent zamansal boyut `((length - 1) // 4) + 1` olarak hesaplanır; latent uzamsal boyutlar ise `height / 8` ve `width / 8`'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Kodlanmış başlangıç görüntüsünün transformer seçeneklerinde (`ar_config.initial_latent`) saklandığı klonlanmış model; örnekleyici, gürültü gidermeden önce KV önbelleğini başlatmak için bunu kullanır. | MODEL |
| `LATENT` | `[batch_size, 16, lat_t, height // 8, width // 8]` şeklinde sıfırlarla doldurulmuş latent tensör; burada `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/tr.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
