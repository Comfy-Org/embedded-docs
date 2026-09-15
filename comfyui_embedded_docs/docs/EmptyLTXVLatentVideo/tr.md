# BoşLTXVGizliVideo

EmptyLTXVLatentVideo düğümü, belirttiğiniz genişlik, yükseklik, uzunluk ve toplu iş boyutunu kullanarak boş (sıfırlarla doldurulmuş) bir latent video tensörü oluşturur. LTXV video oluşturma iş akışları için boş bir başlangıç noktası sağlar; latent boyutlar istenen video boyutuna göre otomatik olarak sıkıştırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent video tensörünün genişliği (varsayılan: 768, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION arası |
| `yükseklik` | Latent video tensörünün yüksekliği (varsayılan: 512, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION arası |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir toplu işte oluşturulacak latent video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 arası |

Not: Latent video, istenen boyutlara kıyasla sıkıştırılır: uzamsal boyutlar (genişlik ve yükseklik) 32'ye bölünür ve kare sayısı (uzunluk) 8'e bölünüp bir üst tam sayıya yuvarlanır. Genişlik, yükseklik ve uzunluk için adım değerleri bu bölümlerin tam sayı çıkmasına yardımcı olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Belirtilen boyutlarda sıfır değerleri içeren ve 32'lik bir uzamsal küçültme oranına sahip oluşturulmuş boş latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
