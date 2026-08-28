# Boş HiDream-O1 Latent Görüntü

Bu düğüm, özellikle HiDream-O1-Image modeli için tasarlanmış, piksel uzayında boş bir latent görüntü oluşturur. Genişlik, yükseklik ve batch boyutu girdileriyle tanımlanan boyutlara sahip, görüntü üretimi için başlangıç noktası olarak hizmet eden sıfırlardan oluşan boş bir tensör üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Latent görüntünün piksel cinsinden genişliği (varsayılan: 2048). Model yaklaşık 4 megapiksel ile eğitilmiştir; daha düşük çözünürlükler dağılım dışına çıkar ve kalite belirgin şekilde geriler. | INT | Evet | 64 ile 4096 (step: 32) |
| `yükseklik` | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048). Model yaklaşık 4 megapiksel ile eğitilmiştir; daha düşük çözünürlükler dağılım dışına çıkar ve kalite belirgin şekilde geriler. | INT | Evet | 64 ile 4096 (step: 32) |
| `batch_size` | Tek bir batch içinde oluşturulacak latent görüntü sayısı (varsayılan: 1). | INT | Hayır | 1 ile 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş, boş latent görüntüyü temsil eden ve (batch_size, 3, height, width) şekline sahip tensör. | LATENT |

## Notlar

- HiDream-O1-Image modeli yaklaşık 4 megapiksel ile eğitilmiştir. Önemli ölçüde daha düşük çözünürlükler kullanmak, görüntü kalitesinin düşmesine neden olabilir.
- Eğitim çözünürlükleri şunları içerir: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
