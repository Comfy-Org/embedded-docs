# MaskeÖnizleme

**Maske Önizleme Düğümü**

Maske Önizleme düğümü, maske verilerini ComfyUI çıktı dizininize önizleme görüntüsü olarak kaydederek iş akışı yürütmesi sırasında maske verilerini görsel olarak incelemenizi sağlar. Giriş maskesini görüntü görüntüleme için uygun bir formata dönüştürür ve yapılandırılabilir bir dosya adı ön ekiyle kaydeder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `maske` | Önizlenecek ve görüntü olarak kaydedilecek maske verileri | MASK | Evet | - |
| `filename_prefix` | Çıktı dosya adı için ön ek (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `prompt` | Meta veriler için istem bilgisi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Meta veriler için ek PNG bilgisi (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui` | Kullanıcı arayüzünde görüntülenmek üzere önizleme görüntüsü bilgilerini ve meta verilerini içerir | DICT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
