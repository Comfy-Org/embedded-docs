> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

**Maske Önizleme Düğümü**

Maske Önizleme düğümü, maske verilerini ComfyUI çıktı dizininize önizleme görüntüsü olarak kaydederek iş akışı yürütmesi sırasında maske verilerini görsel olarak incelemenizi sağlar. Giriş maskesini görüntü görüntüleme için uygun bir formata dönüştürür ve yapılandırılabilir bir dosya adı ön ekiyle kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `maske` | MASK | Evet | - | Önizlenecek ve görüntü olarak kaydedilecek maske verileri |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "ComfyUI") |
| `prompt` | PROMPT | Hayır | - | Meta veriler için istem bilgisi (otomatik olarak sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Meta veriler için ek PNG bilgisi (otomatik olarak sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ui` | DICT | Kullanıcı arayüzünde görüntülenmek üzere önizleme görüntüsü bilgilerini ve meta verilerini içerir |

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
