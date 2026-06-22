# Boş Hunyuan Görüntü Gizli

EmptyHunyuanImageLatent düğümü, Hunyuan görüntü oluşturma modellerinde kullanılmak üzere belirli boyutlarda boş bir latent tensör oluşturur. İş akışındaki sonraki düğümler aracılığıyla işlenebilecek boş bir başlangıç noktası üretir. Bu düğüm, latent uzayın genişliğini, yüksekliğini ve toplu iş boyutunu belirlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 ila MAX_RESOLUTION |
| `yükseklik` | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) | INT | Evet | 64 ila MAX_RESOLUTION |
| `toplu_işlem_boyutu` | Bir toplu işte oluşturulacak latent örnek sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Hunyuan görüntü işleme için belirtilen boyutlarda boş bir latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`
