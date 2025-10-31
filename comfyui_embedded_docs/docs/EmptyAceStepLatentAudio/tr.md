> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/tr.md)

EmptyAceStepLatentAudio düğümü, belirtilen süreye sahip boş gizli ses örnekleri oluşturur. Girdi saniyelerine ve ses işleme parametrelerine dayalı olarak hesaplanan uzunlukta, sıfırlarla dolu sessiz ses gizli örneklerinden oluşan bir grup oluşturur. Bu düğüm, gizli temsillere ihtiyaç duyan ses işleme iş akışlarını başlatmak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Hayır | 1.0 - 1000.0 | Sesin saniye cinsinden süresi (varsayılan: 120.0) |
| `batch_size` | INT | Hayır | 1 - 4096 | Grup içindeki gizli görüntülerin sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Sıfırlarla dolu boş gizli ses örneklerini döndürür |