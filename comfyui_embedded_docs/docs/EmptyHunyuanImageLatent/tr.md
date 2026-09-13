# Boş Hunyuan Görüntü Gizli

EmptyHunyuanImageLatent düğümü, Hunyuan görüntü oluşturma modelleri için boş, tamamen sıfır bir latent uzayı oluşturur. Verilen genişlik, yükseklik ve toplu iş boyutunu kullanarak boş bir başlangıç latent'i üretir; bu latent daha sonra iş akışındaki aşağı akış düğümlerine aktarılabilir. Latent tensörü 64 kanal içerir ve her uzamsal boyut, karşılık gelen piksel boyutunun 32'ye bölünmesine eşittir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `width` | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 - MAX_RESOLUTION |
| `height` | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 - MAX_RESOLUTION |
| `batch_size` | Bir toplu işlemde oluşturulacak latent örnek sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-------------|-----------|
| `LATENT` | 64 kanala sahip, boyutları yükseklik ÷ 32 ve genişlik ÷ 32 olan, Hunyuan görüntü işleme için hazır boş bir latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
