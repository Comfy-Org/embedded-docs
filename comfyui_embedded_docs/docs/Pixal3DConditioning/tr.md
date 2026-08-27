# Pixal3DConditioning

Bu düğüm, Trellis2 3D üretim hattı için görüntü koşullandırması hazırlar. Giriş görüntüsünden DINOv3 görüş modeliyle iki çözünürlükte görsel özellikler çıkarır, bunları aşama başına özellik haritaları halinde düzenler (isteğe bağlı olarak bir NAF modeliyle geliştirilir) ve yatay görüş alanından türetilen kamera verileriyle birleştirir. Pozitif ve negatif bir koşullandırma çifti çıkarır; burada negatif, sınıflandırıcısız rehberlik için sıfırlanmış özellikler kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Evet | — |
| `image` | ImageCropToMask'tan ön işlenmiş görüntü (Pixal3D için pad_factor=1.1). | IMAGE | Evet | — |
| `camera_angle_x` | Derece cinsinden yatay görüş alanı (görünen ad: fov). Görüntü başına bir FoV için bir MoGeGeometryToFOV (axis='horizontal', unit='degrees') bağlayın (yukarı akış varsayılanıyla eşleşir). Varsayılan: 49.13. | FLOAT | Evet | 1.0 – 170.0 |

Not: `camera_angle_x` değeri dahili olarak radyana dönüştürülür ve projeksiyon dönüşüm matrisi için kamera mesafesini hesaplamak üzere kullanılır. Sağlanan görüş modeli bir NAF bileşeni içerdiğinde, düğüm ayrıca şekil ve doku aşamaları için yüksek çözünürlüklü özellik haritaları üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Trellis2 üretimi için görüntüden türetilmiş özellik haritalarını ve projeksiyon verilerini içeren pozitif koşullandırma. | CONDITIONING |
| `negative` | Sınıflandırıcısız rehberlik için kullanılan, sıfırlanmış özellik tensörlerine sahip negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
