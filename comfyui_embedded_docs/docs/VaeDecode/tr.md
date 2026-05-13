> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/tr.md)

VAEDecode düğümü, belirtilen bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli temsilleri (latent representations) görüntülere çözmek için tasarlanmıştır. Sıkıştırılmış veri temsillerinden görüntüler oluşturma ve görüntülerin gizli uzay kodlamalarından yeniden yapılandırılmasını sağlama amacına hizmet eder.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples' parametresi, görüntülere çözülecek gizli temsilleri temsil eder. Görüntülerin yeniden oluşturulduğu sıkıştırılmış verileri sağladığı için kod çözme işlemi için kritik öneme sahiptir. |
| `vae`     | VAE       | 'vae' parametresi, gizli temsilleri görüntülere çözmek için kullanılacak Varyasyonel Otomatik Kodlayıcı modelini belirtir. Kod çözme mekanizmasının ve yeniden oluşturulan görüntülerin kalitesinin belirlenmesi için gereklidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıktı, belirtilen VAE modeli kullanılarak sağlanan gizli temsilden yeniden oluşturulan bir görüntüdür. |