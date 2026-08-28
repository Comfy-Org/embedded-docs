# Nokta Bulutu Önizleme

Preview Point Cloud düğümü, bir 3B nokta bulutu dosyasını ComfyUI çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde görüntülemenizi sağlar. Nokta bulutunu geçici bir konuma kaydeder ve 3B önizleme penceresinde görüntüler; ayrıca model verilerini, kamera bilgilerini ve görünüm alanı durumunu daha sonraki işlemler için iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D | Evet | - |
| `model_3d_info` | 3B model hakkında bilgi | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Geçerli görünüm alanı durumu | LOAD3D | Evet | - |
| `camera_info` | 3B görünüm için kamera bilgisi | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme penceresinin genişliği (varsayılan: 1024) | INT | Evet | 1 ile 4096 |
| `yükseklik` | Önizleme penceresinin yüksekliği (varsayılan: 1024) | INT | Evet | 1 ile 4096 |

Not: `camera_info` veya `model_3d_info` bağlı olmadığında, düğüm `viewport_state` içinde saklanan karşılık gelen değerlere geri döner. Nokta bulutu dosyası ComfyUI'nin geçici dizinine kaydedilir ve çıktı dizinine yazılmaz. Bu bir çıktı düğümüdür, bu nedenle öncelikle önizleme sonucunu arayüzde görüntülemek için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Nokta bulutu modeli verileri | FILE3D |
| `model_3d_info` | 3B model hakkında bilgi | LOAD3DMODELINFO |
| `camera_info` | 3B görünüm için kamera bilgisi | LOAD3DCAMERA |
| `genişlik` | Önizleme penceresinin genişliği | INT |
| `yükseklik` | Önizleme penceresinin yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
