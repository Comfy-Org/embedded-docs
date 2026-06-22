# İkili CFG Rehberi

DualCFGGuider düğümü, çift sınıflandırıcısız yönlendirme örneklemesi için bir yönlendirme sistemi oluşturur. İki pozitif koşullandırma girdisini bir negatif koşullandırma girdisiyle birleştirir ve her koşullandırma çiftine farklı yönlendirme ölçekleri uygulayarak her bir istemin oluşturulan çıktı üzerindeki etkisini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `koşul1` | İlk pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `koşul2` | İkinci pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `cfg_koşulları` | İlk pozitif koşullandırma için yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `cfg_koşul2_negatif` | İkinci pozitif ve negatif koşullandırma için yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `stil` | Uygulanacak yönlendirme stili (varsayılan: "regular"). "nested" olarak ayarlandığında yönlendirme iç içe bir şekilde uygulanır | COMBO | Evet | "regular"<br>"nested" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme ile kullanıma hazır, yapılandırılmış bir yönlendirme sistemi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
