# İkili CFG Rehberi

DualCFGGuider düğümü, çift sınıflandırıcısız rehberlik örneklemesi için bir rehberlik sistemi oluşturur. İki koşullandırma girdisini bir negatif koşullandırma girdisiyle birleştirir ve her koşullandırmanın üretilen çıktıyı ne kadar güçlü etkilediğini kontrol etmek için iki ayrı rehberlik ölçeği uygular. Bu rehberlik ölçeklerini birleştirmenin iki stilini destekler: "regular" ve "nested".

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Rehberlik için kullanılacak model | MODEL | Evet | - |
| `koşul1` | İlk pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `koşul2` | İlk pozitif koşullandırma ile negatif koşullandırma arasında referans olarak kullanılan ikinci koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `cfg_koşulları` | İlk pozitif koşullandırmaya uygulanan rehberlik ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `cfg_koşul2_negatif` | İkinci koşullandırma ile negatif koşullandırma arasında uygulanan rehberlik ölçeği (varsayılan: 8.0) | FLOAT | Evet | 0.0 - 100.0 |
| `stil` | Uygulanacak rehberlik stili (varsayılan: "regular"). "nested" olarak ayarlandığında, rehberlik iç içe bir şekilde uygulanır | COMBO | Evet | "regular"<br>"nested" |

Not: `regular` stilde, `cfg_cond2_negative`, `cond2` ile `negative` arasında uygulanır ve `cfg_conds`, `cond1` ile `cond2` arasında uygulanır. `nested` stilde, `cfg_conds` önce `cond1` ile `cond2` arasında uygulanır ve elde edilen tahmin daha sonra `cfg_cond2_negative` kullanılarak `negative`'den uzaklaştırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme ile kullanıma hazır, yapılandırılmış bir rehberlik sistemi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/tr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
