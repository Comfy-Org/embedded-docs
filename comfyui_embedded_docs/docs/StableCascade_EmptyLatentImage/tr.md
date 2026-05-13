> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/tr.md)

StableCascade_EmptyLatentImage düğümü, Stable Cascade modelleri için boş gizli tensörler oluşturur. Giriş çözünürlüğü ve sıkıştırma ayarlarına bağlı olarak uygun boyutlarda iki ayrı gizli temsil - C aşaması ve B aşaması için birer tane - üretir. Bu düğüm, Stable Cascade oluşturma hattının başlangıç noktasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `genişlik` | INT | Evet | 256 ile MAX_RESOLUTION arası | Çıktı görüntüsünün piksel cinsinden genişliği (varsayılan: 1024, adım: 8) |
| `yükseklik` | INT | Evet | 256 ile MAX_RESOLUTION arası | Çıktı görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024, adım: 8) |
| `sıkıştırma` | INT | Evet | 4 ile 128 arası | C aşaması için gizli boyutları belirleyen sıkıştırma faktörü (varsayılan: 42, adım: 1) |
| `toplu_boyut` | INT | Hayır | 1 ile 4096 arası | Bir grupta oluşturulacak gizli örnek sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `aşama_b` | LATENT | Boyutları [batch_size, 16, height//compression, width//compression] olan C aşaması gizli tensörü |
| `stage_b` | LATENT | Boyutları [batch_size, 4, height//4, width//4] olan B aşaması gizli tensörü |

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
