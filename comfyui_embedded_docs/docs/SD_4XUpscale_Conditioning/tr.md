> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

SD_4XUpscale_Conditioning düğümü, difüzyon modellerini kullanarak görüntüleri yukarı ölçeklendirmek için koşullandırma verilerini hazırlar. Girdi görüntülerini ve koşullandırma verilerini alır, ardından yukarı ölçeklendirme sürecine rehberlik edecek şekilde değiştirilmiş koşullandırma oluşturmak için ölçeklendirme ve gürültü artırma uygular. Düğüm, hem pozitif hem de negatif koşullandırmanın yanı sıra yukarı ölçeklenmiş boyutlar için gizli temsilleri çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Yukarı ölçeklenecek girdi görüntüleri |
| `positive` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma verileri |
| `negative` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma verileri |
| `scale_ratio` | FLOAT | Hayır | 0.0 - 10.0 | Girdi görüntülerine uygulanan ölçeklendirme faktörü (varsayılan: 4.0) |
| `noise_augmentation` | FLOAT | Hayır | 0.0 - 1.0 | Yukarı ölçeklendirme sürecinde eklenen gürültü miktarı (varsayılan: 0.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Yukarı ölçeklendirme bilgisi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Yukarı ölçeklendirme bilgisi uygulanmış değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Yukarı ölçeklenmiş boyutlarla eşleşen boş gizli temsil |