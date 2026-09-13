# MaskeÖnizleme

MaskPreview düğümü, maske verisinin görsel bir önizlemesini doğrudan ComfyUI arayüzünde gösterir; bunu çıktı dizinine kaydetmez. Bu, iş akışınızın herhangi bir noktasında maskeyi incelemenizi sağlarken, maske de düğümden değişmeden geçer ve aşağı akışta kullanılmaya devam edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `maske` | Önizlenecek maske verisi | MASK | Evet | - |
| `filename_prefix` | Önizleme için kullanılan dosya adı öneki (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `prompt` | Meta veriler için istem bilgisi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Meta veriler için ek PNG bilgisi (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

Bağlanması gereken görünür tek girdi `mask`'tir. `filename_prefix`, `prompt` ve `extra_pnginfo` parametreleri sistem tarafından sağlanır: `filename_prefix` varsayılan değerini kullanır; `prompt` ve `extra_pnginfo` ise gizlidir ve ComfyUI çalışma zamanı tarafından otomatik olarak sağlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mask` | Önizlenen aynı maske verisi; iş akışında başka bir yerde kullanılabilmesi için değiştirilmeden döndürülür | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
