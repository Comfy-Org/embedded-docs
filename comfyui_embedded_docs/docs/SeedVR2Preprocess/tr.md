# SeedVR2 Girdisini Ön İşle

Bu düğüm, yeniden boyutlandırılmış bir görüntüyü SeedVR2 modeli için hazırlamak üzere dolgular. İşlem sırasında alfa kanalını kaldırır; alfa kanalı daha sonra eşlik eden Post-Process SeedVR2 Output düğümü tarafından orijinal yeniden boyutlandırılmış görüntü kullanılarak geri yüklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | İşlenecek yeniden boyutlandırılmış görüntü. | IMAGE | Evet | - |

Not: Girdi, tek bir görüntü veya bir kare dizisi olabilir (örneğin, bir videodan kareler). Kısa kenarı en az 2 piksel olmalıdır. İşlem sırasında alfa kanalı (varsa) kaldırılır, piksel değerleri [0, 1] aralığına sıkıştırılır ve genişlik ile yükseklik 16'nın katlarına dolgulanır. Kare dizileri, uzunlukları 1, 5, 9, 13, ... kare desenini izleyecek şekilde dolgulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | VAE kodlaması için dolgulanmış görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/tr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
