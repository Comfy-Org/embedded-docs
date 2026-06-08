Bu düğüm, kullanıcıların Google'ın Gemini AI modelleriyle etkileşime girerek metin yanıtları oluşturmasını sağlar. Modelin daha alakalı ve anlamlı yanıtlar üretmesi için bağlam olarak metin, görsel, ses, video ve dosyalar dahil olmak üzere birden fazla girdi türü sağlayabilirsiniz. Düğüm, tüm API iletişimini ve yanıt ayrıştırmayı otomatik olarak gerçekleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istek` | Modele yapılan metin girdileri, yanıt oluşturmak için kullanılır. Modele ayrıntılı talimatlar, sorular veya bağlam ekleyebilirsiniz. Varsayılan: boş dize. | STRING | Evet | - |
| `model` | Yanıtları oluşturmak için kullanılacak Gemini modeli. Varsayılan: gemini-3-1-pro. | COMBO | Evet | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` |
| `seed` | Tohum belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak üzere en iyi çabayı gösterir. Belirleyici çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. Varsayılan: 42. | INT | Evet | 0 - 18446744073709551615 |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Toplu Görseller düğümünü kullanabilirsiniz. Varsayılan: Yok. | IMAGE | Hayır | - |
| `audio` | Model için bağlam olarak kullanılacak isteğe bağlı ses. Varsayılan: Yok. | AUDIO | Hayır | - |
| `video` | Model için bağlam olarak kullanılacak isteğe bağlı video. Varsayılan: Yok. | VIDEO | Hayır | - |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini İçerik Girdi Dosyaları Oluştur düğümünden girdi kabul eder. Varsayılan: Yok. | GEMINI_INPUT_FILES | Hayır | - |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: boş dize. Bu bir gelişmiş parametredir. | STRING | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `STRING` | Gemini modeli tarafından oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/tr.md)

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
