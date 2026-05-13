> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

StableZero123_Conditioning düğümü, 3B model oluşturma için girdi görüntüsünü ve kamera açılarını işleyerek koşullandırma verileri ve gizli temsiller üretir. Görüntü özelliklerini kodlamak için bir CLIP görüş modeli kullanır, bunları yükseklik ve azimut açılarına dayalı kamera gömme bilgileriyle birleştirir ve aşağı akış 3B oluşturma görevleri için pozitif ve negatif koşullandırmanın yanı sıra bir gizli temsil üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Görüntü özelliklerini kodlamak için kullanılan CLIP görüş modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | İşlenecek ve kodlanacak girdi görüntüsü |
| `vae` | VAE | Evet | - | Pikselleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Evet | 16 - MAX_RESOLUTION | Gizli temsil için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 - MAX_RESOLUTION | Gizli temsil için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) |
| `toplu_boyut` | INT | Evet | 1 - 4096 | Toplu işlemde oluşturulacak örnek sayısı (varsayılan: 1) |
| `yükseklik` | FLOAT | Evet | -180.0 - 180.0 | Derece cinsinden kamera yükseklik açısı (varsayılan: 0.0) |
| `azimut` | FLOAT | Evet | -180.0 - 180.0 | Derece cinsinden kamera azimut açısı (varsayılan: 0.0) |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır çünkü düğüm, gizli temsil boyutlarını oluşturmak için bunları otomatik olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `negatif` | CONDITIONING | Görüntü özellikleri ve kamera gömmelerini birleştiren pozitif koşullandırma verileri |
| `gizli` | CONDITIONING | Sıfır başlatmalı özelliklere sahip negatif koşullandırma verileri |
| `latent` | LATENT | [batch_size, 4, height//8, width//8] boyutlarında gizli temsil |

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
