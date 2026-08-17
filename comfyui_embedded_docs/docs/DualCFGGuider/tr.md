# İkili CFG Rehberi

DualCFGGuider düğümü, çift sınıflandırıcısız rehberlik örneklemesi için bir rehberlik sistemi oluşturur. İki pozitif koşullandırma girdisini bir negatif koşullandırma girdisiyle birleştirir ve her koşullandırma çiftine farklı rehberlik ölçekleri uygulayarak her istemin oluşturulan çıktıyı ne kadar güçlü etkilediğini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Rehberlik için kullanılacak model. | MODEL | Evet | - |
| `cond1` | İlk pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `cond2` | Ara koşullandırma olarak ele alınan ikinci pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negative` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `cfg_conds` | `cond1` ve `cond2` arasında uygulanan rehberlik ölçeği (varsayılan: 8.0). | FLOAT | Evet | 0.0 - 100.0 |
| `cfg_cond2_negative` | `cond2` ile negatif koşullandırma arasında uygulanan rehberlik ölçeği (varsayılan: 8.0). | FLOAT | Evet | 0.0 - 100.0 |
| `style` | Uygulanacak rehberlik stili (varsayılan: "regular"). "regular" her iki rehberlik ölçeğini tek adımda birleştirir; "nested" önce `cfg_conds` uygular ve ardından sonucu, negatif koşullandırmaya göre `cfg_cond2_negative` ile ölçekler. | COMBO | Evet | "regular"<br>"nested" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme ile kullanıma hazır, yapılandırılmış bir rehberlik sistemi. | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
