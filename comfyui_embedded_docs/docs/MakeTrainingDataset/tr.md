> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/tr.md)

Bu düğüm, görüntüleri ve metinleri kodlayarak eğitim için veri hazırlar. Bir görüntü listesi ve buna karşılık gelen bir metin açıklaması listesi alır, ardından görüntüleri gizil temsillere dönüştürmek için bir VAE modeli ve metni koşullandırma verisine dönüştürmek için bir CLIP modeli kullanır. Ortaya çıkan eşleştirilmiş gizil temsiller ve koşullandırmalar, eğitim iş akışlarında kullanıma hazır listeler olarak çıktılanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Yok | Kodlanacak görüntü listesi. |
| `vae` | VAE | Evet | Yok | Görüntüleri gizil temsillere kodlamak için VAE modeli. |
| `clip` | CLIP | Evet | Yok | Metni koşullandırmaya kodlamak için CLIP modeli. |
| `texts` | STRING | Hayır | Yok | Metin açıklamaları listesi. Uzunluğu n (görüntülerle eşleşen), 1 (tümü için tekrarlanan) olabilir veya atlanabilir (boş dize kullanılır). |

**Parametre Kısıtlamaları:**

* `texts` listesindeki öğe sayısı 0, 1 veya `images` listesindeki öğe sayısıyla tam olarak eşleşmelidir. 0 ise, tüm görüntüler için boş bir dize kullanılır. 1 ise, bu tek metin tüm görüntüler için tekrarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latents` | LATENT | Gizil temsil sözlükleri listesi. |
| `conditioning` | CONDITIONING | Koşullandırma listeleri listesi. |

---
**Source fingerprint (SHA-256):** `95947c03f140f527f3db54d0b0131d956646055542ddb546ae5eaa82e4e8cefa`
