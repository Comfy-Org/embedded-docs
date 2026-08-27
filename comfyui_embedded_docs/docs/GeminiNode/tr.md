# Google Gemini

Bu düğüm, kullanıcıların metin yanıtları oluşturmak için Google'ın Gemini AI modelleriyle etkileşime girmesini sağlar. Modele bağlam olarak metin, görüntü, ses, video ve dosyalar dahil olmak üzere birden fazla girdi türü sağlayabilirsiniz; böylece model daha alakalı ve anlamlı yanıtlar üretebilir. Düğüm, tüm API iletişimini ve yanıt ayrıştırmayı otomatik olarak yönetir.

**Not:** Bu düğüm, kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istek` | Modele yapılan metin girdileri; yanıt oluşturmak için kullanılır. Modele ayrıntılı talimatlar, sorular veya bağlam ekleyebilirsiniz. Varsayılan: boş dize. | STRING | Evet | - |
| `model` | Yanıt oluşturmak için kullanılacak Gemini modeli. Varsayılan: gemini-3-1-pro. | COMBO | Evet | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamaya çalışır. Belirleyici çıktı garanti edilmez. Ayrıca, model veya sıcaklık gibi parametre ayarlarının değiştirilmesi, aynı seed değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. Varsayılan: 42. | INT | Evet | 0 ile 18446744073709551615 |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). Birden fazla görüntü eklemek için Batch Images düğümünü kullanabilirsiniz. Varsayılan: Yok. | IMAGE | Hayır | - |
| `audio` | Model için bağlam olarak kullanılacak isteğe bağlı ses. Varsayılan: Yok. | AUDIO | Hayır | - |
| `video` | Model için bağlam olarak kullanılacak isteğe bağlı video. Varsayılan: Yok. | VIDEO | Hayır | - |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. Varsayılan: Yok. | GEMINI_INPUT_FILES | Hayır | - |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan: boş dize. Bu bir gelişmiş parametredir. | STRING | Hayır | - |

Bağlı tüm görüntüler bağlam olarak kullanılır. 10'dan fazla görüntü sağlandığında, ilk 10'u dosya referansı olarak yüklenir ve geri kalan görüntüler API'ye satır içi olarak gönderilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Gemini modeli tarafından oluşturulan metin yanıtı. Model hiçbir metin üretmezse, düğüm "Empty response from Gemini model..." ifadesini döndürür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/tr.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
