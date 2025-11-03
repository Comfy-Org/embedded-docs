> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/tr.md)

FreSca düğümü, örnekleme sürecinde frekansa bağlı ölçeklendirme uygular. Kılavuzluk sinyalini Fourier filtreleme kullanarak düşük frekanslı ve yüksek frekanslı bileşenlere ayırır, ardından bunları yeniden birleştirmeden önce her bir frekans aralığına farklı ölçeklendirme faktörleri uygular. Bu, kılavuzluğun oluşturulan çıktının farklı yönlerini nasıl etkilediği üzerinde daha nüanslı kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Frekans ölçeklendirmesinin uygulanacağı model |
| `düşük_ölçek` | FLOAT | Hayır | 0-10 | Düşük frekanslı bileşenler için ölçeklendirme faktörü (varsayılan: 1.0) |
| `yüksek_ölçek` | FLOAT | Hayır | 0-10 | Yüksek frekanslı bileşenler için ölçeklendirme faktörü (varsayılan: 1.25) |
| `frekans_kesme` | INT | Hayır | 1-10000 | Düşük frekans olarak değerlendirilecek merkez etrafındaki frekans indekslerinin sayısı (varsayılan: 20) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Kılavuzluk fonksiyonuna frekansa bağlı ölçeklendirme uygulanmış modifiye edilmiş model |