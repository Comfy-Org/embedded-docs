# LTXV Çift CFG Yönlendirici

Bu düğüm, LTXV-AV modelleri için rehberli bir örnekleme nesnesi (CFG guider) oluşturur. Paketlenmiş latentin video ve ses bölümlerine ayrı birer rehberlik ölçeği uygulayarak, koşullandırmanın etkisini her bir modalite üzerinde bağımsız olarak kontrol etmenizi sağlar. İki ölçek birbirine eşitse veya latent ayrı video ve ses bileşenleri içermiyorsa, tek bir genel ölçek kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme sırasında kullanılacak model. | MODEL | Evet | - |
| `pozitif` | Üretimi yönlendirmek için pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içeriklerden uzaklaştırmak için negatif koşullandırma. | CONDITIONING | Evet | - |
| `video_cfg` | Latent'in video modalitesine uygulanan rehberlik gücü (varsayılan: 3.0). | FLOAT | Evet | 0.0 ile 100.0 |
| `audio_cfg` | Latent'in ses modalitesine uygulanan rehberlik gücü (varsayılan: 7.0). | FLOAT | Evet | 0.0 ile 100.0 |

Not: `video_cfg` ve `audio_cfg` değerleri eşit veya birbirine çok yakın olduğunda, guider bu değeri tüm latent için tek bir CFG ölçeği olarak kullanır. Latent, paketlenmiş bir LTXV-AV latent değilse yalnızca `video_cfg` değeri kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `guider` | Örnekleyici düğümüne iletilecek yapılandırılmış CFG guider. | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
