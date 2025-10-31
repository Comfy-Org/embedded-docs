> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/tr.md)

EmptyLatentAudio düğümü, ses işleme için boş latent tensörler oluşturur. Belirtilen süre ve batch boyutunda boş bir ses latent temsili üretir ve bu, ses üretimi veya işleme iş akışları için girdi olarak kullanılabilir. Düğüm, ses süresine ve örnekleme hızına dayalı olarak uygun latent boyutlarını hesaplar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Evet | 1.0 - 1000.0 | Saniye cinsinden ses süresi (varsayılan: 47.6) |
| `batch_size` | INT | Evet | 1 - 4096 | Batch içindeki latent görüntülerin sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Belirtilen süre ve batch boyutunda ses işleme için boş bir latent tensör döndürür |