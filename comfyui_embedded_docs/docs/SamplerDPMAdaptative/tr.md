# UyarlanabilirDPMÖrnekleyici

SamplerDPMAdaptative düğümü, örnekleme sürecinde adım boyutlarını otomatik olarak ayarlayan uyarlanabilir bir DPM (Diffusion Probabilistic Model) örnekleyici uygular. Optimum adım boyutlarını belirlemek için tolerans tabanlı hata kontrolü kullanır ve hesaplama verimliliği ile örnekleme doğruluğu arasında denge kurar. Bu uyarlanabilir yaklaşım, gerekebilecek adım sayısını azaltma potansiyeli sunarken kalitenin korunmasına yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sıra` | Örnekleyici yönteminin derecesi (varsayılan: 3) | INT | Evet | 2-3 |
| `rtol` | Hata kontrolü için bağıl tolerans (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `atol` | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) | FLOAT | Evet | 0.0-100.0 |
| `h_başlangıç` | Başlangıç adım boyutu (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `pkatsayı` | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `ikatsayı` | Adım boyutu kontrolü için integral katsayısı (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |
| `dkatsayı` | Adım boyutu kontrolü için türev katsayısı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `kabul_güvenliği` | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) | FLOAT | Evet | 0.0-100.0 |
| `eta` | Stokastiklik parametresi (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `s_gürültü` | Gürültü ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |

Tüm girdiler, uyarlanabilir örnekleme davranışını ince ayarlamak için kullanılan gelişmiş parametrelerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `sampler` | Yapılandırılmış bir DPM uyarlanabilir örnekleyici örneği döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
