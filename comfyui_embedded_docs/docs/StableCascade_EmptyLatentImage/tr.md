# StabilKaskad_BoşGizliGörüntü

The StableCascade_EmptyLatentImage düğümü, Stable Cascade modelleri için boş latent tensörler oluşturur. Giriş çözünürlüğüne ve sıkıştırma ayarlarına bağlı olarak uygun boyutlarda iki ayrı latent gösterimi üretir; biri C aşaması, diğeri B aşaması içindir. Bu düğüm, Stable Cascade üretim hattı için başlangıç noktasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Çıktı görüntüsünün piksel cinsinden genişliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 to MAX_RESOLUTION |
| `yükseklik` | Çıktı görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 to MAX_RESOLUTION |
| `sıkıştırma` | C aşaması için latent boyutlarını belirleyen sıkıştırma faktörü (varsayılan: 42, adım: 1). Bu gelişmiş bir parametredir. | INT | Evet | 4 ile 128 |
| `toplu_boyut` | Bir toplu işte (batch) oluşturulacak latent örneklerinin sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 |

Not: `compression` değeri, C aşaması latent boyutunu kontrol eder; yüksekliği ve genişliği, giriş `height` ve `width` değerlerinin `compression` değerine bölünmesiyle elde edilir. B aşaması latent boyutu her zaman sabit bir 4 sıkıştırma oranı kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `aşama_c` | C aşaması latent tensörü (boyutlar: [batch_size, 16, height//compression, width//compression]) | LATENT |
| `aşama_b` | B aşaması latent tensörü (boyutlar: [batch_size, 4, height//4, width//4]) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
