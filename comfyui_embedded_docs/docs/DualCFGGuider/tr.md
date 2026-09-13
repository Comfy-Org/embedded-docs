# İkili CFG Rehberi

Dual CFG Guider düğümü, örnekleme için iki koşullandırma girdisini bir negatif koşullandırma girdisiyle birlikte kullanan bir yönlendirme sistemi oluşturur. Her bir koşullandırmanın üretilen sonucu ne kadar güçlü etkilediğini kontrol etmek için iki ayrı yönlendirme ölçeği uygular ve bu ölçekleri birleştirmenin iki yolunu destekler: "regular" ve "nested".

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yönlendirme için kullanılacak model | MODEL | Evet | - |
| `cond1` | İlk pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `cond2` | İlk pozitif koşullandırma ile negatif koşullandırma arasında referans olarak kullanılan ikinci koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `cfg_conds` | İlk pozitif koşullandırmaya uygulanan yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `cfg_cond2_negative` | İkinci koşullandırma ile negatif koşullandırma arasında uygulanan yönlendirme ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `style` | Uygulanacak yönlendirme stili (varsayılan: "regular"). "nested" olarak ayarlandığında yönlendirme iç içe bir biçimde uygulanır | COMBO | Evet | "regular"<br>"nested" |

Not: `regular` stilinde, `cfg_cond2_negative`, `cond2` ile `negative` arasında uygulanır ve `cfg_conds`, `cond1` ile `cond2` arasında uygulanır. `nested` stilinde ise önce `cfg_conds`, `cond1` ile `cond2` arasında uygulanır ve elde edilen tahmin daha sonra `cfg_cond2_negative` kullanılarak `negative` değerinden uzaklaştırılır.

Not: `regular` stilinde, `cfg_cond2_negative` 1.0 değerine eşit olduğunda negatif koşullandırma atlanır ve `cfg_conds` da 1.0 değerine eşit olduğunda ikinci koşullandırma da atlanır. Bu, gerçekleştirilen model değerlendirmelerinin sayısını azaltır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme ile kullanıma hazır, yapılandırılmış bir yönlendirme sistemi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
