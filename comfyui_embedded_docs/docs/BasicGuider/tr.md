> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/tr.md)

BasicGuider düğümü, örnekleme süreci için basit bir yönlendirme mekanizması oluşturur. Giriş olarak bir model ve koşullandırma verisi alır ve örnekleme sırasında üretim sürecini yönlendirmek için kullanılabilecek bir yönlendirici nesnesi üretir. Bu düğüm, kontrollü üretim için gereken temel yönlendirme işlevselliğini sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Yönlendirme için kullanılacak model |
| `conditioning` | CONDITIONING | Evet | - | Üretim sürecini yönlendiren koşullandırma verisi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Örnekleme sürecinde üretimi yönlendirmek için kullanılabilecek bir yönlendirici nesnesi |

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
