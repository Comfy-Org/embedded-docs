# Google Gemini

Bu düğüm, kullanıcıların metin yanıtları oluşturmak için Google'ın Gemini AI modelleriyle etkileşime girmesini sağlar. Modelin daha alakalı ve anlamlı yanıtlar oluşturması için bağlam olarak metin, görsel, ses, video ve dosyalar dahil olmak üzere birden çok girdi türü sağlayabilirsiniz. Düğüm, tüm API iletişimini ve yanıt ayrıştırmayı otomatik olarak yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istek` | Modele verilen metin girdileri, bir yanıt oluşturmak için kullanılır. Modele ayrıntılı talimatlar, sorular veya bağlam ekleyebilirsiniz. Varsayılan: boş dize. | STRING | Evet | - |
| `model` | Yanıt oluşturmak için kullanılacak Gemini modeli. Varsayılan: gemini-3-1-pro. | COMBO | Evet | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak üzere elinden geleni yapar. Deterministik çıktı garanti edilmez. Ayrıca modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı seed değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. Varsayılan: 42. | INT | Evet | 0 - 18446744073709551615 |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Batch Images düğümünü kullanabilirsiniz. Varsayılan: Yok. | IMAGE | Hayır | - |
| `audio` | Model için bağlam olarak kullanılacak isteğe bağlı ses. Varsayılan: Yok. | AUDIO | Hayır | - |
| `video` | Model için bağlam olarak kullanılacak isteğe bağlı video. Varsayılan: Yok. | VIDEO | Hayır | - |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdileri kabul eder. Varsayılan: Yok. | GEMINI_INPUT_FILES | Hayır | - |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: boş dize. Bu gelişmiş bir parametredir. | STRING | Hayır | - |

Bağlanan tüm görseller bağlam olarak kullanılır. 10'dan fazla görsel sağlandığında, ilk 10 görsel dosya referansı olarak yüklenir ve kalan görseller API'ye satır içi (inline) olarak gönderilir.

Düğüm, listede verilen seçili model adını kullanır; bazı girdiler istek gönderilmeden önce dahili olarak geçerli API model tanımlayıcılarına eşlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Gemini modeli tarafından oluşturulan metin yanıtı. Model herhangi bir metin üretmezse, düğüm "Empty response from Gemini model..." döndürür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/tr.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
