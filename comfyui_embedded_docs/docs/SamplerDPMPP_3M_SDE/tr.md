# ÖrnekleyiciDPMPP_3M_SDE

The SamplerDPMPP_3M_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ 3M SDE örnekleyicisi oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametrelerine sahip üçüncü dereceden çok adımlı stokastik diferansiyel denklem yöntemini kullanır. Düğüm, gürültü hesaplamalarının GPU veya CPU üzerinde yapılmasını seçmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin rastgeleliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `noise_device` | Gürültü hesaplamaları için cihazı seçer: GPU veya CPU (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme iş akışlarında kullanılmak üzere yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
