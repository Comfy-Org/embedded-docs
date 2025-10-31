> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

StableZero123_Conditioning düğümü, bir giriş görüntüsünü ve kamera açılarını işleyerek 3B model oluşturma için koşullandırma verileri ve gizli temsiller üretir. Görüntü özelliklerini kodlamak için bir CLIP görüntü modeli kullanır, bunları yükseklik ve azimut açılarına dayalı kamera gömme bilgileriyle birleştirir ve sonraki 3B oluşturma görevleri için pozitif ve negatif koşullandırmanın yanı sıra bir gizli temsil üretir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Görüntü özelliklerini kodlamak için kullanılan CLIP görüntü modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | İşlenecek ve kodlanacak giriş görüntüsü |
| `vae` | VAE | Evet | - | Pikselleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Gizli temsil için çıkış genişliği (varsayılan: 256, 8'e bölünebilir olmalı) |
| `yükseklik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Gizli temsil için çıkış yüksekliği (varsayılan: 256, 8'e bölünebilir olmalı) |
| `toplu_boyut` | INT | Hayır | 1'den 4096'ya | Toplu işte oluşturulacak örnek sayısı (varsayılan: 1) |
| `yükseklik` | FLOAT | Hayır | -180.0 ile 180.0 arası | Kamera yükseklik açısı (derece cinsinden, varsayılan: 0.0) |
| `azimut` | FLOAT | Hayır | -180.0 ile 180.0 arası | Kamera azimut açısı (derece cinsinden, varsayılan: 0.0) |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır, çünkü düğüm gizli temsil boyutlarını oluşturmak için bunları otomatik olarak 8'e böler.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Görüntü özellikleri ve kamera gömme bilgilerini birleştiren pozitif koşullandırma verisi |
| `negative` | CONDITIONING | Sıfır başlatılmış özelliklere sahip negatif koşullandırma verisi |
| `latent` | LATENT | [batch_size, 4, height//8, width//8] boyutlarına sahip gizli temsil |