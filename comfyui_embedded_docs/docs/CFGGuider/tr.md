CFGGuider düğümü, görüntü oluşturma sürecinde örnekleme işlemini kontrol etmek için bir yönlendirme sistemi oluşturur. Bir model ile pozitif ve negatif koşullandırma girdilerini alır, ardından sınıflandırıcısız bir yönlendirme ölçeği uygulayarak oluşturmayı istenen içeriğe yönlendirirken istenmeyen öğelerden kaçınır. Bu düğüm, örnekleme düğümleri tarafından görüntü oluşturma yönünü kontrol etmek için kullanılabilen bir yönlendirici nesnesi çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `pozitif` | Oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | Oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `cfg` | Koşullandırmanın oluşturma üzerindeki etkisini kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8,0) | FLOAT | Evet | 0,0 ila 100,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Oluşturma sürecini kontrol etmek için örnekleme düğümlerine aktarılabilen bir yönlendirici nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
