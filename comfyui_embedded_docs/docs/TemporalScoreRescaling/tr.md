> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

Bu düğüm, bir difüzyon modeline Zamansal Skor Yeniden Ölçeklendirme (TSR) uygular. Gürültü giderme sürecinde tahmin edilen gürültü veya skoru yeniden ölçekleyerek modelin örnekleme davranışını değiştirir ve bu da üretilen çıktının çeşitliliğini yönlendirebilir. Bu, bir CFG-sonrası (Sınıflandırıcısız Kılavuzluk) işlevi olarak uygulanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | TSR işlevi ile yamalanacak difüzyon modeli. |
| `tsr_k` | FLOAT | Hayır | 0.01 - 100.0 | Yeniden ölçeklendirme gücünü kontrol eder. Daha düşük k değeri daha detaylı sonuçlar üretir; daha yüksek k değeri görüntü oluşturmada daha pürüzsüz sonuçlar üretir. k = 1 ayarı yeniden ölçeklendirmeyi devre dışı bırakır. (varsayılan: 0.95) |
| `tsr_sigma` | FLOAT | Hayır | 0.01 - 100.0 | Yeniden ölçeklendirmenin ne kadar erken etkili olacağını kontrol eder. Daha büyük değerler daha erken etkili olur. (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Giriş modeli, artık örnekleme sürecine Zamansal Skor Yeniden Ölçeklendirme işlevi uygulanmış şekilde yamalanmıştır. |
