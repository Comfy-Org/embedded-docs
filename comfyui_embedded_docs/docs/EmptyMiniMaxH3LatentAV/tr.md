# Empty MiniMax H3 AV Latent

Bu düğüm, MiniMax H3 modeli için hem video hem de ses bilgilerini birleştiren boş bir latent oluşturur. İçeriğin genişliğini, yüksekliğini ve uzunluğunu siz tanımlarsınız; düğüm, modelin üretim için başlangıç noktası olarak kullanabileceği boş bir latent üretir. Süre (uzunluk), modelin 24 fps'de gerektirdiği 17k+5 karelik kare ızgarasına sığacak şekilde otomatik olarak ayarlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `genişlik` | Latentin piksel cinsinden genişliği. Değerler 32'nin katları olmalıdır. Varsayılan: 1344. | INT | Evet | 32 - MAX_RESOLUTION (adım 32) |
| `yükseklik` | Latentin piksel cinsinden yüksekliği. Değerler 32'nin katları olmalıdır. Varsayılan: 768. | INT | Evet | 32 - MAX_RESOLUTION (adım 32) |
| `uzunluk` | 24 fps'deki kare sayısı, modelin 17k+5 ızgarasına yukarı yuvarlanır (124 = ~5 sn; eğitim aralığı ~124-362'dir, daha uzunu test edilmemiştir). Varsayılan: 124. | INT | Evet | 5 - 3600 (adım 17) |

Not: `length` değeri, modelin 17k+5 ızgarasına (17 x k + 5 kare, örneğin 5, 22, 39, 56, 73, 90, 107, 124 vb.) uyan bir sonraki kare sayısına yukarı yuvarlanır. `width` ve `height` değerleri 32'nin katları olmalıdır. Maksimum çözünürlük, ComfyUI'de sistem tarafından tanımlanan değerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latent` | MiniMax H3 için, girdi genişliği, yüksekliği ve uzunluğuna göre boyutlandırılmış, üretilen boş birleşik video+ses latenti. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/tr.md)

---
**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`
