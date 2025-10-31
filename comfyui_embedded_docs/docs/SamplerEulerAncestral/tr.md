> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/tr.md)

SamplerEulerAncestral düğümü, görüntü oluşturmak için bir Euler Ata Sampler'ı oluşturur. Bu sampler, görüntü varyasyonları üretmek için Euler entegrasyonunu ata örnekleme teknikleriyle birleştiren belirli bir matematiksel yaklaşım kullanır. Düğüm, oluşturma sürecindeki rastgeleliği ve adım boyutunu kontrol eden parametreleri ayarlayarak örnekleme davranışını yapılandırmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sürecinin adım boyutunu ve stokastikliğini kontrol eder (varsayılan: 1.0) |
| `s_noise` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hattında kullanılabilecek yapılandırılmış bir Euler Ata Sampler'ı döndürür |