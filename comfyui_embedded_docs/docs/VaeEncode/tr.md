> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/tr.md)

Bu düğüm, belirli bir VAE modeli kullanarak görüntüleri gizli (latent) uzay temsillerine kodlamak için tasarlanmıştır. Kodlama sürecinin karmaşıklığını soyutlayarak, görüntülerin gizli temsillerine dönüştürülmesi için basit bir yol sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | 'pixels' parametresi, gizli uzaya kodlanacak görüntü verisini temsil eder. Kodlama süreci için doğrudan girdi olarak hizmet ederek, çıktı gizli temsilin belirlenmesinde çok önemli bir rol oynar. |
| `vae`     | VAE       | 'vae' parametresi, görüntü verisini gizli uzaya kodlamak için kullanılacak Varyasyonel Otokodlayıcı (Variational Autoencoder) modelini belirtir. Kodlama mekanizmasını ve oluşturulan gizli temsilin özelliklerini tanımlamak için gereklidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, girdi görüntüsünün temel özelliklerini sıkıştırılmış bir formda kapsayan gizli uzay temsilidir. |