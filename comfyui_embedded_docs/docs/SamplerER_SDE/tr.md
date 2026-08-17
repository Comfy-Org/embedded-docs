# SamplerER_SDE

The SamplerER_SDE düğümü, difüzyon modelleri için özel örnekleme yöntemleri sunar ve üç çözücü türü sağlar: ER-SDE, Reverse-time SDE ve ODE. Örnekleme sürecinin stokastik davranışını ve hesaplama aşamalarının sayısını kontrol etmeye olanak tanır. ODE çözücüsü veya deterministik bir yapılandırma (`eta`=0) seçildiğinde düğüm, gürültü ayarlarını otomatik olarak uyarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | Örnekleme için kullanılacak çözücü türü. Difüzyon sürecinin gürültü ölçekleme davranışını belirler (varsayılan: "ER-SDE"). | COMBO | Evet | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | Örnekleme süreci için maksimum aşama sayısı (varsayılan: 3). Hesaplama karmaşıklığını ve kalitesini kontrol eder. Gelişmiş parametre. | INT | Evet | 1-3 |
| `eta` | SDE'lerin stokastik gücü.<br>eta=0 olduğunda deterministik ODE'ye indirgenir.<br>Büyük eta değerleri geçersiz çıktılara neden olabilir. Bu durumda değeri düşürmeyi deneyin. (varsayılan: 1.0). Gelişmiş parametre. | FLOAT | Evet | 0.0-10.0 |
| `s_noise` | Örnekleme süreci için gürültü ölçekleme faktörü (varsayılan: 1.0). Örnekleme sırasında uygulanan gürültü miktarını kontrol eder. Gelişmiş parametre. | FLOAT | Evet | 0.0-100.0 |

**Parametre Kısıtlamaları:**

- `solver_type` "ODE" olduğunda veya `eta` 0 olduğunda, düğüm `s_noise` değerini 0.0'a zorlar ve çözücüyü "ODE" olarak değiştirir.
- `eta`, hem "ER-SDE" hem de "Reverse-time SDE" çözücü türlerini etkiler. Büyük değerler geçersiz çıktılara neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sampler` | Belirtilen çözücü ayarlarıyla örnekleme hattında kullanılabilen yapılandırılmış bir örnekleyici nesnesi. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
