> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/tr.md)

Differential Diffusion düğümü, zaman adımı eşiklerine dayalı bir ikili maske uygulayarak gürültü giderme işlemini değiştirir. Orijinal gürültü giderme maskesi ile eşik tabanlı ikili maske arasında geçiş yapan bir maske oluşturur ve böylece difüzyon işleminin gücünün kontrollü bir şekilde ayarlanmasına olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Değiştirilecek difüzyon modeli |
| `strength` | FLOAT | Hayır | 0.0 - 1.0 | Orijinal gürültü giderme maskesi ile ikili eşik maskesi arasındaki karıştırma gücünü kontrol eder (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Güncellenmiş gürültü giderme maske fonksiyonuna sahip değiştirilmiş difüzyon modeli |