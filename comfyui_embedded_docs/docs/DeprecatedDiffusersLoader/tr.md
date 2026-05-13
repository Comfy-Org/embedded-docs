> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/tr.md)

DiffusersLoader düğümü, diffusers kütüphanesinden modeller yüklemek için tasarlanmış olup, sağlanan model yollarına göre UNet, CLIP ve VAE modellerinin yüklenmesini özel olarak yönetir. Bu modellerin ComfyUI çerçevesine entegrasyonunu kolaylaştırarak metinden görüntü oluşturma, görüntü işleme ve daha fazlası gibi gelişmiş işlevleri mümkün kılar.

## Girişler

| Parametre     | Veri Türü    | Açıklama |
|---------------|--------------|-------------|
| `model_path`  | COMBO[STRING] | Yüklenecek modelin yolunu belirtir. Bu yol, sonraki işlemler için hangi modelin kullanılacağını belirlediğinden kritiktir ve düğümün çıktısını ve yeteneklerini etkiler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Çıktı demetinin bir parçası olan yüklenmiş UNet modeli. Bu model, ComfyUI çerçevesinde görüntü sentezi ve işleme görevleri için gereklidir. |
| `clip`    | CLIP      | İstenirse çıktı demetine dahil edilen yüklenmiş CLIP modeli. Bu model, gelişmiş metin ve görüntü anlama ile işleme yetenekleri sağlar. |
| `vae`     | VAE       | İstenirse çıktı demetine dahil edilen yüklenmiş VAE modeli. Bu model, gizli uzay işleme ve görüntü oluşturma içeren görevler için kritiktir. |