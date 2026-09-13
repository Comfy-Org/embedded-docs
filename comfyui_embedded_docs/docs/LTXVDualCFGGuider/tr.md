# LTXV Çift CFG Yönlendirici

Bu düğüm, LTXV-AV modelleri için yönlendirilmiş bir örnekleme nesnesi (CFG yönlendiricisi) oluşturur. Paketlenmiş bir LTXV-AV latentinin video bölümüne ve ses bölümüne ayrı bir yönlendirme ölçeği uygular; böylece koşullandırmanın her modalite üzerindeki etkisini bağımsız olarak kontrol etmenizi sağlar. İki ölçek eşitse veya latent ayrı video ve ses bileşenleri içermiyorsa, bunun yerine tek bir genel ölçek kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme sırasında kullanılacak model. | MODEL | Evet | - |
| `pozitif` | Üretimi istenen yöne yönlendirmek için pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen yönden uzaklaştırmak için negatif koşullandırma. | CONDITIONING | Evet | - |
| `video_cfg` | Latentin video modalitesine uygulanan yönlendirme gücü (varsayılan: 3.0). | FLOAT | Evet | 0.0 ile 100.0 |
| `audio_cfg` | Latentin ses modalitesine uygulanan yönlendirme gücü (varsayılan: 7.0). | FLOAT | Evet | 0.0 ile 100.0 |

Not: `video_cfg` ve `audio_cfg` eşit olduğunda (veya değer olarak birbirine çok yakın olduğunda), yönlendirici bu değeri tüm latent için tek bir CFG ölçeği olarak kullanır. Latent paketlenmiş bir LTXV-AV latent değilse, yalnızca `video_cfg` değeri kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `guider` | Örnekleyici düğümüne aktarılacak yapılandırılmış CFG yönlendiricisi. | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
