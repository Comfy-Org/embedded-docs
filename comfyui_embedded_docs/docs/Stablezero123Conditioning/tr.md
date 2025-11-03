> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/tr.md)

Bu düğüm, StableZero123 modellerinde kullanılmak üzere verileri işlemek ve koşullandırmak için tasarlanmıştır ve girdiyi bu modellerle uyumlu ve optimize edilmiş belirli bir formatta hazırlamaya odaklanır.

## Girdiler

| Parametre             | Comfy Veri Türü   | Açıklama |
|-----------------------|-------------------|-------------|
| `clip_vision`         | `CLIP_VISION`     | Modelin gereksinimleriyle uyumlu hale getirmek için görsel verileri işler, modelin görsel bağlamı anlamasını geliştirir. |
| `init_image`          | `IMAGE`           | Model için başlangıç görüntü girdisi olarak hizmet eder, görüntü tabanlı diğer işlemler için temel oluşturur. |
| `vae`                 | `VAE`             | Varyasyonel otokodlayıcı çıktılarını entegre eder, modelin görüntü oluşturma veya değiştirme yeteneğini kolaylaştırır. |
| `width`               | `INT`             | Çıktı görüntüsünün genişliğini belirtir, model ihtiyaçlarına göre dinamik yeniden boyutlandırmaya olanak tanır. |
| `height`              | `INT`             | Çıktı görüntüsünün yüksekliğini belirler, çıktı boyutlarının özelleştirilmesini sağlar. |
| `batch_size`          | `INT`             | Tek bir partide işlenen görüntü sayısını kontrol eder, hesaplama verimliliğini optimize eder. |
| `elevation`           | `FLOAT`           | 3B model oluşturma için yükseklik açısını ayarlar, modelin uzamsal anlayışını geliştirir. |
| `azimuth`             | `FLOAT`           | 3B model görselleştirmesi için azimut açısını değiştirir, modelin yönelim algısını iyileştirir. |

## Çıktılar

| Parametre     | Veri Türü      | Açıklama |
|---------------|----------------|-------------|
| `positive`    | `CONDITIONING` | Pozitif koşullandırma vektörleri oluşturur, modelin pozitif özelliklerini güçlendirmesine yardımcı olur. |
| `negative`    | `CONDITIONING` | Negatif koşullandırma vektörleri üretir, modelin belirli özelliklerden kaçınmasına yardımcı olur. |
| `latent`      | `LATENT`       | Gizil temsiller oluşturur, modelin veriye dair daha derin içgörüler elde etmesini kolaylaştırır. |