> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

EmptyHunyuanImageLatent düğümü, Hunyuan görüntü oluşturma modellerinde kullanılmak üzere belirli boyutlarda boş bir latent tensör oluşturur. İş akışındaki sonraki düğümler aracılığıyla işlenebilecek boş bir başlangıç noktası üretir. Bu düğüm, latent uzayın genişliğini, yüksekliğini ve toplu iş boyutunu belirlemenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `genişlik` | INT | Evet | 64 ila MAX_RESOLUTION | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) |
| `yükseklik` | INT | Evet | 64 ila MAX_RESOLUTION | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) |
| `toplu_işlem_boyutu` | INT | Evet | 1 ila 4096 | Bir toplu işte oluşturulacak latent örnek sayısı (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `LATENT` | LATENT | Hunyuan görüntü işleme için belirtilen boyutlarda boş bir latent tensör |

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`
