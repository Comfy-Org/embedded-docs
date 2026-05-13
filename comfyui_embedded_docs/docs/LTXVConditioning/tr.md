> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/tr.md)

LTXVConditioning düğümü, video oluşturma modelleri için hem pozitif hem de negatif koşullandırma girdilerine kare hızı bilgisi ekler. Mevcut koşullandırma verilerini alır ve belirtilen kare hızı değerini her iki koşullandırma kümesine uygulayarak bunları video modeli işleme için uygun hale getirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `pozitif` | CONDITIONING | Evet | - | Kare hızı bilgisini alacak pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Kare hızı bilgisini alacak negatif koşullandırma girdisi |
| `kare_hızı` | FLOAT | Evet | 0,0 - 1000,0 | Her iki koşullandırma kümesine uygulanacak kare hızı değeri (varsayılan: 25,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negatif` | CONDITIONING | Kare hızı bilgisi uygulanmış pozitif koşullandırma |
| `negatif` | CONDITIONING | Kare hızı bilgisi uygulanmış negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `e8c18b73eb009c1b3ebcc2cb8be3dee4e065d75908607a5cf15d41f89963ee09`
