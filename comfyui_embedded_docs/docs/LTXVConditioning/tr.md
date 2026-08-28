# LTXVKoşullandırma

LTXVConditioning düğümü, video üretim modelleri için hem pozitif hem de negatif koşullandırma girdilerine kare hızı bilgisi ekler. Mevcut koşullandırma verilerini alır ve belirtilen kare hızı değerini her iki koşullandırma kümesine uygulayarak bunları video modeli işleme için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Kare hızı bilgisini alacak pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Kare hızı bilgisini alacak negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `kare_hızı` | Her iki koşullandırma kümesine uygulanacak kare hızı değeri (varsayılan: 25.0) | FLOAT | Evet | 0.0 - 1000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Kare hızı bilgisi uygulanmış pozitif koşullandırma | CONDITIONING |
| `negatif` | Kare hızı bilgisi uygulanmış negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
