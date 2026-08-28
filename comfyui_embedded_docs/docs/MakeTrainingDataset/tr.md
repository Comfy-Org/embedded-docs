# Eğitim Veriseti Oluştur

Bu düğüm, görüntüleri ve metni kodlayarak eğitim için veri hazırlar. Bir görüntü listesi ve buna karşılık gelen bir metin açıklamaları listesi alır; ardından görüntüleri latent gösterimlere dönüştürmek için bir VAE modeli ve metni koşullandırma verisine dönüştürmek için bir CLIP modeli kullanır. Elde edilen eşleştirilmiş latentler ve koşullandırma, eğitim iş akışlarında kullanıma hazır listeler olarak çıktılanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kodlanacak görüntülerin listesi. | IMAGE | Evet | N/A |
| `vae` | Görüntüleri latent'e kodlamak için VAE modeli. | VAE | Evet | N/A |
| `clip` | Metni koşullandırmaya kodlamak için CLIP modeli. | CLIP | Evet | N/A |
| `metinler` | Metin açıklamalarının listesi. Uzunluğu n (görüntülerle eşleşen), 1 (tümü için tekrarlanan) olabilir veya atlanabilir (boş dize kullanılır). | STRING | Hayır | 0, 1 veya n öğe (n = görüntü sayısı) |

**Parametre Kısıtlamaları:**

* `texts` listesindeki öğe sayısı 0, 1 olmalı veya `images` listesindeki öğe sayısıyla tam olarak eşleşmelidir. 0 ise, tüm görüntüler için boş dize kullanılır. 1 ise, bu tek metin tüm görüntüler için tekrarlanır. Başka herhangi bir uzunluk hata verir.
* `latents` ve `conditioning` çıktı listeleri her zaman `images` listesiyle aynı sayıda öğe içerir; böylece her latent, karşılık gelen açıklamasının koşullandırmasıyla eşleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Latent sözlüklerinin listesi. | LATENT |
| `koşullandırma` | Koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
