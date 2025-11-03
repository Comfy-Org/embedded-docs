> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/tr.md)

EmptySD3LatentImage düğümü, Stable Diffusion 3 modelleri için özel olarak biçimlendirilmiş boş bir latent görüntü tensörü oluşturur. SD3 iş hatları tarafından beklenen doğru boyutlara ve yapıya sahip, sıfırlarla doldurulmuş bir tensör üretir. Bu genellikle görüntü oluşturma iş akışları için bir başlangıç noktası olarak kullanılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `genişlik` | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) | Çıktı latent görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) |
| `yükseklik` | INT | Evet | 16 - MAX_RESOLUTION (adım: 16) | Çıktı latent görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) |
| `toplu_boyut` | INT | Evet | 1 - 4096 | Bir toplu işte oluşturulacak latent görüntü sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | SD3 uyumlu boyutlara sahip boş örnekler içeren bir latent tensör |