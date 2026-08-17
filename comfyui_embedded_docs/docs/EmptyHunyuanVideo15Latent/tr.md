# Boş HunyuanVideo 1.5 Latent

Bu düğüm, HunyuanVideo 1.5 modeliyle kullanılmak üzere özel olarak biçimlendirilmiş boş bir latent tensör oluşturur. Modelin latent uzayı için doğru kanal sayısına ve uzamsal boyutlara sahip sıfırlardan oluşan bir tensör tahsis ederek video üretimi için boş bir başlangıç noktası üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Video karesinin piksel cinsinden genişliği. | INT | Evet | - |
| `height` | Video karesinin piksel cinsinden yüksekliği. | INT | Evet | - |
| `length` | Video dizisindeki kare sayısı. | INT | Evet | - |
| `batch_size` | Bir batch içinde oluşturulacak video örneği sayısı (varsayılan: 1). | INT | Hayır | - |

**Not:** Oluşturulan latent tensörün uzamsal boyutları, girdi `width` ve `height` değerlerinin 16'ya bölünmesiyle hesaplanır. Zamansal boyut (kare sayısı) ise `((length - 1) // 4) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | HunyuanVideo 1.5 modeli için uygun boyutlara sahip boş bir latent tensör. Tensör, `[batch_size, 32, frames, height//16, width//16]` şeklinde bir boyuta sahiptir. Çıktı ayrıca 16 değerinde bir `downscale_ratio_spacial` içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/tr.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
