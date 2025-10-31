> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/tr.md)

HunyuanImageToVideo düğümü, Hunyuan video modelini kullanarak görüntüleri video gizli temsillerine dönüştürür. Video oluşturma modelleri tarafından daha fazla işlenebilecek video gizli temsilleri oluşturmak için koşullandırma girdilerini ve isteğe bağlı başlangıç görüntülerini alır. Düğüm, başlangıç görüntüsünün video oluşturma sürecini nasıl etkilediğini kontrol etmek için farklı rehberlik türlerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, adım: 16) |
| `height` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1'den MAX_RESOLUTION'a | Çıktı videosundaki kare sayısı (varsayılan: 53, adım: 4) |
| `batch_size` | INT | Evet | 1'den 4096'ya | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `guidance_type` | COMBO | Evet | "v1 (birleştir)"<br>"v2 (değiştir)"<br>"özel" | Başlangıç görüntüsünü video oluşturmaya dahil etme yöntemi |
| `start_image` | IMAGE | Hayır | - | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü |

**Not:** `start_image` sağlandığında, düğüm seçilen `guidance_type`'a göre farklı rehberlik yöntemleri kullanır:

- "v1 (birleştir)": Görüntü gizli temsilini video gizli temsili ile birleştirir
- "v2 (değiştir)": İlk video karelerini görüntü gizli temsili ile değiştirir
- "özel": Görüntüyü rehberlik için referans gizli temsili olarak kullanır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | start_image sağlandığında görüntü rehberliği uygulanmış değiştirilmiş pozitif koşullandırma |
| `latent` | LATENT | Video oluşturma modelleri tarafından daha fazla işlenmeye hazır video gizli temsili |