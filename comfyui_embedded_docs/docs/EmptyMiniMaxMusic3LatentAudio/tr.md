# EmptyMiniMaxMusic3LatentAudio

Bu düğüm, MiniMax Music3 modeli için boş (sıfırlarla doldurulmuş) bir ses latent tensörü oluşturur. İstenen süreyi saniye cinsinden karşılık gelen ses çerçevelerine dönüştürür ve doğru boyutta boş bir latent tensör üretir; bu tensör, müzik üretimi için başlangıç noktası olarak kullanılmaya hazırdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Ses latent süresi (saniye cinsinden; varsayılan: 120.0). Değer, ses çerçevelerine dönüştürülür ve modelin desteklediği süre sınırlarına kırpılır. | FLOAT | Evet | 0.04 to (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `batch_size` | Bir batch içinde oluşturulacak ses latent sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 |

Not: `seconds` değeri en yakın ses çerçevesine yuvarlanır ve minimum 1 çerçeve ile maksimum `MAX_AUDIO_FRAMES` çerçeve arasında sınırlanır; bu nedenle gerçek latent uzunluğu, girilen tam değerden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | Şekli (batch_size, 128, latent_length) olan sıfırlarla doldurulmuş bir ses latent tensörü. Örneği, 512 zamansal alt örnekleme oranıyla ses verisi olarak işaretleyen meta veriler içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
