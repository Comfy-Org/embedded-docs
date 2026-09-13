# Splat Önizleme

PreviewGaussianSplat düğümü, bir 3D gaussian splat dosyasını ComfyUI çıktı dizinine kaydetmeden bir önizleme penceresinde görüntüler. Çeşitli gaussian splat biçimlerindeki bir 3D model dosyasını kabul eder, önizleme için geçici bir kopya kaydeder ve model verilerini iş akışında daha ileri işleme için geçirir. Bu düğüm deneysel olarak işaretlenmiştir ve bir çıktı düğümü olarak işlev görür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir gaussian splat 3D dosyası. | FILE3D | Evet | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 3D model hakkında isteğe bağlı meta veri bilgisi. Bağlı olmadığında, düğüm `viewport_state` içindeki model bilgisini kullanır. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgileri dahil olmak üzere 3D görüntü alanının geçerli durumu. | LOAD3D | Evet | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgisi. Bağlı olmadığında, düğüm `viewport_state` içindeki kamera bilgisini kullanır. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme render'ının piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |
| `yükseklik` | Önizleme render'ının piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |

Not: `camera_info` veya `model_3d_info` sağlanmadığında, düğüm `viewport_state` içinde saklanan kamera ve model bilgilerine geri döner. `viewport_state` geçerli bir görüntü alanı durumu nesnesi değilse, boş olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Girdi 3D gaussian splat dosyası, değiştirilmeden geçirilir. | FILE3D |
| `model_3d_info` | 3D model hakkında meta veri bilgisi; ya girdiden alınır ya da görüntü alanı durumundan türetilir. | LOAD3DMODELINFO |
| `camera_info` | Önizleme için kamera bilgisi; ya girdiden alınır ya da görüntü alanı durumundan türetilir. | LOAD3DCAMERA |
| `width` | Önizleme render'ının genişliği. | INT |
| `height` | Önizleme render'ının yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
