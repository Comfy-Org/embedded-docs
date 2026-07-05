# SV3D_Koşullandırma

SV3D_Conditioning düğümü, SV3D modelini kullanarak 3D video oluşturma için koşullandırma verilerini hazırlar. Bir başlangıç görüntüsünü alır ve CLIP görüntü ve VAE kodlayıcıları aracılığıyla işleyerek pozitif ve negatif koşullandırma ile birlikte bir gizli temsil oluşturur. Düğüm, belirtilen video karesi sayısına bağlı olarak çok kareli video oluşturma için kamera yükseklik ve azimut dizileri üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Giriş görüntüsünü kodlamak için kullanılan CLIP görüntü modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | 3D video oluşturma için başlangıç noktası olarak hizmet eden başlangıç görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Oluşturulan video kareleri için çıktı genişliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Hayır | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `yükseklik` | Oluşturulan video kareleri için çıktı yüksekliği (varsayılan: 576, 8'e bölünebilir olmalıdır) | INT | Hayır | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `video_kareleri` | Video dizisi için oluşturulacak kare sayısı (varsayılan: 21) | INT | Hayır | 1 ile 4096 |
| `yükseklik` | 3D görünüm için kamera yükseklik açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Hayır | -90.0 ile 90.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Oluşturma için görüntü gömmeleri ve kamera parametrelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `gizli` | Karşılaştırmalı oluşturma için sıfırlanmış gömmelere sahip negatif koşullandırma verileri | CONDITIONING |
| `latent` | Boyutları belirtilen video kareleri ve çözünürlükle eşleşen boş bir gizli tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
