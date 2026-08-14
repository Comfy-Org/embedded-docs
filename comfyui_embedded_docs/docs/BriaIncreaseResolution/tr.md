# BriaIncreaseResolution

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Büyütülecek girdi görüntüsü. | IMAGE | Evet | Single image |
| `desired_increase` | Çözünürlük çarpanı. Çıktı, her kenarda 8192 piksel sınırına uymalıdır. | COMBO | Evet | "2"<br>"4" |
| `auto_downscale` | Çıktı sınırı aşacağında, çarpanı otomatik olarak düşürün ve hâlâ yeterli değilse girdi görüntüsünü küçültün. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `moderation` | Moderasyon ayarları. "true" olarak ayarlandığında, her ikisi de False varsayılanına sahip `visual_input_moderation` ve `visual_output_moderation` alt seçeneklerini etkinleştirir. | COMBO | Evet | "false"<br>"true" |

Notlar:
- Düğüm, maksimum 8192 piksellik bir çıktı kenarı uygular. Seçilen çarpan bu sınırı aşarsa ve `auto_downscale` devre dışıysa, bir hata oluşturulur. `auto_downscale` özelliğini etkinleştirmek, düğümün otomatik olarak daha düşük bir çarpan kullanmasına veya girdi görüntüsünü küçültmesine olanak tanır.
- Bria, büyütmeden önce girdi görüntüsünün kısa kenarını en az 224 piksele büyütür. Çok uzun olan görüntüler, onları daha kare bir şekle kırpmayı isteyen bir hatayı tetikleyebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria API tarafından döndürülen büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/tr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
