> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/tr.md)

EmptyFlux2LatentImage düğümü, boş, sıfır dolu bir gizli (latent) temsil oluşturur. Sıfırlarla dolu bir tensör üretir ve bu, Flux modelinin gürültü giderme (denoising) işlemi için bir başlangıç noktası görevi görür. Gizli temsilin boyutları, girdi genişliği ve yüksekliğinin 16 faktörüne bölünmesiyle belirlenir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 16 - 8192 | Oluşturulacak nihai görüntünün genişliği. Gizli temsilin genişliği bu değerin 16'ya bölümü olacaktır. Varsayılan değer 1024'tür. |
| `height` | INT | Evet | 16 - 8192 | Oluşturulacak nihai görüntünün yüksekliği. Gizli temsilin yüksekliği bu değerin 16'ya bölümü olacaktır. Varsayılan değer 1024'tür. |
| `batch_size` | INT | Hayır | 1 - 4096 | Tek bir partide oluşturulacak gizli örnek sayısı. Varsayılan değer 1'dir. |

**Not:** `width` ve `height` girdileri 16'ya tam bölünebilir olmalıdır, çünkü düğüm içsel olarak gizli boyutları oluşturmak için bu değerleri bu faktöre böler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Sıfırlarla dolu bir gizli tensör. Şekli `[batch_size, 128, height // 16, width // 16]` şeklindedir. |
