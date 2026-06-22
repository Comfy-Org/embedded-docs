# Splat Önizleme

PreviewGaussianSplat düğümü, ComfyUI arayüzü içinde bir 3D gaussian splat dosyasını önizlemenizi sağlar. Çeşitli gaussian splat formatlarındaki bir 3D model dosyasını kabul eder ve bunu bir 3D önizleme penceresinde görüntüler, model verilerini daha sonraki işlemler için geçirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `model_3d` | Bir gaussian splat 3D dosyası. | FILE3D | Evet | Desteklenen formatlar: splat, ply, spz, ksplat |
| `model_3d_info` | 3D model hakkında isteğe bağlı meta veri bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgisi dahil olmak üzere 3D görünüm alanının mevcut durumu. | LOAD3D | Evet | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme görüntüsünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |
| `yükseklik` | Önizleme görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 ile 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_3d_info` | Giriş 3D gaussian splat dosyası, değiştirilmeden geçirilir. | FILE3D |
| `camera_info` | Girişten veya görünüm alanı durumundan türetilen 3D model hakkında meta veri bilgisi. | LOAD3DMODELINFO |
| `genişlik` | Girişten veya görünüm alanı durumundan türetilen önizleme için kamera bilgisi. | LOAD3DCAMERA |
| `yükseklik` | Önizleme görüntüsünün genişliği. | INT |
| `yükseklik` | Önizleme görüntüsünün yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `7b79e9ab25858e7db6e999313cc11226895aeb4d7fee414f56f0d5fd2363b485`
