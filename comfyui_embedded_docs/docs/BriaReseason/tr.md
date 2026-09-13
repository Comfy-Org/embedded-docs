# BriaReseason

Bu düğüm, Bria kullanarak bir görüntüyü farklı bir mevsime taşır. Tüm sahne yeniden işlendiğinden, manzara mevsimin kendisinin ötesinde de değişebilir. Bria tüm kareyi yaklaşık 1 megapiksel olarak yeniden işler, bu nedenle sonuç girdiyle piksel hizalı değildir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Başka bir mevsime taşınacak görüntü. Görüntü gönderilmeden önce varsa alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `mevsim` | Uygulanacak mevsim. | COMBO | Evet | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderasyon` | Moderasyon ayarları. İçerik moderasyonu seçeneklerinin bu istek için yapılandırılıp yapılandırılmayacağını seçer. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon Girdileri

Bu seçenekler `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde içerik moderasyonunu etkinleştirir (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünde içerik moderasyonunu etkinleştirir (varsayılan: false). | BOOLEAN | Hayır | true<br>false |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Seçilen mevsimde yeniden işlenmiş görüntü. | IMAGE |
| `structured_prompt` | Bria FIBO Image Edit ile sonraki bir düzenleme için düzenlenmiş görüntünün yapılandırılmış açıklaması. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/tr.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`
