# BoşCosmosGizliVideo

EmptyCosmosLatentVideo düğümü, belirtilen boyutlarda boş bir latent video tensörü oluşturur. Sıfırlarla doldurulmuş bir latent temsil üretir; bu temsil, yapılandırılabilir genişlik, yükseklik, uzunluk ve toplu iş boyutu parametreleriyle video oluşturma iş akışları için başlangıç noktası olarak kullanılabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent videonun piksel cinsinden genişliği (varsayılan: 1280, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 704, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 121, 8'e bölünebilir olmalıdır) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir toplu işte oluşturulacak latent video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfır değerlerine sahip oluşturulan boş latent video tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `f473820af3faf7cb6992ff1959089801e333df395b4007abeb9b504962bfc73b`
