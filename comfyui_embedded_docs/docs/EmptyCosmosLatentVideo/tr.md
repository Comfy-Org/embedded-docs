# BoşCosmosGizliVideo

The EmptyCosmosLatentVideo düğümü, belirtilen boyutlarda boş bir latent video tensörü oluşturur. Yapılandırılabilir genişlik, yükseklik, uzunluk ve parti boyutu parametreleriyle video üretim iş akışları için başlangıç noktası olarak kullanılabilen sıfırlarla dolu bir latent temsili üretir. Latent'in uzamsal boyutları 8 kat alt örneklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Latent videonun piksel cinsinden genişliği (varsayılan: 1280, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 704, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Latent videodaki kare sayısı (varsayılan: 121, 8'e bölünebilir olmalıdır) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Bir partide üretilecek latent video sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |

Latent tensörü 16 kanal kullanır. Uzamsal boyutlar, piksel boyutlarına kıyasla 8'e bölünür (height // 8, width // 8) ve kare sayısı ((length - 1) // 8) + 1 latent kareye sıkıştırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfır değerlere sahip üretilen boş latent video tensörü. Şekil: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
