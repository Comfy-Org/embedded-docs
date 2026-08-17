# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet düğümü, taban modelin davranışını değiştirmek için bir difüzyon sentezi kontrol ağı yaması uygular. Üretim sürecini ayarlanabilir güçle yönlendirmek için bir görüntü girdisi ve isteğe bağlı maske kullanır; böylece kontrol ağının etkisini içeren, daha kontrollü görüntü sentezi için yamalı bir model oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kontrol ağı ile yamalanacak taban model | MODEL | Evet | - |
| `model_patch` | Taban modele uygulanacak kontrol ağı yama modeli | MODEL_PATCH | Evet | - |
| `vae` | Difüzyon sürecinde kullanılan VAE (Varyasyonel Otokodlayıcı) | VAE | Evet | - |
| `image` | Kontrol ağını yönlendirmek için kullanılan girdi görüntüsü (yalnızca RGB kanalları kullanılır) | IMAGE | Evet | - |
| `strength` | Kontrol ağı etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | -10.0 ila 10.0 (adım: 0.01) |
| `mask` | Kontrol ağının uygulanması gereken alanları tanımlayan isteğe bağlı maske (dahili olarak ters çevrilir) | MASK | Hayır | - |

**Not:** Maske sağlandığında, otomatik olarak ters çevrilir (1.0 - maske) ve kontrol ağı işleme tarafından beklenen boyutlara uyacak şekilde yeniden şekillendirilir. Model yaması bir ZImage Control tipinde olduğunda, yama hem gürültü arıtıcıya hem de çift bloklara uygulanır; standart bir DiffSynth kontrol ağı için yalnızca çift blok yaması uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Difüzyon sentezi kontrol ağı yaması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
