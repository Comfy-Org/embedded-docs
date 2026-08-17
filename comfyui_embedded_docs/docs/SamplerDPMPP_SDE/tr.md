# ÖrnekleyiciDPMPP_SDE

The SamplerDPMPP_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ SDE (Stokastik Diferansiyel Denklem) örnekleyici oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametreleri ve cihaz seçimi ile stokastik bir örnekleme yöntemi sağlar. Örnekleme hattında kullanılabilecek bir örnekleyici nesnesi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `r` | Örnekleme davranışını etkileyen bir parametre (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 |
| `noise_device` | Gürültü hesaplamalarının yapıldığı cihazı seçer (varsayılan: "gpu"). "cpu" olarak ayarlandığında standart `dpmpp_sde` örnekleyici kullanılır; "gpu" olarak ayarlandığında `dpmpp_sde_gpu` örnekleyici kullanılır. | COMBO | Evet | "gpu"<br>"cpu" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hatlarında kullanılmak üzere yapılandırılmış bir DPM++ SDE örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
