# Stablezero123Conditioning

Bu düğüm, StableZero123 modellerinde kullanılmak üzere verileri işlemek ve koşullandırmak için tasarlanmış olup, girdileri bu modellerle uyumlu ve optimize edilmiş belirli bir formatta hazırlamaya odaklanır.

## Girdiler

| Parametre | Açıklama | Comfy Veri Türü |
| --- | --- | --- |
| `clip_vision` | Görsel verileri modelin gereksinimlerine uygun şekilde işleyerek modelin görsel bağlamı anlamasını geliştirir. | `CLIP_VISION` |
| `init_image` | Model için başlangıç görüntüsü girdisi olarak görev yapar ve daha sonraki görüntü tabanlı işlemler için temel oluşturur. | `IMAGE` |
| `vae` | Varyasyonel otokodlayıcı çıktılarını entegre ederek modelin görüntü oluşturma veya değiştirme yeteneğini kolaylaştırır. | `VAE` |
| `width` | Çıktı görüntüsünün genişliğini belirleyerek model ihtiyaçlarına göre dinamik yeniden boyutlandırmaya olanak tanır. | `INT` |
| `height` | Çıktı görüntüsünün yüksekliğini belirleyerek çıktı boyutlarının özelleştirilmesini sağlar. | `INT` |
| `batch_size` | Tek bir partide işlenen görüntü sayısını kontrol ederek hesaplama verimliliğini optimize eder. | `INT` |
| `elevation` | 3B model oluşturma için yükseklik açısını ayarlayarak modelin uzamsal anlayışını geliştirir. | `FLOAT` |
| `azimuth` | 3B model görselleştirmesi için azimut açısını değiştirerek modelin yönelim algısını iyileştirir. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Pozitif koşullandırma vektörleri oluşturarak modelin pozitif özellikleri pekiştirmesine yardımcı olur. | `CONDITIONING` |
| `negative` | Negatif koşullandırma vektörleri üreterek modelin belirli özelliklerden kaçınmasına yardımcı olur. | `CONDITIONING` |
| `latent` | Gizli temsiller oluşturarak modelin verilere ilişkin daha derin içgörüler elde etmesini kolaylaştırır. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/tr.md)
