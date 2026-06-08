PerpNegGuider düğümü, dik negatif koşullandırma kullanarak görüntü oluşturmayı kontrol etmek için bir yönlendirme sistemi oluşturur. Pozitif, negatif ve boş koşullandırma girdilerini alır ve oluşturma sürecini yönlendirmek için özel bir yönlendirme algoritması uygular. Bu düğüm, deneysel testler için tasarlanmıştır ve yönlendirme gücü ile negatif ölçeklendirme üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme oluşturma için kullanılacak model | MODEL | Evet | - |
| `pozitif` | Oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | Oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `boş_koşullandırma` | Temel referans olarak kullanılan boş veya nötr koşullandırma | CONDITIONING | Evet | - |
| `cfg` | Koşullandırmanın oluşturmayı ne kadar güçlü etkileyeceğini kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `neg_ölçek` | Negatif koşullandırmanın gücünü ayarlayan negatif ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `guider` | Oluşturma hattında kullanıma hazır, yapılandırılmış bir yönlendirme sistemi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/tr.md)

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
