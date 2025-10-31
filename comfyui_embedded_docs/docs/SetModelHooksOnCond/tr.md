> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/tr.md)

Bu düğüm, özel kancaları koşullandırma verilerine ekleyerek model yürütme sırasında koşullandırma sürecini kesmenize ve değiştirmenize olanak tanır. Bir dizi kancayı alır ve bunları sağlanan koşullandırma verilerine uygulayarak, metinden görüntü oluşturma iş akışının gelişmiş özelleştirilmesini sağlar. Eklenen kancalarla değiştirilen koşullandırma, sonraki işlem adımlarında kullanılmak üzere döndürülür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | - | Kancaların ekleneceği koşullandırma verisi |
| `hooks` | HOOKS | Evet | - | Koşullandırma verisine uygulanacak kanca tanımları |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Kancalar eklenmiş şekilde değiştirilmiş koşullandırma verisi |