# BriaIncreaseResolution

Bria Increase Resolution, Bria'nın görüntü büyütme hizmetini kullanarak bir girdi görüntüsünü 2 kat veya 4 kat büyütür ve orijinal içeriği korur. Görüntüyü yükler, Bria hizmetinde işler ve büyütülmüş sonucu bir görüntü olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Büyütülecek girdi görüntüsü. | IMAGE | Evet | Tek görüntü |
| `desired_increase` | Çözünürlük çarpanı. Çıktının her bir kenarı 8192 pikseli aşmamalıdır. | COMBO | Evet | "2"<br>"4" |
| `auto_downscale` | Çıktı sınırı aşacağında çarpanı otomatik olarak düşürür; bu hâlâ yeterli olmazsa girdi görüntüsünü küçültür. (varsayılan: False) | BOOLEAN | Evet | True<br>False |
| `moderation` | Moderasyon ayarları. "true" olarak ayarlandığında, `visual_input_moderation` ve `visual_output_moderation` alt seçeneklerini etkinleştirir; her ikisi de varsayılan olarak False'tur. | DYNAMIC_COMBO | Evet | "false"<br>"true" |

Notlar:
- `moderation` "true" olarak ayarlandığında, `visual_input_moderation` ve `visual_output_moderation` alt seçenekleri kullanılabilir hale gelir ve her ikisi de varsayılan olarak False'tur. Bu seçenekler, girdi görüntüsünün ve çıktı görüntüsü içeriğinin moderasyonunu kontrol eder.
- Düğüm, çıktının maksimum kenar uzunluğunu 8192 piksel olarak zorunlu kılar. Seçilen çarpan bu sınırı aşarsa ve `auto_downscale` devre dışıysa bir hata oluşturulur. `auto_downscale` seçeneğinin etkinleştirilmesi, düğümün bunun yerine otomatik olarak daha düşük bir çarpan kullanmasına veya girdi görüntüsünü küçültmesine olanak tanır.
- Bria, büyütmeden önce girdi görüntüsünün kısa kenarını en az 224 piksele kadar büyütür. Aşırı uzun görüntüler, daha kare bir şekle kırpılmalarını isteyen bir hataya neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria API tarafından döndürülen büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/tr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
