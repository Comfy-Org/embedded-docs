> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/tr.md)

SamplerDPMPP_SSE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ SSE (Stokastik Diferansiyel Denklem) örnekleyici oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametreleri ve cihaz seçimi ile stokastik bir örnekleme yöntemi sağlar. Örnekleme işlem hattında kullanılabilecek bir örnekleyici nesnesi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) |
| `s_gürültü` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `r` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme davranışını etkileyen bir parametre (varsayılan: 0.5) |
| `gürültü_cihazı` | COMBO | Evet | "gpu"<br>"cpu" | Gürültü hesaplamalarının yapılacağı cihazı seçer |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hatlarında kullanılmak üzere yapılandırılmış bir DPM++ SSE örnekleyici nesnesi döndürür |