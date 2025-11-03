> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/tr.md)

LTXVConditioning düğümü, video üretim modelleri için hem pozitif hem de negatif koşullandırma girişlerine kare hızı bilgisi ekler. Mevcut koşullandırma verilerini alır ve belirtilen kare hızı değerini her iki koşullandırma setine uygulayarak video model işleme için uygun hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Kare hızı bilgisi eklenecek pozitif koşullandırma girişi |
| `negatif` | CONDITIONING | Evet | - | Kare hızı bilgisi eklenecek negatif koşullandırma girişi |
| `kare_hızı` | FLOAT | Hayır | 0.0 - 1000.0 | Her iki koşullandırma setine uygulanacak kare hızı değeri (varsayılan: 25.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Kare hızı bilgisi uygulanmış pozitif koşullandırma |
| `negatif` | CONDITIONING | Kare hızı bilgisi uygulanmış negatif koşullandırma |