# Eğitim Veriseti Oluştur

Bu düğüm, görüntüleri ve metni kodlayarak eğitim için veri hazırlar. Bir görüntü listesi ve buna karşılık gelen metin altyazıları listesini alır, ardından görüntüleri latent temsillere dönüştürmek için bir VAE modeli ve metni koşullandırma verisine dönüştürmek için bir CLIP modeli kullanır. Ortaya çıkan eşleştirilmiş latentler ve koşullandırma, eğitim iş akışlarında kullanıma hazır listeler olarak çıkarılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kodlanacak görüntülerin listesi. | IMAGE | Evet | N/A |
| `vae` | Görüntüleri latentlere kodlamak için VAE modeli. | VAE | Evet | N/A |
| `clip` | Metni koşullandırmaya kodlamak için CLIP modeli. | CLIP | Evet | N/A |
| `texts` | Metin altyazılarının listesi. Uzunluğu n (görüntülerle eşleşen), 1 (tümü için yinelenen) veya atlanmış (boş dize kullanılır) olabilir. | STRING | Hayır | 0, 1 veya n öğe (n = görüntü sayısı) |

**Parametre Kısıtlamaları:**

* Bu düğüm liste girdileri kullanır: `images` ve `texts` liste olarak işlenir; `vae` ve `clip` ise her biri tek bir model kabul eder (sağlanan listenin ilk öğesi kullanılır).
* `texts` listesindeki öğe sayısı 0, 1 olmalı veya `images` listesindeki öğe sayısıyla tam olarak eşleşmelidir. 0 ise veya atlanırsa, tüm görüntüler için boş bir dize kullanılır. 1 ise, bu tek metin tüm görüntüler için yinelenir. Başka herhangi bir uzunluk hata verir.
* Çıktı `latents` ve `conditioning` listeleri her zaman `images` listesiyle aynı sayıda öğe içerir; böylece her latent, karşılık gelen altyazının koşullandırmasıyla eşleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Latent sözlüklerinin listesi. | LATENT |
| `conditioning` | Koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
