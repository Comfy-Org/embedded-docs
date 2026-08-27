# Splat Önizleme

PreviewGaussianSplat düğümü, bir 3D gaussian splat dosyasını ComfyUI çıktı dizinine kaydetmeden bir önizleme penceresinde görüntüler. Çeşitli gaussian splat formatlarındaki bir 3D model dosyasını kabul eder, önizleme için geçici bir kopya kaydeder ve model verilerini iş akışında daha fazla işlenmek üzere iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir gaussian splat 3D dosyası. | FILE3D | Evet | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 3D model hakkında isteğe bağlı meta veri bilgileri. Bağlı olmadığında, düğüm `viewport_state` içindeki model bilgisini kullanır. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgileri dahil olmak üzere 3D görünüm alanının geçerli durumu. | LOAD3D | Evet | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgileri. Bağlı olmadığında, düğüm `viewport_state` içindeki kamera bilgisini kullanır. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme görüntüsünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |
| `yükseklik` | Önizleme görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |

Not: `camera_info` veya `model_3d_info` sağlanmadığında, düğüm `viewport_state` içinde saklanan kamera ve model bilgilerini kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Değiştirilmeden iletilen girdi 3D gaussian splat dosyası. | FILE3D |
| `model_3d_info` | Girdiden veya görünüm alanı durumundan türetilen 3D model hakkında meta veri bilgileri. | LOAD3DMODELINFO |
| `camera_info` | Girdiden veya görünüm alanı durumundan türetilen önizleme için kamera bilgileri. | LOAD3DCAMERA |
| `genişlik` | Önizleme görüntüsünün genişliği. | INT |
| `yükseklik` | Önizleme görüntüsünün yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
