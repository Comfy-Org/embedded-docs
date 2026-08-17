# ÖrnekleyiciDPMPP_2M_SDE

SamplerDPMPP_2M_SDE düğümü, difüzyon modelleri için bir DPM++ 2M SDE örnekleyici oluşturur. Bu örnekleyici, örnekler üretmek için ikinci dereceden çok adımlı bir çözücüyü stokastik diferansiyel denklem (SDE) gürültüsüyle birleştirir. Örnekleme sürecini kontrol etmek için farklı çözücü türleri ve gürültü işleme seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `solver_type` | Örnekleme sırasında kullanılacak diferansiyel denklem çözücüsünün türü: "midpoint" veya "heun" (varsayılan: "midpoint") | COMBO | Evet | "midpoint"<br>"heun" |
| `eta` | Örnekleme sürecindeki stokastiklik (rastgelelik) miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `noise_device` | Gürültü hesaplamaları için kullanılan cihaz. "gpu", potansiyel olarak daha hızlı performans için gürültü üretimini GPU üzerinde gerçekleştirir; "cpu" ise CPU'yu kullanır (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

Not: `noise_device` "cpu" olarak ayarlandığında, düğüm `dpmpp_2m_sde` örnekleyicisini oluşturur. "gpu" olarak ayarlandığında, gürültüyle ilgili hesaplamaları GPU üzerinde gerçekleştiren `dpmpp_2m_sde_gpu` varyantını oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanıma hazır, yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
