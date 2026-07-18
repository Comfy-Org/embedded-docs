# Google Gemini Omni (Video)

Bu düğüm, Google'ın Gemini Omni Flash modelini kullanarak bir metin isteminden sesli video oluşturur. İsteğe bağlı olarak, sonucu yönlendirmek veya düzenlemek için referans görseller veya videolar sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | COMBO | Evet | `"Omni Flash"` |
| `seed` | Tohum (seed), düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

**Not:** `model` parametresi, "Omni Flash" seçildiğinde ek girişler içerecek şekilde genişleyen dinamik bir kombinasyon kutusudur. Bu ek girişler şunları içerir:
- `prompt` (STRING, zorunlu): İstenen videoyu tanımlayan metin istemi. İstenen süreyi (3-10 saniye) ve en boy oranını (16:9 veya 9:16) doğrudan istemde belirtin.
- `images` (IMAGE, isteğe bağlı): Video oluşturmayı yönlendirmek için referans görseller. Maksimum 14 görsel.
- `videos` (VIDEO, isteğe bağlı): Video oluşturmayı yönlendirmek için referans videolar. Her biri maksimum 10 saniye süreli olmak üzere maksimum 3 video.
- `temperature` (FLOAT, isteğe bağlı, varsayılan: 1.0): Oluşturmadaki rastgeleliği kontrol eder.
- `top_p` (FLOAT, isteğe bağlı, varsayılan: 0.95): Çekirdek örneklemeyi kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Sesli olarak oluşturulan video. | VIDEO |
| `text` | Varsa, modelden gelen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `948eb712ca0ad3b7d3c7b3a9e1576f2c52a3575c07d8d52bb727bd9df717caa6`
