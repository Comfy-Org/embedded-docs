> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/tr.md)

WanTrackToVideo düğümü, hareket izleme verilerini video dizilerine dönüştürür. İzleme noktalarını işleyerek karşılık gelen video kareleri oluşturur. İzleme koordinatlarını girdi olarak alır ve video üretimi için kullanılabilecek video koşullandırması ve gizli temsiller üretir. Hiçbir iz sağlanmadığında, standart görüntüden videoya dönüştürmeye geri döner.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimi için pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | Video üretimi için negatif koşullandırma |
| `vae` | VAE | Evet | - | Kodlama ve kod çözme için VAE modeli |
| `tracks` | STRING | Evet | - | Çok satırlı dize olarak JSON biçimli izleme verileri (varsayılan: "[]") |
| `width` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1'den MAX_RESOLUTION'a | Çıktı videosundaki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1'den 4096'ya | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `temperature` | FLOAT | Evet | 1.0'dan 1000.0'a | Hareket yama işlemi için sıcaklık parametresi (varsayılan: 220.0, adım: 0.1) |
| `topk` | INT | Evet | 1'den 10'a | Hareket yama işlemi için top-k değeri (varsayılan: 2) |
| `start_image` | IMAGE | Hayır | - | Video üretimi için başlangıç görüntüsü |
| `clip_vision_output` | CLIPVISIONOUTPUT | Hayır | - | Ek koşullandırma için CLIP görü çıktısı |

**Not:** `tracks` geçerli izleme verileri içerdiğinde, düğüm video üretmek için hareket izlerini işler. `tracks` boş olduğunda, standart görüntüden videoya moduna geçer. `start_image` sağlanmışsa, video dizisinin ilk karesini başlatır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Hareket iz bilgisi uygulanmış pozitif koşullandırma |
| `negative` | CONDITIONING | Hareket iz bilgisi uygulanmış negatif koşullandırma |
| `latent` | LATENT | Üretilen video gizli temsili |