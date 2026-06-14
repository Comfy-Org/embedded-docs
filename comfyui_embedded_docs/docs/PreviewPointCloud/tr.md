# Nokta Bulutunu Önizle

Nokta Bulutunu Önizle düğümü, ComfyUI arayüzü içinde bir 3B nokta bulutu dosyasını görüntülemenizi sağlar. Nokta bulutunu geçici bir dosyaya kaydeder ve bir 3B önizleme penceresinde görüntüler; model verilerini ve görüntü alanı ayarlarını daha sonraki işlemler için iletir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D | Evet | - |
| `model_3d_info` | 3B model hakkında bilgi | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Geçerli görüntü alanı durumu | LOAD3D | Evet | - |
| `camera_info` | 3B görünüm için kamera bilgisi | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme penceresi genişliği (varsayılan: 1024) | INT | Evet | 1 ila 4096 |
| `yükseklik` | Önizleme penceresi yüksekliği (varsayılan: 1024) | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_3d_info` | Nokta bulutu model verisi | FILE3D |
| `camera_info` | 3B model hakkında bilgi | LOAD3DMODELINFO |
| `genişlik` | 3B görünüm için kamera bilgisi | LOAD3DCAMERA |
| `yükseklik` | Önizleme penceresi genişliği | INT |
| `yükseklik` | Önizleme penceresi yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `f3121511841d1962aad881c0ac5b93f24842bf4810e84fe241330e9eab90334a`
