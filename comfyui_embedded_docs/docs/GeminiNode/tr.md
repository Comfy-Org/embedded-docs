> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/tr.md)

Bu düğüm, kullanıcıların Google'ın Gemini AI modelleriyle etkileşime girerek metin yanıtları oluşturmasını sağlar. Modelin daha alakalı ve anlamlı yanıtlar üretmesi için bağlam olarak metin, görsel, ses, video ve dosyalar dahil olmak üzere birden fazla girdi türü sağlayabilirsiniz. Düğüm, tüm API iletişimini ve yanıt ayrıştırmayı otomatik olarak gerçekleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Modele yapılan metin girdileri, yanıt oluşturmak için kullanılır. Modele ayrıntılı talimatlar, sorular veya bağlam ekleyebilirsiniz. Varsayılan: boş dize. |
| `model` | COMBO | Evet | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` | Yanıtları oluşturmak için kullanılacak Gemini modeli. Varsayılan: gemini-3-1-pro. |
| `seed` | INT | Evet | 0 - 18446744073709551615 | Tohum belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak üzere en iyi çabayı gösterir. Belirleyici çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. Varsayılan: 42. |
| `images` | IMAGE | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Toplu Görseller düğümünü kullanabilirsiniz. Varsayılan: Yok. |
| `audio` | AUDIO | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı ses. Varsayılan: Yok. |
| `video` | VIDEO | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı video. Varsayılan: Yok. |
| `files` | GEMINI_INPUT_FILES | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini İçerik Girdi Dosyaları Oluştur düğümünden girdi kabul eder. Varsayılan: Yok. |
| `system_prompt` | STRING | Hayır | - | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: boş dize. Bu bir gelişmiş parametredir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `STRING` | STRING | Gemini modeli tarafından oluşturulan metin yanıtı. |

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
