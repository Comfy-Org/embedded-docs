# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet, temel bir modele difüzyon sentezi kontrol ağı yaması uygular. Giriş görüntüsü ve isteğe bağlı bir maske kullanarak modelin üretim sürecini ayarlanabilir güçle yönlendirir; kontrol ağının etkisini içeren yamalı bir model üretir ve böylece daha kontrollü görüntü sentezi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol ağı ile yamalanacak temel model | MODEL | Evet | - |
| `model_yaması` | Temel modele uygulanacak kontrol ağı yama modeli | MODEL_PATCH | Evet | - |
| `vae` | Difüzyon sürecinde kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) | VAE | Evet | - |
| `görsel` | Kontrol ağını yönlendirmek için kullanılan giriş görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır; ek kanallar atılır | IMAGE | Evet | - |
| `güç` | Kontrol ağı etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | -10.0 ile 10.0 |
| `maske` | Kontrol ağının uygulanacağı alanları tanımlayan isteğe bağlı maske. Maske kullanımdan önce dahili olarak ters çevrilir | MASK | Hayır | - |

**Not:** Maske sağlandığında, maske otomatik olarak ters çevrilir (1.0 - maske) ve kontrol ağı işleme için beklenen boyutlara yeniden şekillendirilir. Düğüm, model yamasının bir ZImage Kontrol tipi mi yoksa standart bir DiffSynth kontrol ağı mı olduğuna bağlı olarak farklı dahili işleme yöntemleri kullanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Difüzyon sentezi kontrol ağı yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
