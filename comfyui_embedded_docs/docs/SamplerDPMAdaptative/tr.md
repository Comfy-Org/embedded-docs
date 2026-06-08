SamplerDPMAdaptative düğümü, örnekleme işlemi sırasında adım boyutlarını otomatik olarak ayarlayan uyarlanabilir bir DPM (Difüzyon Olasılıksal Modeli) örnekleyicisi uygular. Optimum adım boyutlarını belirlemek için tolerans tabanlı hata kontrolü kullanarak hesaplama verimliliği ile örnekleme doğruluğu arasında denge kurar. Bu uyarlanabilir yaklaşım, potansiyel olarak gereken adım sayısını azaltırken kalitenin korunmasına yardımcı olur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sıra` | Örnekleyici yönteminin derecesi (varsayılan: 3) | INT | Evet | 2-3 |
| `rtol` | Hata kontrolü için bağıl tolerans (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `atol` | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) | FLOAT | Evet | 0.0-100.0 |
| `h_başlangıç` | Başlangıç adım boyutu (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `pkatsayı` | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `ikatsayı` | Adım boyutu kontrolü için integral katsayısı (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |
| `dkatsayı` | Adım boyutu kontrolü için türev katsayısı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `kabul_güvenliği` | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) | FLOAT | Evet | 0.0-100.0 |
| `eta` | Rastgelelik parametresi (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `s_gürültü` | Gürültü ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Yapılandırılmış bir DPM uyarlanabilir örnekleyici örneği döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

---
**Source fingerprint (SHA-256):** `2815ba8c3325d3d099de685edc99e9ff8e90736c1f4bd0188165969179cb99fa`
