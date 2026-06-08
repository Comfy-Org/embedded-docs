## Genel Bakış

TextEncodeAceStepAudio düğümü, etiketler ve şarkı sözlerini token'larda birleştirip ayarlanabilir şarkı sözü gücüyle kodlayarak ses koşullandırması için metin girdilerini işler. Bir CLIP modelini metin açıklamaları ve şarkı sözleriyle birlikte alır, bunları birlikte tokenize eder ve ses üretim görevlerine uygun koşullandırma verileri oluşturur. Düğüm, şarkı sözlerinin son çıktı üzerindeki etkisini kontrol eden bir güç parametresi aracılığıyla etkilerinin ince ayarını yapmaya olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `etiketler` | Ses koşullandırması için metin etiketleri veya açıklamaları (çok satırlı giriş ve dinamik istemleri destekler) | STRING | Evet | - |
| `şarkı_sözleri` | Ses koşullandırması için şarkı sözü metni (çok satırlı giriş ve dinamik istemleri destekler) | STRING | Evet | - |
| `şarkı_sözleri_gücü` | Şarkı sözlerinin koşullandırma çıktısı üzerindeki etki gücünü kontrol eder (varsayılan: 1.0, adım: 0.01) | FLOAT | Hayır | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Uygulanan şarkı sözü gücüyle birlikte işlenmiş metin token'larını içeren kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/tr.md)

---
**Source fingerprint (SHA-256):** `89600133d8b0edaa36958530dacffe812675b595b0d77db702bb7709567cd83d`
