> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/tr.md)

CFGGuider düğümü, görüntü oluşturma sürecinde örnekleme işlemini kontrol etmek için bir yönlendirme sistemi oluşturur. Bir model ile pozitif ve negatif koşullandırma girdilerini alır, ardından sınıflandırıcısız bir yönlendirme ölçeği uygulayarak oluşturmayı istenen içeriğe yönlendirirken istenmeyen öğelerden kaçınır. Bu düğüm, örnekleme düğümleri tarafından görüntü oluşturma yönünü kontrol etmek için kullanılabilen bir yönlendirici nesnesi çıktısı verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `model` | MODEL | Evet | - | Yönlendirme için kullanılacak model |
| `pozitif` | CONDITIONING | Evet | - | Oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | Oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `cfg` | FLOAT | Evet | 0,0 ila 100,0 | Koşullandırmanın oluşturma üzerindeki etkisini kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-----------|
| `GUIDER` | GUIDER | Oluşturma sürecini kontrol etmek için örnekleme düğümlerine aktarılabilen bir yönlendirici nesnesi |

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
