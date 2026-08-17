# SV3D_Koşullandırma

SV3D_Conditioning düğümü, SV3D modelini kullanarak 3D video üretimi için koşullandırma verilerini hazırlar. Başlangıç görüntüsünü alır ve CLIP vision ile VAE kodlayıcılarından geçirerek pozitif ve negatif koşullandırma ile birlikte bir latent temsil oluşturur. Düğüm, belirtilen video karesi sayısına göre çok kareli video üretimi için kamera yükseklik ve azimut dizileri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | Girdi görüntüsünü kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `init_image` | 3D video üretimi için başlangıç noktası olarak kullanılan başlangıç görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Üretilen video kareleri için çıktı genişliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION (adım 8) |
| `height` | Üretilen video kareleri için çıktı yüksekliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ile MAX_RESOLUTION (adım 8) |
| `video_frames` | Video dizisi için üretilecek kare sayısı (varsayılan: 21) | INT | Evet | 1 ile 4096 |
| `elevation` | 3D görünüm için kamera yükseklik açısı (derece cinsinden), her kareye uygulanır (varsayılan: 0.0) | FLOAT | Evet | -90.0 ile 90.0 (adım 0.1) |

Not: Kamera azimutu 0 derecede başlar ve her karede 360 / (video_frames - 1) derece artar; böylece kamera dizi boyunca nesnenin çevresinde tam bir tur tamamlar. Aynı `elevation` değeri tüm karelere uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Üretim için görüntü gömmelerini ve kamera parametrelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Karşılaştırmalı üretim için sıfırlanmış gömmelere sahip negatif koşullandırma verileri | CONDITIONING |
| `latent` | Belirtilen video kare sayısı ve çözünürlükle eşleşen boyutlara sahip boş bir latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
