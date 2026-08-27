# Boş Hunyuan Görüntü Gizli

EmptyHunyuanImageLatent düğümü, Hunyuan görüntü üretim modelleri için boş (sıfırlarla doldurulmuş) bir latent alanı oluşturur. Belirtilen genişlik, yükseklik ve parti boyutuyla iş akışındaki sonraki düğümlere aktarılabilen boş bir başlangıç latenti üretir. Latent tensörü 64 kanala sahiptir ve uzamsal boyutları, genişlik ve yüksekliğin her birinin 32'ye bölünmesiyle elde edilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `genişlik` | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 ila MAX_RESOLUTION |
| `yükseklik` | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 ila MAX_RESOLUTION |
| `toplu_işlem_boyutu` | Bir partide oluşturulacak latent örneklerinin sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | 64 kanallı ve yükseklik ÷ 32 x genişlik ÷ 32 boyutlarına sahip, Hunyuan görüntü işleme için hazır boş bir latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
