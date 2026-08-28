# BoşCosmosGizliVideo

EmptyCosmosLatentVideo, belirtilen boyutlara sahip boş bir latent video tensörü oluşturur. Video üretimi iş akışları için başlangıç noktası olarak kullanılabilen, genişlik, yükseklik, uzunluk ve toplu iş boyutu parametreleri yapılandırılabilir, sıfırlarla doldurulmuş bir latent temsili üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `genişlik` | Latent videonun piksel cinsinden genişliği (varsayılan: 1280, 16'şar artışlarla) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Latent videonun piksel cinsinden yüksekliği (varsayılan: 704, 16'şar artışlarla) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `uzunluk` | Latent videodaki kare sayısı (varsayılan: 121, 8'er artışlarla) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir toplu işte oluşturulacak latent video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 arası |

Not: Latent tensör, hem yükseklik hem de genişlikte 8 kat uzamsal olarak alt örneklenir ve 16 kanal içerir. Latent zamansal kare sayısı `((length - 1) // 8) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `samples` | Sıfır değerlerle oluşturulmuş boş latent video tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
