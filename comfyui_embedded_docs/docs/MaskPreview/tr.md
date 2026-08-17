# MaskeÖnizleme

The MaskPreview düğümü, maske verilerinin görsel bir önizlemesini doğrudan ComfyUI arayüzünde gösterir; böylece iş akışınız sırasında maskeleri inceleyebilirsiniz. Önizlemeyi ComfyUI çıktı dizinine kaydetmeden gösterir ve maskeyi çıktı olarak geçirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mask` | Önizlenecek maske verisi | MASK | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `prompt` | Metadata için prompt bilgisi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Metadata için ek PNG bilgisi (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mask` | Önizlenen maske verisi, değiştirilmeden geçirilir | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
