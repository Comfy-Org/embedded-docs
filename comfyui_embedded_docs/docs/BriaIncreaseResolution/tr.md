# Bria Çözünürlüğünü Artır

Bria Increase Resolution, Bria'nın görüntü yükseltme hizmetini kullanarak bir girdi görüntüsünü orijinal içeriği koruyarak 2x veya 4x ölçeklendirir. Düğüm, görüntüyü yükler, işlenmek üzere Bria hizmetine gönderir, sonucu bekler ve yükseltilmiş görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Yükseltilecek girdi görüntüsü. | IMAGE | Evet | Tek görüntü |
| `desired_increase` | Çözünürlük çarpanı. Çıktı, her bir kenarda 8192 piksel içinde kalmalıdır. | COMBO | Evet | "2"<br>"4" |
| `auto_downscale` | Çıktı sınırı aşacaksa çarpanı otomatik olarak düşürür ve bu hâlâ yeterli değilse girdi görüntüsünü küçültür. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `moderation` | Moderasyon ayarları. "true" olarak ayarlandığında, `visual_input_moderation` ve `visual_output_moderation` alt seçeneklerini etkinleştirir; her ikisinin varsayılanı da False'dur. | DYNAMIC_COMBO | Evet | "false"<br>"true" |

Notlar:
- `moderation` "true" olarak ayarlandığında, `visual_input_moderation` ve `visual_output_moderation` alt seçenekleri kullanılabilir hale gelir; her ikisinin varsayılanı da False'dur. Bunlar, girdi görüntüsünün ve çıktı görüntüsü içeriğinin moderasyonunu kontrol eder.
- Düğüm, çıktının her bir kenarı için maksimum 8192 piksel sınırı uygular. Seçilen çarpan bu sınırı aşacaksa ve `auto_downscale` devre dışıysa, bir hata oluşturulur. `auto_downscale` etkinleştirildiğinde, düğümün otomatik olarak daha düşük bir çarpan kullanmasına veya bunun yerine girdi görüntüsünü küçültmesine olanak tanır.
- Bria, yükseltme işleminden önce girdi görüntüsünün kısa kenarını en az 224 piksele genişletir. Aşırı uzun görüntüler, daha kare bir şekle kırpılmalarını isteyen bir hataya neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria hizmeti tarafından döndürülen yükseltilmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/tr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
