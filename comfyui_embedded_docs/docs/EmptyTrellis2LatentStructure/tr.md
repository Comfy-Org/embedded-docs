# EmptyTrellis2LatentStructure

Bu düğüm, Trellis2 modeli için tüm değerleri sıfıra ayarlanmış boş bir latent yapı oluşturur. Belirtilen batch boyutuna göre, 32 kanallı ve 16×16×16 çözünürlüğünde boş bir 3B latent tensör üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | Batch içindeki latent görüntü sayısı (varsayılan: 1). | INT | Evet | 1 to 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | Boş bir Trellis2 latent yapısı. Örnekler, (batch_size, 32, 16, 16, 16) şeklinde sıfırlarla doldurulmuş bir tensördür ve latent türü "trellis2" olarak ayarlanmıştır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/tr.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
