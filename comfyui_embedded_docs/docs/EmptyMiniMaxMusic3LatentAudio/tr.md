# EmptyMiniMaxMusic3LatentAudio

Bu düğüm, MiniMax Music3 modeli için boş (sıfırlarla doldurulmuş) bir ses latent tensörü oluşturur. İstenen süreyi saniye cinsinden karşılık gelen ses çerçevelerine dönüştürür ve müzik üretimi için başlangıç noktası olarak kullanılmaya hazır, doğru boyutta boş bir latent üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Ses latentinin saniye cinsinden süresi (varsayılan: 120.0). Değer, ses çerçevelerine dönüştürülür ve modelin desteklediği süre sınırlarına kırpılır. | FLOAT | Evet | 0.04 ila model maksimumu (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), adım 0.04 |
| `batch_size` | Tek bir batch'te oluşturulacak ses latentlerinin sayısı (varsayılan: 1). | INT | Evet | 1 ila 4096 |

Not: `seconds` değeri en yakın ses çerçevesine yuvarlanır ve minimum 1 çerçeve, maksimum `MAX_AUDIO_FRAMES` çerçeve olacak şekilde kırpılır; bu nedenle gerçek latent uzunluğu, girilen tam değerden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | (batch_size, 128, latent_length) boyutlarında, sıfırlarla doldurulmuş bir ses latent tensörü. Örneği, zamansal küçültme oranı 512 olan ses verisi olarak işaretleyen meta veri içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
