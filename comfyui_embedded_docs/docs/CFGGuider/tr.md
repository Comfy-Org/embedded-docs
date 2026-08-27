# CFG Rehberi

CFG Guider düğümü, görüntü üretiminde örnekleme sürecini kontrol etmek için bir yönlendirme sistemi oluşturur. Bir modeli, pozitif ve negatif koşullandırma girdileriyle birlikte alır ve üretimi istenen içeriğe doğru yönlendirirken istenmeyen öğelerden uzak tutmak için sınıflandırıcısız yönlendirme ölçeği uygular. Bu düğüm, örnekleme düğümleri tarafından görüntü üretim yönünü kontrol etmek için kullanılabilen bir yönlendirici nesnesi çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `pozitif` | Üretimi istenen içeriğe doğru yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `cfg` | Koşullandırmanın üretim üzerindeki etki gücünü kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 ile 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme düğümlerine aktarılabilen ve üretim sürecini kontrol etmek için kullanılan bir yönlendirici nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
