# SV3D_Koşullandırma

SV3D_Conditioning, SV3D modelini kullanarak 3D video üretimi için koşullandırma verilerini hazırlar. Başlangıç görüntüsünü alır ve CLIP vision ile VAE kodlayıcılarından geçirerek pozitif ve negatif koşullandırmanın yanı sıra bir latent temsil oluşturur. Düğüm, belirtilen video karesi sayısına göre çok kareli video üretimi için kamera yükseklik ve azimut dizileri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Giriş görüntüsünü kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | 3D video üretimi için başlangıç noktası olarak hizmet eden başlangıç görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Üretilen video kareleri için çıktı genişliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Üretilen video kareleri için çıktı yüksekliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `video_kareleri` | Video dizisi için üretilecek kare sayısı (varsayılan: 21) | INT | Evet | 1 ila 4096 |
| `yükseklik` | 3D görünüm için kamera yükseklik açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Evet | -90.0 ila 90.0 |

Not: Kamera azimutu 0 dereceden başlar ve her karede sabit bir miktarda artar; böylece kamera, üretilen kareler boyunca nesnenin etrafında tam 360 derecelik bir yörüngeyi tamamlar. `elevation` değeri her kare için sabit kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Üretim için görüntü yerleştirmelerini ve kamera parametrelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negatif` | Karşılaştırmalı üretim için sıfırlanmış yerleştirmeler ve latentler içeren negatif koşullandırma verileri | CONDITIONING |
| `gizli` | Belirtilen video kareleri ve çözünürlükle eşleşen boyutlara sahip boş bir latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
