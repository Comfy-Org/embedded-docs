> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/tr.md)

Bu düğüm, bir görüntü ve bir kontrol net modeline dayanarak koşullandırma verilerine gelişmiş kontrol net dönüşümleri uygular. Kontrol net'in üretilen içerik üzerindeki etkisinin ince ayarlı düzenlemelerine olanak tanıyarak, koşullandırmada daha hassas ve çeşitli değişiklikler yapılmasını sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `pozitif` | `CONDITIONING` | Kontrol net dönüşümlerinin uygulanacağı pozitif koşullandırma verisi. Üretilen içerikte geliştirilecek veya korunacak istenen nitelikleri veya özellikleri temsil eder. |
| `negatif` | `CONDITIONING` | Üretilen içerikten azaltılacak veya kaldırılacak nitelikleri veya özellikleri temsil eden negatif koşullandırma verisi. İçeriğin özelliklerinin dengeli bir şekilde ayarlanmasına olanak tanımak için kontrol net dönüşümleri bu veriye de uygulanır. |
| `kontrol_ağı` | `CONTROL_NET` | Kontrol net modeli, koşullandırma verilerine yapılacak belirli ayarlamaları ve iyileştirmeleri tanımlamak için çok önemlidir. Referans görüntüyü ve güç parametrelerini yorumlayarak dönüşümler uygular ve hem pozitif hem de negatif koşullandırma verilerindeki nitelikleri değiştirerek nihai çıktıyı önemli ölçüde etkiler. |
| `görüntü` | `IMAGE` | Kontrol net dönüşümleri için referans olarak hizmet eden görüntü. Belirli özelliklerin geliştirilmesine veya bastırılmasına rehberlik ederek, kontrol net'in koşullandırma verilerine yaptığı ayarlamaları etkiler. |
| `güç` | `FLOAT` | Kontrol net'in koşullandırma verileri üzerindeki etki yoğunluğunu belirleyen bir skaler değer. Daha yüksek değerler, daha belirgin ayarlamalara yol açar. |
| `başlangıç_yüzdesi` | `FLOAT` | Kontrol net etkisinin başlangıç yüzdesi. Bu, dönüşümlerin belirli bir aralıkta kademeli olarak uygulanmasına olanak tanır. |
| `bitiş_yüzdesi` | `FLOAT` | Kontrol net etkisinin bitiş yüzdesi. Dönüşümlerin uygulandığı aralığı tanımlar. Bu, ayarlama süreci üzerinde daha nüanslı bir kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `negatif` | `CONDITIONING` | Kontrol net dönüşümleri uygulandıktan sonra değiştirilmiş pozitif koşullandırma verisi. Girdi parametrelerine dayalı olarak yapılan iyileştirmeleri yansıtır. |
| `negatif` | `CONDITIONING` | Kontrol net dönüşümleri uygulandıktan sonra değiştirilmiş negatif koşullandırma verisi. Girdi parametrelerine dayalı olarak belirli özelliklerin bastırılmasını veya kaldırılmasını yansıtır. |