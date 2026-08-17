# Boş Hunyuan Görüntü Gizli

The EmptyHunyuanImageLatent düğümü, Hunyuan görüntü üretim modelleriyle kullanılmak üzere belirli boyutlarda boş bir latent tensör oluşturur. İş akışındaki sonraki düğümlerde işlenebilecek boş bir başlangıç noktası üretir. Düğüm, latent uzayın genişliğini, yüksekliğini ve yığın boyutunu belirlemenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `width` | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 to MAX_RESOLUTION |
| `height` | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 to MAX_RESOLUTION |
| `batch_size` | Bir yığın içinde oluşturulacak latent örneklerinin sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | Hunyuan görüntü işleme için belirtilen boyutlarda boş bir latent tensör. Tensör 64 kanala sahiptir ve uzamsal boyutları istenen genişlik ve yüksekliğin otuz ikide biri (1/32)'dir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
