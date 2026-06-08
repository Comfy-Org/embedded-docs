## Genel Bakış

Bu düğüm, piksel uzayında boş bir latent görüntü oluşturur ve özellikle HiDream-O1-Image modeli için tasarlanmıştır. Genişlik, yükseklik ve batch boyutu girdileriyle tanımlanan boyutlarda, görüntü oluşturma için başlangıç noktası görevi gören sıfırlardan oluşan boş bir tensör üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Piksel cinsinden latent görüntünün genişliği (varsayılan: 2048). Model yaklaşık 4 megapikselde eğitilmiştir; daha düşük çözünürlükler dağılım dışına çıkar ve kalite belirgin şekilde düşer. | INT | Evet | 64 ila 4096 (adım: 32) |
| `yükseklik` | Piksel cinsinden latent görüntünün yüksekliği (varsayılan: 2048). Model yaklaşık 4 megapikselde eğitilmiştir; daha düşük çözünürlükler dağılım dışına çıkar ve kalite belirgin şekilde düşer. | INT | Evet | 64 ila 4096 (adım: 32) |
| `batch_size` | Tek bir batch'te oluşturulacak latent görüntü sayısı (varsayılan: 1). | INT | Hayır | 1 ila 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | (batch_size, 3, height, width) şeklinde, boş latent görüntüyü temsil eden sıfırlarla dolu bir tensör. | LATENT |

{heading_notes}

- HiDream-O1-Image modeli yaklaşık 4 megapikselde eğitilmiştir. Önemli ölçüde daha düşük çözünürlükler kullanmak, görüntü kalitesinin düşmesine neden olabilir.
- Eğitilmiş çözünürlükler şunları içerir: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `fca32bbeddf120b4a7f9a9b88814f5345db133b35252c4d86079397be350c15e`
