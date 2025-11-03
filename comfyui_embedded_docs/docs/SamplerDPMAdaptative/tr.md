> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

SamplerDPMAdaptative düğümü, örnekleme süreci boyunca adım boyutlarını otomatik olarak ayarlayan uyarlamalı bir DPM (Diffusion Probabilistic Model) örnekleyici uygular. Hata kontrolü için tolerans tabanlı bir yaklaşım kullanarak, hesaplama verimliliği ile örnekleme doğruluğunu dengeleyen optimal adım boyutlarını belirler. Bu uyarlamalı yaklaşım, gerekli adım sayısını potansiyel olarak azaltırken kaliteyi korumaya yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sıra` | INT | Evet | 2-3 | Örnekleyici metodunun derecesi (varsayılan: 3) |
| `rtol` | FLOAT | Evet | 0.0-100.0 | Hata kontrolü için göreli tolerans (varsayılan: 0.05) |
| `atol` | FLOAT | Evet | 0.0-100.0 | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) |
| `h_başlangıç` | FLOAT | Evet | 0.0-100.0 | Başlangıç adım boyutu (varsayılan: 0.05) |
| `pkatsayı` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) |
| `ikatsayı` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için integral katsayı (varsayılan: 1.0) |
| `dkatsayı` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için türev katsayı (varsayılan: 0.0) |
| `kabul_güvenliği` | FLOAT | Evet | 0.0-100.0 | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) |
| `eta` | FLOAT | Evet | 0.0-100.0 | Stokastisite parametresi (varsayılan: 0.0) |
| `s_gürültü` | FLOAT | Evet | 0.0-100.0 | Gürültü ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Yapılandırılmış bir DPM uyarlamalı örnekleyici örneği döndürür |