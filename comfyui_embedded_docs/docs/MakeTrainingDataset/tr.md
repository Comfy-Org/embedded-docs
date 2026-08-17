# Eğitim Veriseti Oluştur

Bu düğüm, görüntüleri ve metinleri kodlayarak eğitim için veri hazırlar. Bir görüntü listesi ve buna karşılık gelen bir metin açıklaması listesi alır; ardından görüntüleri latent temsillere dönüştürmek için bir VAE modeli, metni koşullandırma verisine dönüştürmek için ise bir CLIP modeli kullanır. Elde edilen eşleştirilmiş latentler ve koşullandırmalar liste olarak çıktılanır ve eğitim iş akışlarında kullanıma hazır hale getirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kodlanacak görüntülerin listesi. | IMAGE | Evet | N/A |
| `vae` | Görüntüleri latentlere kodlamak için VAE modeli. | VAE | Evet | N/A |
| `clip` | Metni koşullandırmaya kodlamak için CLIP modeli. | CLIP | Evet | N/A |
| `texts` | Metin açıklamalarının listesi. Uzunluğu n (görüntülerle eşleşen), 1 (tümü için tekrarlanan) veya 0 (boş dize kullanılır) olabilir. | STRING | Hayır | N/A |

**Parametre Kısıtlamaları:**

* `texts` listesindeki öğe sayısı 0, 1 veya `images` listesindeki öğe sayısıyla birebir aynı olmalıdır. Sayı 0 ise tüm görüntüler için boş bir dize kullanılır. Sayı 1 ise bu tek metin tüm görüntüler için tekrarlanır. Sayı başka bir değer ise düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Latent sözlüklerinin listesi. | LATENT |
| `conditioning` | Koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
