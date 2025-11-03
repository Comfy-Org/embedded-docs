> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/tr.md)

DiffusersLoader düğümü, diffusers kütüphanesinden model yüklemek için tasarlanmış olup, özellikle sağlanan model yollarına dayalı olarak UNet, CLIP ve VAE modellerinin yüklenmesini işler. Bu modellerin ComfyUI çerçevesine entegrasyonunu kolaylaştırarak, metinden görüntü oluşturma, görüntü manipülasyonu ve daha fazlası gibi gelişmiş işlevlerin kullanılmasını sağlar.

## Girdiler

| Parametre    | Veri Tipi      | Açıklama |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | Yüklenecek modelin yolunu belirtir. Bu yol, hangi modelin sonraki işlemlerde kullanılacağını belirlediği ve düğümün çıktılarını ve yeteneklerini etkilediği için kritik öneme sahiptir. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Yüklenen UNet modelidir ve çıktı demetinin bir parçasıdır. Bu model, ComfyUI çerçevesi içinde görüntü sentezi ve manipülasyonu görevleri için gereklidir. |
| `clip`    | CLIP      | İstenirse çıktı demetine dahil edilen yüklenmiş CLIP modelidir. Bu model, gelişmiş metin ve görüntü anlama ve manipülasyon yetenekleri sağlar. |
| `vae`     | VAE       | İstenirse çıktı demetine dahil edilen yüklenmiş VAE modelidir. Bu model, gizli uzay manipülasyonu ve görüntü oluşturma içeren görevler için çok önemlidir. |