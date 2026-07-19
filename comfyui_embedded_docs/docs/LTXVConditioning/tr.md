# LTXVKoşullandırma

LTXVConditioning düğümü, video oluşturma modelleri için hem pozitif hem de negatif koşullandırma girdilerine kare hızı bilgisi ekler. Mevcut koşullandırma verilerini alır ve belirtilen kare hızı değerini her iki koşullandırma kümesine uygulayarak bunları video modeli işleme için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Kare hızı bilgisini alacak pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Kare hızı bilgisini alacak negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `kare_hızı` | Her iki koşullandırma kümesine uygulanacak kare hızı değeri (varsayılan: 25,0) | FLOAT | Evet | 0,0 - 1000,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Kare hızı bilgisi uygulanmış pozitif koşullandırma | CONDITIONING |
| `negatif` | Kare hızı bilgisi uygulanmış negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e8c18b73eb009c1b3ebcc2cb8be3dee4e065d75908607a5cf15d41f89963ee09`
