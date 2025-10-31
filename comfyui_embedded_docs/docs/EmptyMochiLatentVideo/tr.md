> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/tr.md)

EmptyMochiLatentVideo düğümü, belirtilen boyutlarda boş bir gizli video tensörü oluşturur. Video üretimi iş akışlarında başlangıç noktası olarak kullanılabilecek, sıfırlarla doldurulmuş bir gizli temsil oluşturur. Düğüm, gizli video tensörü için genişlik, yükseklik, uzunluk ve toplu işlem boyutunu tanımlamanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `genişlik` | INT | Evet | 16 - MAX_RESOLUTION | Gizli videonun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Evet | 16 - MAX_RESOLUTION | Gizli videonun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Evet | 7 - MAX_RESOLUTION | Gizli videodaki kare sayısı (varsayılan: 25) |
| `toplu_boyut` | INT | Hayır | 1 - 4096 | Toplu işlemde oluşturulacak gizli video sayısı (varsayılan: 1) |

**Not:** Gerçek gizli boyutlar genişlik/8 ve yükseklik/8 olarak hesaplanır ve zamansal boyut ((uzunluk - 1) // 6) + 1 olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Belirtilen boyutlarda, tamamen sıfırlardan oluşan boş bir gizli video tensörü |