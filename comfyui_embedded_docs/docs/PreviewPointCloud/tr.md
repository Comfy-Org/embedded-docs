# Nokta Bulutu Önizleme

Preview Point Cloud düğümü, bir 3B nokta bulutu dosyasını (.ply dosyası gibi) çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde görüntülemenizi sağlar. Düğüm, nokta bulutunu geçici bir dosyaya yazar, 3B önizleme penceresinde görüntüler ve model verilerini, model bilgilerini, kamera bilgilerini, genişliği ve yüksekliği daha sonraki işlemler için iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D | Evet | - |
| `model_3d_info` | 3B model hakkında bilgi. Gelişmiş girdi. Bağlı olmadığında, `viewport_state` içinde saklanan değer kullanılır. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Geçerli görünüm alanı durumu; önizleme için kullanılan kamera bilgilerini ve model bilgilerini içerebilir. | LOAD3D | Evet | - |
| `camera_info` | 3B görünüm için kamera bilgisi. Gelişmiş girdi. Bağlı olmadığında, `viewport_state` içinde saklanan değer kullanılır. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizleme penceresinin piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |
| `height` | Önizleme penceresinin piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |

Not: `camera_info` veya `model_3d_info` bağlı olmadığında, düğüm `viewport_state` içinde saklanan değerleri kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Nokta bulutu model verisi, değiştirilmeden iletilir. | FILE3D |
| `model_3d_info` | Önizleme için kullanılan 3B model hakkında bilgi. | LOAD3DMODELINFO |
| `camera_info` | 3B görünüm için kullanılan kamera bilgisi. | LOAD3DCAMERA |
| `width` | Önizleme penceresinin genişliği. | INT |
| `height` | Önizleme penceresinin yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
