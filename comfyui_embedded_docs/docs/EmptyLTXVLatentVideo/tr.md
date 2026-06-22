# BoşLTXVGizliVideo

EmptyLTXVLatentVideo düğümü, video işleme için boş bir latent tensör oluşturur. Belirtilen boyutlarda boş bir başlangıç noktası üretir ve bu, video oluşturma iş akışlarında girdi olarak kullanılabilir. Düğüm, yapılandırılmış genişlik, yükseklik, uzunluk ve yığın boyutuyla sıfır dolu bir latent temsil oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent video tensörünün genişliği (varsayılan: 768, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION arası |
| `yükseklik` | Latent video tensörünün yüksekliği (varsayılan: 512, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION arası |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir yığında oluşturulacak latent video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda sıfır değerlerine sahip oluşturulan boş latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`
