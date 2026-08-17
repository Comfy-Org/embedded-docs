# CFG Rehberi

CFGGuider düğümü, görüntü üretiminde örnekleme sürecini kontrol etmek için bir yönlendirme sistemi oluşturur. Pozitif ve negatif koşullandırma girdileriyle birlikte bir model alır ve üretimi istenen içeriğe yönlendirirken istenmeyen öğelerden kaçınmak için sınıflandırıcısız yönlendirme ölçeği uygular. Bu düğüm, örnekleme düğümleri tarafından görüntü üretim yönünü kontrol etmek için kullanılabilen bir yönlendirici nesnesi çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `positive` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `cfg` | Koşullandırmanın üretimi ne kadar güçlü etkileyeceğini kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 ile 100.0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme düğümlerine aktarılarak üretim sürecini kontrol etmek için kullanılabilen bir yönlendirici nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
