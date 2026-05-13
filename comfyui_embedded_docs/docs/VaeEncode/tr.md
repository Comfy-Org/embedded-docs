> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/tr.md)

Bu düğüm, belirtilen bir VAE modeli kullanarak görüntüleri bir gizli uzay temsiline kodlamak için tasarlanmıştır. Kodlama sürecinin karmaşıklığını soyutlayarak, görüntüleri gizli temsillerine dönüştürmek için basit bir yol sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `pikseller`  | `IMAGE`     | 'pixels' parametresi, gizli uzaya kodlanacak görüntü verilerini temsil eder. Kodlama süreci için doğrudan girdi görevi görerek çıktı gizli temsilinin belirlenmesinde çok önemli bir rol oynar. |
| `vae`     | VAE       | 'vae' parametresi, görüntü verilerini gizli uzaya kodlamak için kullanılacak Varyasyonel Otomatik Kodlayıcı modelini belirtir. Kodlama mekanizmasını ve oluşturulan gizli temsilin özelliklerini tanımlamak için gereklidir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, giriş görüntüsünün, temel özelliklerini sıkıştırılmış bir biçimde kapsayan, gizli uzay temsilidir. |