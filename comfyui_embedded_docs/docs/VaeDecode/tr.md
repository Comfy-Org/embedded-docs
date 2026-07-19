# VAE Kod Çözme

VAEDecode düğümü, belirtilen bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli temsilleri (latent representations) görüntülere çözmek için tasarlanmıştır. Sıkıştırılmış veri temsillerinden görüntüler oluşturma ve görüntülerin gizli uzay kodlamalarından yeniden yapılandırılmasını sağlama amacına hizmet eder.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, görüntülere çözülecek gizli temsilleri temsil eder. Görüntülerin yeniden oluşturulduğu sıkıştırılmış verileri sağladığı için kod çözme işlemi için kritik öneme sahiptir. | `LATENT` |
| `vae` | 'vae' parametresi, gizli temsilleri görüntülere çözmek için kullanılacak Varyasyonel Otomatik Kodlayıcı modelini belirtir. Kod çözme mekanizmasının ve yeniden oluşturulan görüntülerin kalitesinin belirlenmesi için gereklidir. | VAE |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Çıktı, belirtilen VAE modeli kullanılarak sağlanan gizli temsilden yeniden oluşturulan bir görüntüdür. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/tr.md)
