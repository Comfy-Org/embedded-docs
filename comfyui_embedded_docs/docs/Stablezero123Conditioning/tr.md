> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/tr.md)

Bu düğüm, StableZero123 modellerinde kullanılmak üzere verileri işlemek ve koşullandırmak için tasarlanmış olup, girdileri bu modellerle uyumlu ve optimize edilmiş belirli bir formatta hazırlamaya odaklanır.

## Girdiler

| Parametre             | Comfy Veri Türü | Açıklama |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Görsel verileri modelin gereksinimlerine uygun şekilde işleyerek modelin görsel bağlamı anlamasını geliştirir. |
| `init_image`          | `IMAGE`            | Model için başlangıç görüntüsü girdisi olarak görev yapar ve daha sonraki görüntü tabanlı işlemler için temel oluşturur. |
| `vae`                 | `VAE`              | Varyasyonel otokodlayıcı çıktılarını entegre ederek modelin görüntü oluşturma veya değiştirme yeteneğini kolaylaştırır. |
| `width`               | `INT`              | Çıktı görüntüsünün genişliğini belirleyerek model ihtiyaçlarına göre dinamik yeniden boyutlandırmaya olanak tanır. |
| `height`              | `INT`              | Çıktı görüntüsünün yüksekliğini belirleyerek çıktı boyutlarının özelleştirilmesini sağlar. |
| `batch_size`          | `INT`              | Tek bir partide işlenen görüntü sayısını kontrol ederek hesaplama verimliliğini optimize eder. |
| `elevation`           | `FLOAT`            | 3B model oluşturma için yükseklik açısını ayarlayarak modelin uzamsal anlayışını geliştirir. |
| `azimuth`             | `FLOAT`            | 3B model görselleştirmesi için azimut açısını değiştirerek modelin yönelim algısını iyileştirir. |

## Çıktılar

| Parametre     | Veri Türü | Açıklama |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Pozitif koşullandırma vektörleri oluşturarak modelin pozitif özellikleri pekiştirmesine yardımcı olur. |
| `negative`    | `CONDITIONING` | Negatif koşullandırma vektörleri üreterek modelin belirli özelliklerden kaçınmasına yardımcı olur. |
| `latent`      | `LATENT`     | Gizli temsiller oluşturarak modelin verilere ilişkin daha derin içgörüler elde etmesini kolaylaştırır. |