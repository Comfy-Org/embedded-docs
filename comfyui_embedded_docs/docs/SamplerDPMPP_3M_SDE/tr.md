SamplerDPMPP_3M_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ 3M SDE örnekleyicisi oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametrelerine sahip üçüncü dereceden çok adımlı bir stokastik diferansiyel denklem yöntemi kullanır. Düğüm, gürültü hesaplamalarının GPU veya CPU'da yapılıp yapılmayacağını seçmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamaları için kullanılacak cihazı seçer, GPU veya CPU (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme iş akışlarında kullanılmak üzere yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `817ce8c12245063e5f2f3421f57dd55801aae96dfd8fe1bf3f88f814799b830a`
