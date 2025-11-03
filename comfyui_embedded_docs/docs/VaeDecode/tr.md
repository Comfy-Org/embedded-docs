> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/tr.md)

VAEDecode düğümü, belirli bir Varyasyonel Otokodlayıcı (VAE) kullanarak gizli temsilleri görüntülere dönüştürmek için tasarlanmıştır. Amacı, sıkıştırılmış veri temsillerinden görüntüler oluşturmak ve gizli uzay kodlamalarından görüntülerin yeniden yapılandırılmasını sağlamaktır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `örnekler` | `LATENT`    | 'samples' parametresi, görüntülere dönüştürülecek gizli temsilleri belirtir. Kod çözme işlemi için kritik öneme sahiptir çünkü görüntülerin yeniden oluşturulduğu sıkıştırılmış veriyi sağlar. |
| `vae`     | VAE       | 'vae' parametresi, gizli temsilleri görüntülere dönüştürmek için kullanılacak Varyasyonel Otokodlayıcı modelini belirtir. Kod çözme mekanizmasını ve yeniden oluşturulan görüntülerin kalitesini belirlemede esastır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıktı, belirtilen VAE modeli kullanılarak sağlanan gizli temsilden yeniden oluşturulmuş bir görüntüdür. |