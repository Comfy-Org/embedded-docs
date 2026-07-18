# SavePointCloud

Save Point Cloud (Nokta Bulutunu Kaydet) düğümü, 3B nokta bulutu dosyasını ComfyUI çıktı dizininize kaydeder. Ayrıca nokta bulutu verilerini ve isteğe bağlı kamera ile model bilgilerini, iş akışınızdaki diğer düğümler tarafından kullanılmak üzere iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D | Evet | - |
| `filename_prefix` | Kaydedilen dosya adı için ön ek (varsayılan: "3d/ComfyUI") | STRING | Evet | - |
| `viewport_state` | Bir 3B görüntü alanı düğümünden gelen durum | LOAD3D | Evet | - |
| `model_3d_info` | Gelişmiş kullanım için isteğe bağlı 3B model bilgisi | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Gelişmiş kullanım için isteğe bağlı kamera bilgisi | LOAD3DCAMERA | Hayır | - |
| `width` | Önizleme görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | min: 1, maks: 4096, adım: 1 |
| `height` | Önizleme görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | min: 1, maks: 4096, adım: 1 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Kaydedilen nokta bulutu dosyası | FILE3D |
| `model_3d_info` | 3B model hakkında bilgi | LOAD3DMODELINFO |
| `camera_info` | Görüntü alanı için kamera bilgisi | LOAD3DCAMERA |
| `width` | Önizleme görüntüsünün genişliği | INT |
| `height` | Önizleme görüntüsünün yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
