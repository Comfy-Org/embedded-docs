> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/tr.md)

UNetTemporalAttentionMultiply düğümü, zamansal bir UNet modelindeki farklı dikkat mekanizmalarına çarpım faktörleri uygular. Modeli, öz-dikkat ve çapraz dikkat katmanlarının ağırlıklarını ayarlayarak değiştirir ve yapısal ve zamansal bileşenler arasında ayrım yapar. Bu, her bir dikkat türünün model çıktısı üzerinde ne kadar etkiye sahip olduğunun ince ayarını yapmayı sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dikkat çarpanları ile değiştirilecek giriş modeli |
| `self_structural` | FLOAT | Hayır | 0.0 - 10.0 | Öz-dikkat yapısal bileşenleri için çarpan (varsayılan: 1.0) |
| `self_temporal` | FLOAT | Hayır | 0.0 - 10.0 | Öz-dikkat zamansal bileşenleri için çarpan (varsayılan: 1.0) |
| `cross_structural` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkat yapısal bileşenleri için çarpan (varsayılan: 1.0) |
| `cross_temporal` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkat zamansal bileşenleri için çarpan (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Ayarlanmış dikkat ağırlıklarına sahip değiştirilmiş model |