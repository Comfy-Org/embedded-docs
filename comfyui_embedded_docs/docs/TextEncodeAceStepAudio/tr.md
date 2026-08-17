# TextEncodeAceStepAudio

### Genel Bakış

TextEncodeAceStepAudio düğümü, etiketleri ve şarkı sözlerini token'larda birleştirerek ve ardından ayarlanabilir şarkı sözü gücüyle kodlayarak ses koşullandırması için metin girdilerini işler. Bir CLIP modelini metin açıklamaları ve şarkı sözleriyle birlikte alır, bunları birlikte tokenize eder ve ses üretim görevleri için uygun koşullandırma verileri üretir. Düğüm, şarkı sözlerinin son çıktı üzerindeki etkisini kontrol eden bir güç parametresi aracılığıyla bu etkinin ince ayarını yapmayı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `tags` | Ses koşullandırması için metin etiketleri veya açıklamalar (çok satırlı giriş ve dinamik istemleri destekler) | STRING | Evet | - |
| `lyrics` | Ses koşullandırması için şarkı sözü metni (çok satırlı giriş ve dinamik istemleri destekler) | STRING | Evet | - |
| `lyrics_strength` | Şarkı sözlerinin koşullandırma çıktısı üzerindeki etkisinin gücünü kontrol eder (varsayılan: 1.0, adım: 0.01) | FLOAT | Hayır | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | İşlenmiş metin token'larını ve uygulanan şarkı sözü gücünü içeren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
