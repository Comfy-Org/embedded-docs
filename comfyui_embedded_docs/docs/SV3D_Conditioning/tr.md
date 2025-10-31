> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/tr.md)

SV3D_Conditioning düğümü, SV3D modelini kullanarak 3D video üretimi için koşullandırma verilerini hazırlar. Başlangıç görüntüsünü alır ve CLIP görüntü ve VAE kodlayıcılarından geçirerek pozitif ve negatif koşullandırmanın yanı sıra bir gizli temsil de oluşturur. Düğüm, belirtilen video karesi sayısına dayalı olarak çok kareli video üretimi için kamera yükseklik ve azimut dizileri oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Girdi görüntüsünü kodlamak için kullanılan CLIP görüntü modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | 3D video üretimi için başlangıç noktası olarak hizmet veren ilk görüntü |
| `vae` | VAE | Evet | - | Görüntüyü gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Üretilen video kareleri için çıktı genişliği (varsayılan: 576, 8'e bölünebilir olmalı) |
| `yükseklik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Üretilen video kareleri için çıktı yüksekliği (varsayılan: 576, 8'e bölünebilir olmalı) |
| `video_kareleri` | INT | Hayır | 1'den 4096'ya | Video dizisi için üretilecek kare sayısı (varsayılan: 21) |
| `yükseklik` | FLOAT | Hayır | -90.0 ila 90.0 | 3D görünüm için kamera yükseklik açısı (derece cinsinden, varsayılan: 0.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Görüntü yerleştirmelerini ve üretim için kamera parametrelerini içeren pozitif koşullandırma verisi |
| `gizli` | CONDITIONING | Karşılaştırmalı üretim için sıfırlanmış yerleştirmeler içeren negatif koşullandırma verisi |
| `latent` | LATENT | Belirtilen video kareleri ve çözünürlük ile eşleşen boyutlara sahip boş bir gizli tensör |