> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

DualCFGGuider düğümü, çift sınıflandırıcısız yönlendirme örneklemesi için bir yönlendirme sistemi oluşturur. İki pozitif koşullandırma girdisini bir negatif koşullandırma girdisiyle birleştirir ve her koşullandırma çiftine farklı yönlendirme ölçekleri uygulayarak her bir istemin oluşturulan çıktı üzerindeki etkisini kontrol eder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|----------|
| `model` | MODEL | Evet | - | Yönlendirme için kullanılacak model |
| `cond1` | CONDITIONING | Evet | - | İlk pozitif koşullandırma girdisi |
| `cond2` | CONDITIONING | Evet | - | İkinci pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Negatif koşullandırma girdisi |
| `cfg_conds` | FLOAT | Evet | 0.0 - 100.0 | İlk pozitif koşullandırma için yönlendirme ölçeği (varsayılan: 8.0) |
| `cfg_cond2_negative` | FLOAT | Evet | 0.0 - 100.0 | İkinci pozitif ve negatif koşullandırma için yönlendirme ölçeği (varsayılan: 8.0) |
| `style` | COMBO | Evet | "regular"<br>"nested" | Uygulanacak yönlendirme stili (varsayılan: "regular"). "nested" olarak ayarlandığında yönlendirme iç içe bir şekilde uygulanır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `GUIDER` | GUIDER | Örnekleme ile kullanıma hazır, yapılandırılmış bir yönlendirme sistemi |

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
