> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/tr.md)

LatentApplyOperation düğümü, belirtilen bir işlemi gizli örnekler üzerine uygular. Girdi olarak gizli verileri ve bir işlemi alır, gizli örnekleri sağlanan işlem kullanılarak işler ve değiştirilmiş gizli verileri döndürür. Bu düğüm, iş akışınızda gizli temsilleri dönüştürmenize veya manipüle etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | - | İşlem tarafından işlenecek gizli örnekler |
| `operation` | LATENT_OPERATION | Evet | - | Gizli örneklere uygulanacak işlem |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | İşlem uygulandıktan sonra değiştirilmiş gizli örnekler |