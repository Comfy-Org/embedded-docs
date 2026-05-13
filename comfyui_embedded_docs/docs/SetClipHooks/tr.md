> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/tr.md)

SetClipHooks düğümü, bir CLIP modeline özel kancalar (hooks) uygulamanıza olanak tanıyarak davranışında gelişmiş değişiklikler yapılmasını sağlar. Koşullandırma çıktılarına kancalar uygulayabilir ve isteğe bağlı olarak clip zamanlama işlevselliğini etkinleştirebilir. Bu düğüm, belirtilen kanca yapılandırmaları uygulanmış şekilde giriş CLIP modelinin klonlanmış bir kopyasını oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `clip` | CLIP | Evet | - | Kanca uygulanacak CLIP modeli |
| `koşullara_uygula` | BOOLEAN | Evet | - | Koşullandırma çıktılarına kanca uygulanıp uygulanmayacağı (varsayılan: True) |
| `zamanlama_klibi` | BOOLEAN | Evet | - | Clip zamanlamasının etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |
| `kancalar` | HOOKS | Hayır | - | CLIP modeline uygulanacak isteğe bağlı kanca grubu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `clip` | CLIP | Belirtilen kancalar uygulanmış klonlanmış bir CLIP modeli |

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`
