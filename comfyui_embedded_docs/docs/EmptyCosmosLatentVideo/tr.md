> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/tr.md)

EmptyCosmosLatentVideo düğümü, belirtilen boyutlarda boş bir gizli video tensörü oluşturur. Video üretimi iş akışları için bir başlangıç noktası olarak kullanılabilecek, sıfırlarla doldurulmuş bir gizli temsil oluşturur ve yapılandırılabilir genişlik, yükseklik, uzunluk ve toplu iş boyutu parametrelerine sahiptir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `genişlik` | INT | Evet | 16'dan MAX_RESOLUTION'a | Gizli videonun piksel cinsinden genişliği (varsayılan: 1280, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16'dan MAX_RESOLUTION'a | Gizli videonun piksel cinsinden yüksekliği (varsayılan: 704, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 1'den MAX_RESOLUTION'a | Gizli videodaki kare sayısı (varsayılan: 121) |
| `toplu_boyut` | INT | Hayır | 1'den 4096'ya | Toplu işte oluşturulacak gizli video sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Sıfır değerlerle oluşturulan boş gizli video tensörü |