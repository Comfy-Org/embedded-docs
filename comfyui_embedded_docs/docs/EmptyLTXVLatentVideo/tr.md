> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/tr.md)

EmptyLTXVLatentVideo düğümü, video işleme için boş bir latent tensör oluşturur. Belirtilen boyutlarda, video üretimi iş akışlarında girdi olarak kullanılabilecek boş bir başlangıç noktası oluşturur. Düğüm, yapılandırılan genişlik, yükseklik, uzunluk ve toplu iş boyutu ile sıfır doldurulmuş bir latent temsil üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 64 - MAX_RESOLUTION | Latent video tensörünün genişliği (varsayılan: 768, adım: 32) |
| `height` | INT | Evet | 64 - MAX_RESOLUTION | Latent video tensörünün yüksekliği (varsayılan: 512, adım: 32) |
| `length` | INT | Evet | 1 - MAX_RESOLUTION | Latent videodaki kare sayısı (varsayılan: 97, adım: 8) |
| `batch_size` | INT | Hayır | 1 - 4096 | Toplu işte oluşturulacak latent video sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Belirtilen boyutlarda sıfır değerlerle oluşturulmuş boş latent tensör |