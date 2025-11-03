> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/tr.md)

UNETLoader düğümü, U-Net modellerini isimle yüklemek için tasarlanmış olup, sistem içinde önceden eğitilmiş U-Net mimarilerinin kullanımını kolaylaştırır.

Bu düğüm, `ComfyUI/models/diffusion_models` klasöründe bulunan modelleri tespit edecektir.

## Girdiler

| Parametre   | Veri Tipi    | Açıklama |
|-------------|--------------|-------------|
| `unet_adı` | COMBO[STRING] | Yüklenecek U-Net modelinin adını belirtir. Bu ad, önceden tanımlanmış bir dizin yapısı içinde modelin konumunu bulmak için kullanılır ve farklı U-Net modellerinin dinamik olarak yüklenmesini sağlar. |
| `ağırlık_veri_türü` | ... | 🚧  fp8_e4m3fn fp9_e5m2  |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Yüklenen U-Net modelini döndürür ve bu modelin sistem içinde daha fazla işleme veya çıkarım için kullanılmasına olanak tanır. |