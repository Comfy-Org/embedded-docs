> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/tr.md)

VAEDecodeAudio düğümü, gizli temsilleri varyasyonel otokodlayıcı kullanarak ses dalga formlarına geri dönüştürür. Kodlanmış ses örneklerini alır ve bunları VAE üzerinden işleyerek orijinal sesi yeniden oluşturur, tutarlı çıkış seviyeleri sağlamak için normalleştirme uygular. Ortaya çıkan ses, 44100 Hz'lik standart örnekleme hızıyla döndürülür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | Ses dalga formuna geri çözülecek, gizli uzaydaki kodlanmış ses örnekleri |
| `vae` | VAE | Evet | - | Gizli örnekleri sese çözmek için kullanılan Varyasyonel Otokodlayıcı modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Normalleştirilmiş ses seviyesine ve 44100 Hz örnekleme hızına sahip çözülmüş ses dalga formu |