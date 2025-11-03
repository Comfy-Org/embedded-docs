> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/tr.md)

EmptyChromaRadianceLatentImage düğümü, chroma radiance iş akışlarında kullanılmak üzere belirtilen boyutlarda boş bir latent görüntü oluşturur. Latent uzay işlemleri için bir başlangıç noktası olarak hizmet eden, sıfırlarla doldurulmuş bir tensör üretir. Düğüm, boş latent görüntünün genişlik, yükseklik ve batch boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Latent görüntünün piksel cinsinden genişliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Latent görüntünün piksel cinsinden yüksekliği (varsayılan: 1024, 16'ya bölünebilir olmalıdır) |
| `batch_size` | INT | Hayır | 1 - 4096 | Bir batch içinde oluşturulacak latent görüntü sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Belirtilen boyutlarda oluşturulmuş boş latent görüntü tensörü |