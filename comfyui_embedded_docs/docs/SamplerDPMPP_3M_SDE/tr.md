# ÖrnekleyiciDPMPP_3M_SDE

SamplerDPMPP_3M_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ 3M SDE örnekleyici oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametrelerine sahip üçüncü dereceden çok adımlı stokastik diferansiyel denklem yöntemini kullanır. Düğüm, gürültü hesaplamalarının GPU'da mı yoksa CPU'da mı yapılacağını seçmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamaları için cihazı seçer, GPU veya CPU (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

Not: Üç girdi de gelişmiş parametrelerdir.

`noise_device` "cpu" olarak ayarlandığında standart `dpmpp_3m_sde` örnekleyici oluşturulur; "gpu" olarak ayarlandığında GPU hızlandırmalı `dpmpp_3m_sde_gpu` örnekleyici oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `sampler` | Örnekleme iş akışlarında kullanılmak üzere yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
