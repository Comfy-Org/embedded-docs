> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/tr.md)

SamplerDPMPP_3M_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ 3M SDE örnekleyici oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametrelerine sahip üçüncü dereceden çok adımlı stokastik diferansiyel denklem yöntemini kullanır. Düğüm, gürültü hesaplamalarının GPU'da mı yoksa CPU'da mı gerçekleştirileceğini seçmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) |
| `s_noise` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `noise_device` | COMBO | Evet | "gpu"<br>"cpu" | Gürültü hesaplamaları için cihazı seçer, GPU veya CPU |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme iş akışlarında kullanılmak üzere yapılandırılmış bir örnekleyici nesnesi döndürür |