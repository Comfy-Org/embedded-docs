> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/tr.md)

Bu düğüm, bir görüntü ve bir kontrol ağı modeline dayanarak koşullandırma verilerine gelişmiş kontrol ağı dönüşümleri uygular. Kontrol ağının oluşturulan içerik üzerindeki etkisinin ince ayarlı şekilde ayarlanmasına olanak tanıyarak, koşullandırmada daha hassas ve çeşitli değişiklikler yapılmasını sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Kontrol ağı dönüşümlerinin uygulanacağı pozitif koşullandırma verileri. Oluşturulan içerikte geliştirilmesi veya korunması istenen öznitelikleri veya özellikleri temsil eder. |
| `negative` | `CONDITIONING` | Oluşturulan içerikten azaltılması veya çıkarılması istenen öznitelikleri veya özellikleri temsil eden negatif koşullandırma verileri. Kontrol ağı dönüşümleri bu verilere de uygulanarak içerik özelliklerinin dengeli bir şekilde ayarlanmasına olanak tanır. |
| `control_net` | `CONTROL_NET` | Kontrol ağı modeli, koşullandırma verilerine yapılacak belirli ayarlamaları ve iyileştirmeleri tanımlamak için çok önemlidir. Referans görüntüyü ve güç parametrelerini yorumlayarak dönüşümler uygular ve hem pozitif hem de negatif koşullandırma verilerindeki öznitelikleri değiştirerek nihai çıktıyı önemli ölçüde etkiler. |
| `image` | `IMAGE` | Kontrol ağı dönüşümleri için referans görevi gören görüntü. Kontrol ağının koşullandırma verilerine yaptığı ayarlamaları etkileyerek belirli özelliklerin geliştirilmesine veya bastırılmasına rehberlik eder. |
| `strength` | `FLOAT` | Kontrol ağının koşullandırma verileri üzerindeki etkisinin yoğunluğunu belirleyen skaler bir değer. Daha yüksek değerler daha belirgin ayarlamalarla sonuçlanır. |
| `start_percent` | `FLOAT` | Kontrol ağı etkisinin başlangıç yüzdesi, dönüşümlerin belirli bir aralıkta kademeli olarak uygulanmasına olanak tanır. |
| `end_percent` | `FLOAT` | Kontrol ağı etkisinin bitiş yüzdesi, dönüşümlerin uygulandığı aralığı tanımlar. Bu, ayarlama süreci üzerinde daha incelikli bir kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Kontrol ağı dönüşümlerinin uygulanmasından sonra, giriş parametrelerine göre yapılan iyileştirmeleri yansıtan değiştirilmiş pozitif koşullandırma verileri. |
| `negative` | `CONDITIONING` | Kontrol ağı dönüşümlerinin uygulanmasından sonra, giriş parametrelerine göre belirli özelliklerin bastırılmasını veya kaldırılmasını yansıtan değiştirilmiş negatif koşullandırma verileri. |