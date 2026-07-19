# SavePointCloud

Save Point Cloud düğümü, 3B nokta bulutu dosyasını çıktı dizinine kaydeder ve isteğe bağlı olarak 3B görüntüleyici için önizleme verisi sağlar. Dosya adlandırma ve kaydetme işlemlerini yönetirken, görüntüleme amacıyla kamera ve model bilgilerini de iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D_POINT_CLOUD_ANY veya FILE3D_PLY | Evet | - |
| `filename_prefix` | Kaydedilen dosya adı için ön ek (varsayılan: "3d/ComfyUI") | STRING | Evet | - |
| `viewport_state` | Kamera ve model bilgilerini içeren mevcut görünüm alanı durumu | LOAD3D | Evet | - |
| `model_3d_info` | 3B görüntüleyici için ek model bilgisi | LOAD3D_MODEL_INFO | Hayır | - |
| `camera_info` | 3B görüntüleyici için kamera bilgisi | LOAD3D_CAMERA | Hayır | - |
| `width` | Önizleme ekranının piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 1 ila 4096 |
| `height` | Önizleme ekranının piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Kaydedilen nokta bulutu dosyası | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | 3B görüntüleyici için model bilgisi | LOAD3D_MODEL_INFO |
| `camera_info` | 3B görüntüleyici için kamera bilgisi | LOAD3D_CAMERA |
| `width` | Önizleme ekranının genişliği | INT |
| `height` | Önizleme ekranının yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
