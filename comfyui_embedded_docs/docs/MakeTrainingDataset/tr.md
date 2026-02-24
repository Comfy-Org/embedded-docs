> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/tr.md)

Bu düğüm, görüntüleri ve metni kodlayarak eğitim için veri hazırlar. Bir görüntü listesi ve karşılık gelen bir metin açıklaması listesi alır, ardından görüntüleri gizli temsillere dönüştürmek için bir VAE modeli ve metni koşullandırma verisine dönüştürmek için bir CLIP modeli kullanır. Ortaya çıkan eşleştirilmiş gizli temsiller ve koşullandırma verileri, eğitim iş akışlarında kullanılmaya hazır listeler olarak çıktılanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Yok | Kodlanacak görüntü listesi. |
| `vae` | VAE | Evet | Yok | Görüntüleri gizli temsillere kodlamak için VAE modeli. |
| `clip` | CLIP | Evet | Yok | Metni koşullandırma verisine kodlamak için CLIP modeli. |
| `texts` | STRING | Hayır | Yok | Metin açıklamaları listesi. Uzunluğu n (görüntülerle eşleşen), 1 (tümü için tekrarlanan) olabilir veya atlanabilir (boş dize kullanılır). |

**Parametre Kısıtlamaları:**

* `texts` listesindeki öğe sayısı 0, 1 olmalı veya `images` listesindeki öğe sayısıyla tam olarak eşleşmelidir. 0 ise, tüm görüntüler için boş bir dize kullanılır. 1 ise, o tek metin tüm görüntüler için tekrarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latents` | LATENT | Gizli veri sözlüklerinin listesi. |
| `conditioning` | CONDITIONING | Koşullandırma listelerinin listesi. |
