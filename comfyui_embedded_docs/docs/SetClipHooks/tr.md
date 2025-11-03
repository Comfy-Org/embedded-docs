> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/tr.md)

SetClipHooks düğümü, bir CLIP modeline özel kancalar uygulamanıza olanak tanıyarak, modelin davranışında gelişmiş değişiklikler yapabilmenizi sağlar. Koşullandırma çıktılarına kancalar uygulayabilir ve isteğe bağlı olarak clip zamanlama işlevselliğini etkinleştirebilir. Bu düğüm, girdi olarak verilen CLIP modelinin belirtilen kanca yapılandırmaları uygulanmış klonlanmış bir kopyasını oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Kanca uygulanacak CLIP modeli |
| `koşullara_uygula` | BOOLEAN | Evet | - | Koşullandırma çıktılarına kancaların uygulanıp uygulanmayacağı (varsayılan: True) |
| `zamanlama_klibi` | BOOLEAN | Evet | - | Clip zamanlamanın etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |
| `kancalar` | HOOKS | Hayır | - | CLIP modeline uygulanacak isteğe bağlı kanca grubu |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | Belirtilen kancalar uygulanmış klonlanmış bir CLIP modeli |