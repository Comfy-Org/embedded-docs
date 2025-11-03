> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/tr.md)

FluxKontextMultiReferenceLatentMethod düğümü, belirli bir referans latent yöntemi belirleyerek koşullandırma verilerini değiştirir. Seçilen yöntemi koşullandırma girişine ekler ve bu, sonraki üretim adımlarında referans latentlerin nasıl işleneceğini etkiler. Bu düğüm deneysel olarak işaretlenmiştir ve Flux koşullandırma sisteminin bir parçasıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | - | Referans latent yöntemi ile değiştirilecek koşullandırma verisi |
| `reference_latents_method` | STRING | Evet | `"offset"`<br>`"index"`<br>`"uxo/uno"` | Referans latent işleme için kullanılacak yöntem. "uxo" veya "uso" seçilirse, "uxo" olarak dönüştürülecektir |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Referans latent yöntemi uygulanmış değiştirilmiş koşullandırma verisi |