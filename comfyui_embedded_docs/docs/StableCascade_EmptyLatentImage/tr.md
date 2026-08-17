# StabilKaskad_BoşGizliGörüntü

StableCascade_EmptyLatentImage düğümü, Stable Cascade modelleri için boş latent tensörler oluşturur. Giriş çözünürlüğüne ve sıkıştırma ayarlarına bağlı olarak uygun boyutlarda iki ayrı latent temsil üretir: biri C aşaması, diğeri B aşaması için. Bu düğüm, Stable Cascade üretim hattı için başlangıç noktasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Çıktı görüntüsünün piksel cinsinden genişliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 ila MAX_RESOLUTION |
| `height` | Çıktı görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 ila MAX_RESOLUTION |
| `compression` | C aşaması için latent boyutlarını belirleyen sıkıştırma faktörü (varsayılan: 42, adım: 1). Bu gelişmiş bir parametredir. | INT | Evet | 4 ila 128 |
| `batch_size` | Bir toplu işte (batch) oluşturulacak latent örnek sayısı (varsayılan: 1) | INT | Hayır | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `stage_c` | C aşaması latent tensörü; boyutlar: [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | B aşaması latent tensörü; boyutlar: [batch_size, 4, height//4, width//4] | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
