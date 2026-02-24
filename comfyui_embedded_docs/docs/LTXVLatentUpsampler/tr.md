> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/tr.md)

LTXVLatentUpsampler düğümü, bir video gizli (latent) temsilinin uzamsal çözünürlüğünü iki katına çıkarır. Gizli verileri işlemek için özel bir ölçek büyütme modeli kullanır; bu veriler önce sağlanan VAE'nin kanal istatistikleri kullanılarak normalleştirilmekten çıkarılır, ardından yeniden normalleştirilir. Bu düğüm, gizli uzay içindeki video iş akışları için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | | Ölçeği büyütülecek video gizli temsili. |
| `upscale_model` | LATENT_UPSCALE_MODEL | Evet | | Gizli veriler üzerinde 2x ölçek büyütme işlemini gerçekleştirmek için yüklenen model. |
| `vae` | VAE | Evet | | Giriş gizli verilerini ölçek büyütmeden önce normalleştirilmekten çıkarmak ve çıktı gizli verilerini daha sonra normalleştirmek için kullanılan VAE modeli. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Ölçeği büyütülmüş gizli temsil; uzamsal boyutları girişe kıyasla iki katına çıkarılmıştır. |
