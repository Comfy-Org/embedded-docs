# Pixal3DConditioning

Pixal3DConditioning düğümü, Trellis2 3D üretim hattı için görüntü koşullandırmayı hazırlar. Girdi görüntüsünden iki çözünürlükte (512 ve 1024) görsel özellikler çıkarmak için bir DINOv3 görü modeli kullanır ve ardından bunları isteğe bağlı olarak bir NAF modeliyle iyileştirilebilen aşama başına özellik haritaları halinde düzenler. Kamera bilgisi, projeksiyon dönüşüm matrisini oluşturmak için yatay görüş alanından türetilir ve düğüm, sınıflandırıcıdan bağımsız yönlendirme için bir pozitif koşullandırma çifti (görüntüden türetilen özellikler artı projeksiyon verileri) ve bir negatif koşullandırma çifti (sıfırlanmış özellik tensörleri) üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Evet | — |
| `görüntü` | ImageCropToMask'ten gelen ön işlenmiş görüntü (Pixal3D için pad_factor=1.1). | IMAGE | Evet | — |
| `camera_angle_x` | Yatay FOV, derece cinsinden (`fov` olarak görüntülenir). Görüntü başına FoV için bir MoGeGeometryToFOV (axis='horizontal', unit='degrees') bağlayın (üst kaynak varsayılanıyla eşleşir). Varsayılan: 49.13. | FLOAT | Evet | 1.0 – 170.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Trellis2 üretimi için görüntüden türetilen özellik haritalarını ve projeksiyon verilerini içeren pozitif koşullandırma çıktısı. | CONDITIONING |
| `negative` | Sınıflandırıcıdan bağımsız yönlendirme için kullanılan, sıfırlanmış özellik tensörlerine sahip negatif koşullandırma çıktısı. | CONDITIONING |

Not: `camera_angle_x` değeri dahili olarak dereceden radyana dönüştürülür ve projeksiyon dönüşüm matrisini oluşturmak için bundan kamera mesafesi hesaplanır. Sağlanan görü modeli bir NAF bileşeni içeriyorsa, düğüm şekil ve doku aşamaları için yüksek çözünürlüklü özellik haritaları da üretir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
