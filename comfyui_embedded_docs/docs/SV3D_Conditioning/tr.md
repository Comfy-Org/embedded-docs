> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

SV3D_Conditioning düğümü, SV3D modelini kullanarak 3D video oluşturma için koşullandırma verilerini hazırlar. Bir başlangıç görüntüsünü alır ve CLIP görüntü ve VAE kodlayıcıları aracılığıyla işleyerek pozitif ve negatif koşullandırma ile birlikte bir gizli temsil oluşturur. Düğüm, belirtilen video karesi sayısına bağlı olarak çok kareli video oluşturma için kamera yükseklik ve azimut dizileri üretir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Giriş görüntüsünü kodlamak için kullanılan CLIP görüntü modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | 3D video oluşturma için başlangıç noktası olarak hizmet eden başlangıç görüntüsü |
| `vae` | VAE | Evet | - | Görüntüyü gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16 ile MAKS_ÇÖZÜNÜRLÜK | Oluşturulan video kareleri için çıktı genişliği (varsayılan: 576, 8'e bölünebilir olmalıdır) |
| `yükseklik` | INT | Hayır | 16 ile MAKS_ÇÖZÜNÜRLÜK | Oluşturulan video kareleri için çıktı yüksekliği (varsayılan: 576, 8'e bölünebilir olmalıdır) |
| `video_kareleri` | INT | Hayır | 1 ile 4096 | Video dizisi için oluşturulacak kare sayısı (varsayılan: 21) |
| `yükseklik` | FLOAT | Hayır | -90.0 ile 90.0 | 3D görünüm için kamera yükseklik açısı (derece cinsinden) (varsayılan: 0.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Oluşturma için görüntü gömmeleri ve kamera parametrelerini içeren pozitif koşullandırma verileri |
| `gizli` | CONDITIONING | Karşılaştırmalı oluşturma için sıfırlanmış gömmelere sahip negatif koşullandırma verileri |
| `latent` | LATENT | Boyutları belirtilen video kareleri ve çözünürlükle eşleşen boş bir gizli tensör |

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
