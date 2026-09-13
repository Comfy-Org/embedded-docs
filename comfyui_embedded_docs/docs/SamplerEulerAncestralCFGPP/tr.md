# Euler Atasal Örnekleyici CFG++

SamplerEulerAncestralCFG++ düğümü, görüntü üretimi için sınıflandırıcısız yönlendirme (CFG++) ile Euler Ancestral yöntemini kullanan bir örnekleyici oluşturur. Bu örnekleyici, tutarlılığı korurken çeşitli görüntü varyasyonları üretmek için atasal örnekleme tekniklerini yönlendirme koşullandırmasıyla birleştirir ve gürültü ile adım boyutu ayarlamalarını kontrol eden parametreler aracılığıyla ince ayar yapılmasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sırasındaki adım boyutunu kontrol eder; daha yüksek değerler daha agresif güncellemelere yol açar (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `s_noise` | Örnekleme işlemi sırasında eklenen gürültü miktarını ayarlar (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Görüntü üretim iş akışında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/tr.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
