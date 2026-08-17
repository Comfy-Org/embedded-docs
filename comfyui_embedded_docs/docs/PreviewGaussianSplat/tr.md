# Splat Önizleme

PreviewGaussianSplat düğümü, 3B gaussian splat dosyasını çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde önizlemenizi sağlar. Dosyayı geçici olarak bir geçici klasörde saklar, 3B önizleme penceresinde görüntüler ve model verilerini, kamera bilgilerini ve önizleme boyutunu diğer düğümlere iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir 3B gaussian splat dosyası. | FILE3D | Evet | splat, ply, spz, ksplat |
| `model_3d_info` | 3B model hakkında isteğe bağlı meta veri bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgilerini içeren 3B görünüm alanının geçerli durumu. | LOAD3D | Evet | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizleme görüntüsünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |
| `height` | Önizleme görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |

Not: `camera_info` veya `model_3d_info` sağlanmadığında, düğüm bunun yerine `viewport_state` içindeki ilgili değerleri kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Girdi olarak verilen 3B gaussian splat dosyası, değiştirilmeden geçirilir. | FILE3D |
| `model_3d_info` | 3B model hakkında, girdiden veya görünüm alanı durumundan alınan meta veri bilgisi. | LOAD3DMODELINFO |
| `camera_info` | Önizleme için, girdiden veya görünüm alanı durumundan alınan kamera bilgisi. | LOAD3DCAMERA |
| `width` | Önizleme görüntüsünün genişliği. | INT |
| `height` | Önizleme görüntüsünün yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
