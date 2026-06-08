BasicGuider düğümü, örnekleme süreci için basit bir yönlendirme mekanizması oluşturur. Giriş olarak bir model ve koşullandırma verisi alır ve örnekleme sırasında üretim sürecini yönlendirmek için kullanılabilecek bir yönlendirici nesnesi üretir. Bu düğüm, kontrollü üretim için gereken temel yönlendirme işlevselliğini sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `koşullandırma` | Üretim sürecini yönlendiren koşullandırma verisi | CONDITIONING | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme sürecinde üretimi yönlendirmek için kullanılabilecek bir yönlendirici nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/tr.md)

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
