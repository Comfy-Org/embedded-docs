# Temel Rehber

BasicGuider düğümü, örnekleme süreci için basit bir yönlendirme mekanizması oluşturur. Girdi olarak bir model ve koşullandırma verisi alır ve örnekleme sırasında üretim sürecini yönlendirmek için kullanılabilecek bir guider nesnesi üretir. Bu düğüm, kontrollü üretim için gereken temel yönlendirme işlevselliğini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `koşullandırma` | Üretim sürecini yönlendiren koşullandırma verisi | CONDITIONING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme sürecinde üretimi yönlendirmek için kullanılabilen bir guider nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/tr.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
