StableZero123_Conditioning düğümü, 3B model oluşturma için girdi görüntüsünü ve kamera açılarını işleyerek koşullandırma verileri ve gizli temsiller üretir. Görüntü özelliklerini kodlamak için bir CLIP görüş modeli kullanır, bunları yükseklik ve azimut açılarına dayalı kamera gömme bilgileriyle birleştirir ve aşağı akış 3B oluşturma görevleri için pozitif ve negatif koşullandırmanın yanı sıra bir gizli temsil üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Görüntü özelliklerini kodlamak için kullanılan CLIP görüş modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | İşlenecek ve kodlanacak girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Pikselleri gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Gizli temsil için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Gizli temsil için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `toplu_boyut` | Toplu işlemde oluşturulacak örnek sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `yükseklik` | Derece cinsinden kamera yükseklik açısı (varsayılan: 0.0) | FLOAT | Evet | -180.0 - 180.0 |
| `azimut` | Derece cinsinden kamera azimut açısı (varsayılan: 0.0) | FLOAT | Evet | -180.0 - 180.0 |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır çünkü düğüm, gizli temsil boyutlarını oluşturmak için bunları otomatik olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Görüntü özellikleri ve kamera gömmelerini birleştiren pozitif koşullandırma verileri | CONDITIONING |
| `gizli` | Sıfır başlatmalı özelliklere sahip negatif koşullandırma verileri | CONDITIONING |
| `latent` | [batch_size, 4, height//8, width//8] boyutlarında gizli temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
