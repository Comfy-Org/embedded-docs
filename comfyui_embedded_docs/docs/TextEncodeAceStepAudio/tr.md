# TextEncodeAceStepAudio

TextEncodeAceStepAudio düğümü, etiketleri ve şarkı sözlerini token'lar halinde birleştirerek ve ardından bunları ayarlanabilir şarkı sözü gücüyle kodlayarak ses koşullandırma için metin girdilerini işler. Bir CLIP modelini metin açıklamaları ve şarkı sözleriyle birlikte alır, bunları birlikte tokenize eder ve ses üretim görevleri için uygun koşullandırma verileri üretir. Düğüm, şarkı sözlerinin son çıktı üzerindeki etkisini kontrol eden bir güç parametresi aracılığıyla şarkı sözlerinin etkisinin ince ayarlanmasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `etiketler` | Ses koşullandırma için metin etiketleri veya açıklamaları (çok satırlı girdi ve dinamik prompt'ları destekler) | STRING | Evet | - |
| `şarkı_sözleri` | Ses koşullandırma için şarkı sözü metni (çok satırlı girdi ve dinamik prompt'ları destekler) | STRING | Evet | - |
| `şarkı_sözleri_gücü` | Şarkı sözlerinin koşullandırma çıktısı üzerindeki etki gücünü kontrol eder (varsayılan: 1.0, adım: 0.01) | FLOAT | Evet | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | İşlenmiş metin token'larını uygulanmış şarkı sözü gücüyle içeren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
