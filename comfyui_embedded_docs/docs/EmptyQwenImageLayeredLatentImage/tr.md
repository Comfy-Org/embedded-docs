> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/tr.md)

Empty Qwen Image Layered Latent düğümü, Qwen görüntü modelleriyle kullanılmak üzere boş, çok katmanlı bir latent temsili oluşturur. Belirtilen katman sayısı, toplu iş boyutu ve uzamsal boyutlarla yapılandırılmış, sıfırlarla dolu bir tensör üretir. Bu boş latent, sonraki görüntü oluşturma veya manipülasyon iş akışları için bir başlangıç noktası görevi görür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16'dan MAX_RESOLUTION'a | Oluşturulacak latent görüntünün genişliği. Değer 16'ya tam bölünebilir olmalıdır. (varsayılan: 640) |
| `height` | INT | Evet | 16'dan MAX_RESOLUTION'a | Oluşturulacak latent görüntünün yüksekliği. Değer 16'ya tam bölünebilir olmalıdır. (varsayılan: 640) |
| `layers` | INT | Evet | 0'dan MAX_RESOLUTION'a | Latent yapıya eklenecek ek katman sayısı. Bu, latent temsilin derinliğini tanımlar. (varsayılan: 3) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Bir toplu işte oluşturulacak latent örnek sayısı. (varsayılan: 1) |

**Not:** `width` ve `height` parametreleri, çıktı latent tensörünün uzamsal boyutlarını belirlemek için dahili olarak 8'e bölünür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Sıfırlarla dolu bir latent tensör. Şekli `[batch_size, 16, layers + 1, height // 8, width // 8]` şeklindedir. |
