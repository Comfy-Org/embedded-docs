# Boş HiDream-O1 Latent Görüntü

Bu düğüm, HiDream-O1-Image modeli için piksel uzayında boş bir latent görüntü oluşturur. Görüntü oluşturma için başlangıç noktası görevi gören, sıfırlarla dolu boş bir tensör üretir; boyutları `width`, `height` ve `batch_size` girdileriyle tanımlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Latent görüntünün piksel cinsinden genişliği. Varsayılan: 2048. Değer 32'nin katı olmalıdır. Model yaklaşık 4 megapikselde eğitilmiştir; daha düşük çözünürlükler kaliteyi belirgin şekilde düşürebilir. | INT | Evet | 64 ile 4096 arası (adım: 32) |
| `height` | Latent görüntünün piksel cinsinden yüksekliği. Varsayılan: 2048. Değer 32'nin katı olmalıdır. Model yaklaşık 4 megapikselde eğitilmiştir; daha düşük çözünürlükler kaliteyi belirgin şekilde düşürebilir. | INT | Evet | 64 ile 4096 arası (adım: 32) |
| `batch_size` | Tek bir grupta oluşturulacak latent görüntü sayısı. Varsayılan: 1. | INT | Evet | 1 ile 64 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Boş latent görüntüyü temsil eden, (batch_size, 3, height, width) şeklinde sıfırlarla dolu bir tensör. | LATENT |

## Notlar

- HiDream-O1-Image modeli yaklaşık 4 megapikselde eğitilmiştir. Belirgin şekilde daha düşük çözünürlükler kullanmak, görüntü kalitesinin hissedilir derecede azalmasına yol açabilir.
- Eğitimde kullanılan çözünürlükler şunları içerir: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
