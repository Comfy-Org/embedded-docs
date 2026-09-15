# Boş MiniMax Music3 Latent Ses

Bu düğüm, MiniMax Music3 modeli için boş (sıfırlarla doldurulmuş) bir ses latenti oluşturur. Saniye cinsinden istenen süreyi karşılık gelen ses çerçevesi sayısına dönüştürür ve müzik üretimi için başlangıç noktası olarak kullanılmaya hazır, doğru boyutta boş bir latent tensörü üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Ses latentinin saniye cinsinden süresi (varsayılan: 120.0). Değer, ses çerçevelerine dönüştürülür ve modelin desteklediği süre sınırlarına sınırlandırılır. | FLOAT | Evet | 0.04 ile (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND) arası, adım 0.04 |
| `batch_size` | Tek bir partide üretilecek ses latenti sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 |

Not: `seconds` değeri en yakın ses çerçevesine yuvarlanır ve en az 1 çerçeve, en fazla `MAX_AUDIO_FRAMES` çerçeve olacak şekilde sınırlandırılır; bu nedenle gerçek latent uzunluğu girilen kesin değerden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | (batch_size, 128, latent_length) şeklinde sıfırlarla doldurulmuş bir ses latent tensörü. Örneği 512 zamansal küçültme oranıyla ses verisi olarak işaretleyen meta verileri içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
