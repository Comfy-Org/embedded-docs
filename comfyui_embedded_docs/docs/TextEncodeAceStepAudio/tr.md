> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/tr.md)

TextEncodeAceStepAudio düğümü, etiketleri ve şarkı sözlerini token'lara birleştirerek ve ayarlanabilir şarkı sözü gücü ile kodlayarak, ses koşullandırması için metin girişlerini işler. Bir CLIP modelini metin açıklamaları ve şarkı sözleriyle birlikte alır, bunları birlikte token'lara ayırır ve ses üretimi görevleri için uygun koşullandırma verisi oluşturur. Düğüm, son çıktı üzerindeki etkilerini kontrol eden bir güç parametresi aracılığıyla şarkı sözlerinin etkisinin ince ayarını yapmayı sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Token'lara ayırma ve kodlama için kullanılan CLIP modeli |
| `tags` | STRING | Evet | - | Ses koşullandırması için metin etiketleri veya açıklamaları (çok satırlı giriş ve dinamik prompt'ları destekler) |
| `lyrics` | STRING | Evet | - | Ses koşullandırması için şarkı sözleri metni (çok satırlı giriş ve dinamik prompt'ları destekler) |
| `lyrics_strength` | FLOAT | Hayır | 0.0 - 10.0 | Koşullandırma çıktısı üzerindeki şarkı sözü etkisinin gücünü kontrol eder (varsayılan: 1.0, adım: 0.01) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Uygulanmış şarkı sözü gücü ile işlenmiş metin token'larını içeren kodlanmış koşullandırma verisi |