# MaskeÖnizleme

MaskPreview düğümü, maske verilerinin görsel bir önizlemesini çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde görüntüler. Bu, iş akışınızın herhangi bir noktasında tam maske değerlerini incelemenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `maske` | Önizlenecek maske verisi | MASK | Evet | - |
| `filename_prefix` | Önizleme dosya adı için ön ek (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `prompt` | Meta veriler için prompt bilgisi (otomatik sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Meta veriler için ek PNG bilgisi (otomatik sağlanır) | EXTRA_PNGINFO | Hayır | - |

`prompt` ve `extra_pnginfo` girdileri gizlidir ve ComfyUI sistemi tarafından otomatik olarak sağlanır; bunları elle bağlamanız gerekmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mask` | Önizlenen maske verisi, iş akışında daha fazla kullanılmak üzere değiştirilmeden döndürülür | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
