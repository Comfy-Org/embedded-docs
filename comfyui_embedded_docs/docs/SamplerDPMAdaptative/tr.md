> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

SamplerDPMAdaptative düğümü, örnekleme işlemi sırasında adım boyutlarını otomatik olarak ayarlayan uyarlanabilir bir DPM (Difüzyon Olasılıksal Modeli) örnekleyicisi uygular. Optimum adım boyutlarını belirlemek için tolerans tabanlı hata kontrolü kullanarak hesaplama verimliliği ile örnekleme doğruluğu arasında denge kurar. Bu uyarlanabilir yaklaşım, potansiyel olarak gereken adım sayısını azaltırken kalitenin korunmasına yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `order` | INT | Evet | 2-3 | Örnekleyici yönteminin derecesi (varsayılan: 3) |
| `rtol` | FLOAT | Evet | 0.0-100.0 | Hata kontrolü için bağıl tolerans (varsayılan: 0.05) |
| `atol` | FLOAT | Evet | 0.0-100.0 | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) |
| `h_init` | FLOAT | Evet | 0.0-100.0 | Başlangıç adım boyutu (varsayılan: 0.05) |
| `pcoeff` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) |
| `icoeff` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için integral katsayısı (varsayılan: 1.0) |
| `dcoeff` | FLOAT | Evet | 0.0-100.0 | Adım boyutu kontrolü için türev katsayısı (varsayılan: 0.0) |
| `accept_safety` | FLOAT | Evet | 0.0-100.0 | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) |
| `eta` | FLOAT | Evet | 0.0-100.0 | Rastgelelik parametresi (varsayılan: 0.0) |
| `s_noise` | FLOAT | Evet | 0.0-100.0 | Gürültü ölçekleme faktörü (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sampler` | SAMPLER | Yapılandırılmış bir DPM uyarlanabilir örnekleyici örneği döndürür |

---
**Source fingerprint (SHA-256):** `2815ba8c3325d3d099de685edc99e9ff8e90736c1f4bd0188165969179cb99fa`
