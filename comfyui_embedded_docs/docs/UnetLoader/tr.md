UNETLoader düğümü, U-Net modellerini ada göre yüklemek için tasarlanmış olup, sistem içinde önceden eğitilmiş U-Net mimarilerinin kullanımını kolaylaştırır.

Bu düğüm, `ComfyUI/models/diffusion_models` klasöründe bulunan modelleri algılayacaktır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `unet_adı` | Yüklenecek U-Net modelinin adını belirtir. Bu ad, modeli önceden tanımlanmış bir dizin yapısı içinde konumlandırmak için kullanılır ve farklı U-Net modellerinin dinamik olarak yüklenmesini sağlar. | COMBO[STRING] |
| `ağırlık_veri_türü` | 🚧  fp8_e4m3fn fp9_e5m2 | ... |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yüklenen U-Net modelini döndürür ve sistem içinde daha ileri işleme veya çıkarım için kullanılmasına olanak tanır. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/tr.md)
