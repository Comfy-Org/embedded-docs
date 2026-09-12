# ModelÖrneklemeSD3

Bu düğüm, bir modele Stable Diffusion 3 tarzı örnekleme ayarlarını uygular. Modelin bir kopyasını oluşturur ve örnekleme yöntemini, verilen `shift` değerini kullanan akış tabanlı bir örnekleme yapılandırmasıyla değiştirir; bu değer örnekleme dağılımının nasıl şekillendirileceğini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SD3 örnekleme parametrelerinin uygulanacağı giriş modeli | MODEL | Evet | - |
| `kaydırma` | Örnekleme kaydırma parametresini kontrol eder (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

Not: `shift` değeri, sabit bir dahili 1000 çarpanıyla birlikte uygulanır. Özgün modelde bir gürültü ölçeği ayarı varsa, bu değer değiştirilmiş modele aktarılır. Özgün model değiştirilmez; klonlanmış ve yamalanmış bir kopya döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | SD3 örnekleme parametreleri uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/tr.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
