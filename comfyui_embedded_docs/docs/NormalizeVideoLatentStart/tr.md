> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

Bu düğüm, bir video gizli temsilinin ilk birkaç karesini, sonra gelen karelere daha çok benzeyecek şekilde ayarlar. Videoda daha sonraki bir dizi referans kareden ortalama ve varyasyonu hesaplar ve aynı özellikleri başlangıç karelerine uygular. Bu, bir videonun başlangıcında daha akıcı ve tutarlı bir görsel geçiş oluşturmaya yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latent` | LATENT | Evet | - | İşlenecek video gizli temsili. |
| `start_frame_count` | INT | Hayır | 1 ila 16384 | Baştan itibaren sayılan, normalleştirilecek gizli kare sayısı (varsayılan: 4). |
| `reference_frame_count` | INT | Hayır | 1 ila 16384 | Başlangıç karelerinden sonra referans olarak kullanılacak gizli kare sayısı (varsayılan: 5). |

**Not:** `reference_frame_count` parametresi, başlangıç karelerinden sonra kullanılabilir kare sayısı ile otomatik olarak sınırlandırılır. Video gizli temsili yalnızca 1 kare uzunluğundaysa, normalleştirme işlemi yapılmaz ve orijinal gizli temsil değiştirilmeden döndürülür.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | Başlangıç kareleri normalleştirilmiş işlenmiş video gizli temsili. |
