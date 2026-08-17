# UyarlanabilirDPMÖrnekleyici

SamplerDPMAdaptative düğümü, örnekleme süreci sırasında adım boyutlarını otomatik olarak ayarlayan uyarlanabilir bir DPM (Difüzyon Olasılıksal Model) örnekleyici uygular. En uygun adım boyutlarını belirlemek için tolerans tabanlı hata kontrolü kullanır ve hesaplama verimliliği ile örnekleme doğruluğunu dengeler. Bu uyarlanabilir yaklaşım, gerekli adım sayısını potansiyel olarak azaltırken kalitenin korunmasına yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `order` | Örnekleyici yönteminin derecesi (varsayılan: 3) | INT | Evet | 2-3 |
| `rtol` | Hata kontrolü için göreli tolerans (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `atol` | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) | FLOAT | Evet | 0.0-100.0 |
| `h_init` | Başlangıç adım boyutu (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `pcoeff` | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `icoeff` | Adım boyutu kontrolü için integral katsayısı (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |
| `dcoeff` | Adım boyutu kontrolü için türev katsayısı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `accept_safety` | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) | FLOAT | Evet | 0.0-100.0 |
| `eta` | Stokastiklik parametresi (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `s_noise` | Gürültü ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Yapılandırılmış bir DPM uyarlanabilir örnekleyici örneği döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
