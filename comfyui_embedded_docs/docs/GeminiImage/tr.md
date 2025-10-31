> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/tr.md)

GeminiImage düğümü, Google'ın Gemini AI modellerinden metin ve görüntü yanıtları oluşturur. Tutarlı metin ve görüntü çıktıları oluşturmak için metin istemleri, görüntüler ve dosyalar dahil olmak üzere çoklu ortam girdileri sağlamanıza olanak tanır. Düğüm, en son Gemini modelleriyle tüm API iletişimini ve yanıt ayrıştırmasını halleder.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | gerekli | "" | - | Oluşturma için metin istemi |
| `model` | COMBO | gerekli | gemini_2_5_flash_image_preview | Mevcut Gemini modelleri<br>GeminiImageModel enum'dan alınan seçenekler | Yanıtları oluşturmak için kullanılacak Gemini modeli. |
| `seed` | INT | gerekli | 42 | 0 ile 18446744073709551615 arası | Seed belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamak için elinden geleni yapar. Belirleyici çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı seed değerini kullansanız bile yanıtta değişikliklere neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. |
| `images` | IMAGE | isteğe bağlı | Yok | - | Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). Birden fazla görüntü eklemek için Batch Images düğümünü kullanabilirsiniz. |
| `files` | GEMINI_INPUT_FILES | isteğe bağlı | Yok | - | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden gelen girdileri kabul eder. |

**Not:** Düğüm, sistem tarafından otomatik olarak yönetilen ve kullanıcı girdisi gerektirmeyen gizli parametreler (`auth_token`, `comfy_api_key`, `unique_id`) içerir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Gemini modelinden oluşturulan görüntü yanıtı |
| `STRING` | STRING | Gemini modelinden oluşturulan metin yanıtı |