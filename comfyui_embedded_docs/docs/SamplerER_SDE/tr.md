# SamplerER_SDE

SamplerER_SDE düğümü, difüzyon modelleri için özel örnekleme yöntemleri sağlar ve farklı çözücü türleri sunar: ER-SDE, Reverse-time SDE ve ODE. Örnekleme sürecinin stokastik davranışını ve hesaplama aşamalarının sayısını kontrol etmenizi sağlar. Düğüm, seçilen çözücü türüne göre ayarları otomatik olarak uyarlayarak örnekleyicinin doğru şekilde çalışmasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `çözücü_tipi` | Örnekleme için kullanılacak çözücü türü. Difüzyon sürecinin matematiksel yaklaşımını belirler (varsayılan: "ER-SDE"). | COMBO | Evet | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `maksimum_aşama` | Örnekleme sürecindeki maksimum aşama sayısı (varsayılan: 3). Hesaplama karmaşıklığını ve kaliteyi kontrol eder. | INT | Evet | 1-3 |
| `eta` | SDE'lerin stokastik gücü.<br>eta=0 olduğunda, deterministik ODE'ye indirgenir.<br>Büyük eta değerleri geçersiz çıktılara neden olabilir. Bu durum meydana gelirse, bu değeri düşürmeyi deneyin. (varsayılan: 1.0) | FLOAT | Evet | 0.0-10.0 (adım: 0.01) |
| `s_gürültü` | Örnekleme süreci için gürültü ölçekleme faktörü (varsayılan: 1.0). Örnekleme sırasında uygulanan gürültü miktarını kontrol eder. | FLOAT | Evet | 0.0-100.0 (adım: 0.01) |

**Parametre Kısıtlamaları:**

- `solver_type` "ODE" olarak ayarlandığında veya `eta` 0 olduğunda, düğüm ODE moduna geçer ve `s_noise` için girilen değer ne olursa olsun `s_noise` değerini 0.0 olarak ayarlar.
- `eta` parametresi, hem "ER-SDE" hem de "Reverse-time SDE" çözücü türlerinin stokastik gücünü kontrol eder. Çözücü ODE modunda çalıştığında hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Belirtilen çözücü ayarlarıyla örnekleme hattında kullanılabilen, yapılandırılmış bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
