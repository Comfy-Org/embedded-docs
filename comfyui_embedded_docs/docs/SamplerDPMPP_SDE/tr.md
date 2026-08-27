# ÖrnekleyiciDPMPP_SDE

SamplerDPMPP_SDE, örnekleme sürecinde kullanılmak üzere bir DPM++ SDE (Stokastik Diferansiyel Denklem) örnekleyici oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametreleri ve cihaz seçimi ile stokastik bir örnekleme yöntemi sağlar. Örnekleme hattında kullanılabilecek bir örnekleyici nesnesi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `r` | Örnekleme davranışını etkileyen bir parametre (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamalarının yapıldığı cihazı seçer. "cpu" olarak ayarlandığında `dpmpp_sde` örnekleyici oluşturulur; "gpu" olarak ayarlandığında `dpmpp_sde_gpu` örnekleyici oluşturulur (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

Not: Tüm girdiler gelişmiş parametreler olarak işaretlenmiştir. `noise_device` seçimi hangi örnekleyici çeşidinin oluşturulacağını değiştirir: "cpu", `dpmpp_sde` ile eşlenir ve "gpu", `dpmpp_sde_gpu` ile eşlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hatlarında kullanılmak üzere yapılandırılmış bir DPM++ SDE örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
