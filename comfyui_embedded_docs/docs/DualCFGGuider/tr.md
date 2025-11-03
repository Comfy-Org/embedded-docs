> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

DualCFGGuider düğümü, çift sınıflandırıcısız kılavuzluk örneklemesi için bir kılavuzluk sistemi oluşturur. İki pozitif koşullandırma girişini bir negatif koşullandırma girişiyle birleştirir ve her bir koşullandırma çiftine farklı kılavuzluk ölçekleri uygulayarak her bir istemin oluşturulan çıktı üzerindeki etkisini kontrol eder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kılavuzluk için kullanılacak model |
| `koşul1` | CONDITIONING | Evet | - | İlk pozitif koşullandırma girişi |
| `koşul2` | CONDITIONING | Evet | - | İkinci pozitif koşullandırma girişi |
| `negatif` | CONDITIONING | Evet | - | Negatif koşullandırma girişi |
| `cfg_koşulları` | FLOAT | Evet | 0.0 - 100.0 | İlk pozitif koşullandırma için kılavuzluk ölçeği (varsayılan: 8.0) |
| `cfg_koşul2_negatif` | FLOAT | Evet | 0.0 - 100.0 | İkinci pozitif ve negatif koşullandırma için kılavuzluk ölçeği (varsayılan: 8.0) |
| `style` | COMBO | Evet | "regular"<br>"nested" | Uygulanacak kılavuzluk stili (varsayılan: "regular") |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Örnekleme ile kullanıma hazır yapılandırılmış bir kılavuzluk sistemi |