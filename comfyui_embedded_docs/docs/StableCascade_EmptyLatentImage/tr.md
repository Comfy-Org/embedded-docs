# StabilKaskad_BoşGizliGörüntü

StableCascade_EmptyLatentImage düğümü, Stable Cascade modelleri için boş latent tensörler oluşturur. Girdi çözünürlüğü ve sıkıştırma ayarlarından hesaplanan boyutlarla, biri stage C diğeri stage B için olmak üzere iki ayrı latent temsil üretir. Bu düğüm, Stable Cascade üretim hattı için bir başlangıç noktası sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Çıktı görüntüsünün piksel cinsinden genişliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 - MAX_RESOLUTION |
| `height` | Çıktı görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024, adım: 8) | INT | Evet | 256 - MAX_RESOLUTION |
| `compression` | Stage C için latent boyutlarını belirleyen sıkıştırma faktörü (varsayılan: 42, adım: 1). Bu gelişmiş bir parametredir. | INT | Evet | 4 - 128 |
| `batch_size` | Bir grupta oluşturulacak latent örnek sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

Not: `compression` değeri stage C latent boyutunu kontrol eder: yüksekliği ve genişliği, girdi `height` ve `width` değerlerinin `compression` değerine bölümüdür. Stage B latent her zaman sabit 4 sıkıştırması kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `stage_c` | [batch_size, 16, height//compression, width//compression] boyutlarına sahip stage C latent tensörü | LATENT |
| `stage_b` | [batch_size, 4, height//4, width//4] boyutlarına sahip stage B latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
