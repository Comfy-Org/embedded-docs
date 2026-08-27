# Boş HunyuanVideo 1.5 Latent

Bu düğüm, HunyuanVideo 1.5 modeliyle kullanım için özel olarak biçimlendirilmiş boş bir latent tensör oluşturur. Modelin latent uzayı için doğru kanal sayısı ve uzamsal boyutlarla sıfırlardan oluşan bir tensör tahsis ederek video üretimi için boş bir başlangıç noktası oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Video karesinin piksel cinsinden genişliği. | INT | Evet | - |
| `yükseklik` | Video karesinin piksel cinsinden yüksekliği. | INT | Evet | - |
| `uzunluk` | Video dizisindeki kare sayısı. | INT | Evet | - |
| `toplu_boyut` | Bir yığında oluşturulacak video örneklerinin sayısı (varsayılan: 1). | INT | Hayır | - |

**Not:** Oluşturulan latent tensörün uzamsal boyutları, girdi `width` ve `height` değerlerinin 16'ya bölünmesiyle hesaplanır. Zamansal boyut (kareler) `((length - 1) // 4) + 1` olarak hesaplanır. Bu hesaplamalar tam sayı bölmesi kullanır, bu nedenle kırpılmayı önlemek için `width` ve `height` değerleri 16'nın katı olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | HunyuanVideo 1.5 modeli için uygun boyutlara sahip boş bir latent tensör. Tensör `[batch_size, 32, frames, height//16, width//16]` şeklindedir. Çıktı ayrıca 16 değerinde bir `downscale_ratio_spacial` değeri içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/tr.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
