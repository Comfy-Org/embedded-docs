# Google Gemini Omni (Video)

Google'ın Gemini Omni Flash modeliyle bir metin isteminden sesli video oluşturun. Sonucu yönlendirmek veya düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar sağlayabilirsiniz. İstemde istenen uzunluğu (3-10 sn) ve en-boy oranını (16:9 veya 9:16) doğrudan belirtin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | MODEL | Yes | "Omni Flash" |
| `seed` | Seed, düğümün tekrar çalıştırılıp çalıştırılmayacağını kontrol eder; seed ne olursa olsun sonuçlar deterministik değildir. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
