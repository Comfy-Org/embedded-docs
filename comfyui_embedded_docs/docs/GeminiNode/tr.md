> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/tr.md)

Bu düğüm, kullanıcıların Google'ın Gemini AI modelleriyle etkileşime girerek metin yanıtları oluşturmasına olanak tanır. Modelin daha alakalı ve anlamlı yanıtlar üretmesi için bağlam olarak metin, resim, ses, video ve dosya gibi birden fazla girdi türü sağlayabilirsiniz. Düğüm, tüm API iletişimini ve yanıt ayrıştırmasını otomatik olarak halleder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Model için metin girdileri, bir yanıt oluşturmak için kullanılır. Model için ayrıntılı talimatlar, sorular veya bağlam bilgisi ekleyebilirsiniz. Varsayılan: boş dize. |
| `model` | COMBO | Evet | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | Yanıt oluşturmak için kullanılacak Gemini modeli. Varsayılan: gemini-2.5-pro. |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak için elinden geleni yapar. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı seed değerini kullansanız bile yanıtta değişikliklere neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. Varsayılan: 42. |
| `images` | IMAGE | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı resim(ler). Birden fazla resim eklemek için Batch Images düğümünü kullanabilirsiniz. Varsayılan: Yok. |
| `audio` | AUDIO | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı ses. Varsayılan: Yok. |
| `video` | VIDEO | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı video. Varsayılan: Yok. |
| `files` | GEMINI_INPUT_FILES | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden gelen girdileri kabul eder. Varsayılan: Yok. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `STRING` | STRING | Gemini modeli tarafından oluşturulan metin yanıtı. |