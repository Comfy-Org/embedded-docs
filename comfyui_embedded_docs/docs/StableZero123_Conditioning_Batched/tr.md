> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/tr.md)

StableZero123_Conditioning_Batched düğümü, bir giriş görüntüsünü işler ve 3B model oluşturma için koşullandırma verileri üretir. Görüntüyü CLIP vision ve VAE modellerini kullanarak kodlar, ardından yükseklik ve azimut açılarına dayalı kamera yerleştirmeleri oluşturarak toplu işleme için pozitif ve negatif koşullandırmanın yanı sıra gizli temsiller üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Giriş görüntüsünü kodlamak için kullanılan CLIP vision modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | İşlenecek ve kodlanacak olan başlangıç giriş görüntüsü |
| `vae` | VAE | Evet | - | Görüntü piksellerini gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | İşlenen görüntü için çıkış genişliği (varsayılan: 256, 8'e bölünebilir olmalı) |
| `yükseklik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | İşlenen görüntü için çıkış yüksekliği (varsayılan: 256, 8'e bölünebilir olmalı) |
| `toplu_boyut` | INT | Hayır | 1'den 4096'ya | Toplu işte oluşturulacak koşullandırma örneklerinin sayısı (varsayılan: 1) |
| `yükseklik` | FLOAT | Hayır | -180.0 ile 180.0 arası | Başlangıç kamera yükseklik açısı (derece cinsinden, varsayılan: 0.0) |
| `azimut` | FLOAT | Hayır | -180.0 ile 180.0 arası | Başlangıç kamera azimut açısı (derece cinsinden, varsayılan: 0.0) |
| `yükseklik_toplu_artışı` | FLOAT | Hayır | -180.0 ile 180.0 arası | Her toplu iş öğesi için yüksekliği artırma miktarı (varsayılan: 0.0) |
| `azimut_toplu_artışı` | FLOAT | Hayır | -180.0 ile 180.0 arası | Her toplu iş öğesi için azimutu artırma miktarı (varsayılan: 0.0) |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır, çünkü düğüm bu boyutları dahili olarak gizli uzay oluşturma için 8'e böler.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Görüntü yerleştirmelerini ve kamera parametrelerini içeren pozitif koşullandırma verisi |
| `negative` | CONDITIONING | Sıfır başlatılmış yerleştirmeler içeren negatif koşullandırma verisi |
| `latent` | LATENT | Toplu indeksleme bilgisiyle birlikte işlenen görüntünün gizli temsili |