SamplerEulerAncestralCFGPP düğümü, görüntü oluşturma için Euler Atasal yöntemiyle sınıflandırıcısız yönlendirme (CFG++) kullanan bir örnekleyici oluşturur. Bu örnekleyici, atasal örnekleme tekniklerini yönlendirme koşullandırmasıyla birleştirerek tutarlılığı korurken çeşitli görüntü varyasyonları üretir ve gürültü ile adım boyutu ayarlamalarını kontrol eden parametreler aracılığıyla ince ayar yapılmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sırasında adım boyutunu kontrol eder; daha yüksek değerler daha agresif güncellemelerle sonuçlanır (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `s_gürültü` | Örnekleme işlemi sırasında eklenen gürültü miktarını ayarlar (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Görüntü oluşturma hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/tr.md)

---
**Source fingerprint (SHA-256):** `7eceec539a6a045db4d9953214add17011ef9d17e663dbbbbbb2bae0cbe40aa2`
