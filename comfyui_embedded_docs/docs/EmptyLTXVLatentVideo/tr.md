# BoşLTXVGizliVideo

EmptyLTXVLatentVideo düğümü, video işleme için boş bir latent tensör oluşturur. Belirtilen genişlik, yükseklik, uzunluk ve yığın boyutuyla boş bir başlangıç noktası üretir; bu, video oluşturma iş akışları için girdi olarak kullanılabilir. Düğüm, uzamsal boyutları yapılandırılan genişlik ve yükseklikten 32 kat daha küçük olan ve kare sayısı 8 kat sıkıştırılan sıfır dolu bir latent temsili üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent video tensörünün genişliği (varsayılan: 768, adım: 32) | INT | Evet | 64 to MAX_RESOLUTION |
| `yükseklik` | Latent video tensörünün yüksekliği (varsayılan: 512, adım: 32) | INT | Evet | 64 to MAX_RESOLUTION |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Bir yığında oluşturulacak latent video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |

Not: Latent video, girdi boyutlarına kıyasla sıkıştırılır: uzamsal boyutlar (genişlik ve yükseklik) 32'ye bölünür ve kare sayısı (uzunluk) 8'e bölünerek en yakın tam sayıya yuvarlanır. Genişlik, yükseklik ve uzunluk adım değerleri bu bölmelerin tam sayı olmasını sağlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda sıfır değerler içeren, 32 uzamsal küçültme oranıyla birlikte üretilen boş latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
