# SV3D_Koşullandırma

SV3D_Conditioning, SV3D modelini kullanarak 3D video oluşturma için koşullandırma verilerini hazırlar. Bir başlangıç görüntüsü alır ve bunu CLIP vision ile VAE kodlayıcılarından geçirerek pozitif ve negatif koşullandırma ile birlikte bir latent temsil oluşturur. Düğüm, belirtilen video kare sayısına göre çok kareli video oluşturma için kamera yükselti ve azimut dizileri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_vision` | Girdi görüntüsünü kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `init_image` | 3D video oluşturma için başlangıç noktası olarak hizmet eden başlangıç görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Oluşturulan video kareleri için çıktı genişliği (varsayılan: 576, adım: 8) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Oluşturulan video kareleri için çıktı yüksekliği (varsayılan: 576, adım: 8) | INT | Evet | 16 to MAX_RESOLUTION |
| `video_frames` | Video dizisi için oluşturulacak kare sayısı (varsayılan: 21) | INT | Evet | 1 ile 4096 |
| `elevation` | 3D görünüm için kamera yükselti açısı, derece cinsinden (varsayılan: 0.0, adım: 0.1) | FLOAT | Evet | -90.0 ile 90.0 |

Not: Kamera azimutu 0 dereceden başlar ve her karede sabit bir miktar artarak kamera, oluşturulan kareler boyunca nesnenin etrafında tam 360 derecelik bir yörünge tamamlar. Kare başına artış, 360'ın (`video_frames` - 1) değerine bölünmesiyle hesaplanır; yalnızca bir kare istendiğinde minimum bölen 2 kullanılır. `elevation` değeri her kare için sabit kalır.

`init_image`, VAE kodlamasından önce belirtilen `width` ve `height` değerlerine ölçeklenir ve döndürülen latent, `video_frames` x 4 x (`height` // 8) x (`width` // 8) boyutlarını kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Oluşturma için görüntü gömlemleri ve kamera parametrelerini içeren pozitif koşullandırma verisi | CONDITIONING |
| `negative` | Karşıtsal oluşturma için sıfırlanmış gömlemler ve latentler içeren negatif koşullandırma verisi | CONDITIONING |
| `latent` | Belirtilen video kareleri ve çözünürlükle eşleşen boyutlara sahip boş bir latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
