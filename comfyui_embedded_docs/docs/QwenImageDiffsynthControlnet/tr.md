# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet, bir temel modele difüzyon sentez kontrol ağı yaması uygular. Ayarlanabilir güçle modelin üretim sürecine yol göstermek için bir giriş görüntüsü ve isteğe bağlı bir maske kullanır; daha kontrollü görüntü sentezi için kontrol ağının etkisini içeren yamalı bir model üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol ağıyla yamalanacak temel model | MODEL | Evet | - |
| `model_yaması` | Temel modele uygulanacak kontrol ağı yama modeli | MODEL_PATCH | Evet | - |
| `vae` | Difüzyon sürecinde kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) | VAE | Evet | - |
| `görsel` | Kontrol ağına yol göstermek için kullanılan giriş görüntüsü. Yalnızca ilk üç renk kanalı (RGB) kullanılır; ilave kanallar atılır | IMAGE | Evet | - |
| `güç` | Kontrol ağı etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | -10.0 ila 10.0 (adım 0.01) |
| `maske` | Kontrol ağının uygulanacağı alanları tanımlayan isteğe bağlı maske. DiffSynth ve Z-Image yamaları için maske kullanılmadan önce dahili olarak ters çevrilir | MASK | Hayır | - |
| `start_percent` | Toplam örnekleme adımlarının bir kesri olarak, kontrol ağının etkili olmaya başladığı gürültü giderme sürecindeki nokta (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |
| `end_percent` | Kontrol ağının etkili olmayı bıraktığı gürültü giderme sürecindeki nokta (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |

**Not:** `start_percent` ve `end_percent` değerleri kontrol ağını gürültü giderme sürecinin bir penceresiyle sınırlar; bu pencerenin dışında model yama olmadan örneklenir. `strength` 0 olarak ayarlanırsa düğüm temel modeli değişmeden döndürür. Bir maske sağlandığında, Z-Image Control ve standart DiffSynth yolları için maske ters çevrilir (1.0 - mask) ve yeniden şekillendirilir; Qwen Image 2.1 Fun ControlNet yaması ise maskeyi verildiği gibi kullanır. Düğüm, dahili yama uygulamasını yüklenen model yamasından seçer; bu nedenle aynı girdiler Z-Image Control, Qwen Image 2.1 Fun ControlNet ve standart DiffSynth checkpoint'leri için biraz farklı davranır. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Difüzyon sentez kontrol ağı yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`
