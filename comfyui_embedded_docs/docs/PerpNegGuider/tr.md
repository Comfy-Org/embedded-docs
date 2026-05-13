> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/tr.md)

PerpNegGuider düğümü, dik negatif koşullandırma kullanarak görüntü oluşturmayı kontrol etmek için bir yönlendirme sistemi oluşturur. Pozitif, negatif ve boş koşullandırma girdilerini alır ve oluşturma sürecini yönlendirmek için özel bir yönlendirme algoritması uygular. Bu düğüm, deneysel testler için tasarlanmıştır ve yönlendirme gücü ile negatif ölçeklendirme üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Yönlendirme oluşturma için kullanılacak model |
| `pozitif` | CONDITIONING | Evet | - | Oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | Oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `boş_koşullandırma` | CONDITIONING | Evet | - | Temel referans olarak kullanılan boş veya nötr koşullandırma |
| `cfg` | FLOAT | Evet | 0.0 - 100.0 | Koşullandırmanın oluşturmayı ne kadar güçlü etkileyeceğini kontrol eden sınıflandırıcısız yönlendirme ölçeği (varsayılan: 8.0) |
| `neg_ölçek` | FLOAT | Evet | 0.0 - 100.0 | Negatif koşullandırmanın gücünü ayarlayan negatif ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `guider` | GUIDER | Oluşturma hattında kullanıma hazır, yapılandırılmış bir yönlendirme sistemi |

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
