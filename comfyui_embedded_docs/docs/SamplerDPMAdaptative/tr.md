# UyarlanabilirDPMÖrnekleyici

SamplerDPMAdaptative düğümü, örnekleme işlemi sırasında adım boyutlarını otomatik olarak ayarlayan uyarlamalı bir DPM (Difüzyon Olasılıksal Modeli) örnekleyicisi uygular. En uygun adım boyutlarını belirlemek için tolerans tabanlı hata kontrolü kullanır ve hesaplama verimliliği ile örnekleme doğruluğunu dengeler. Bu uyarlamalı yaklaşım, gereken adım sayısını potansiyel olarak azaltırken kalitenin korunmasına yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `order` | Örnekleyici yönteminin derecesi (varsayılan: 3) | INT | Evet | 2-3 |
| `rtol` | Hata kontrolü için göreli tolerans (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `atol` | Hata kontrolü için mutlak tolerans (varsayılan: 0.0078) | FLOAT | Evet | 0.0-100.0 |
| `h_init` | Başlangıç adım boyutu (varsayılan: 0.05) | FLOAT | Evet | 0.0-100.0 |
| `pcoeff` | Adım boyutu kontrolü için oransal katsayı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `icoeff` | Adım boyutu kontrolü için integral katsayısı (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |
| `dcoeff` | Adım boyutu kontrolü için türev katsayısı (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `accept_safety` | Adım kabulü için güvenlik faktörü (varsayılan: 0.81) | FLOAT | Evet | 0.0-100.0 |
| `eta` | Rastgelelik parametresi (varsayılan: 0.0) | FLOAT | Evet | 0.0-100.0 |
| `s_noise` | Gürültü ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0-100.0 |

Tüm girdiler, uyarlamalı örnekleme davranışını ince ayarlamak için kullanılan gelişmiş parametrelerdir. `order` dışında tüm sayısal girdiler ondalık değerlere izin verir ve en az 0.0 ile en fazla 100.0 değerlerini kabul eder; `order` ise yalnızca 2 veya 3 tam sayı değerleriyle sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `sampler` | Yapılandırılmış bir DPM uyarlamalı örnekleyici örneği döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/tr.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
