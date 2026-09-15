# T5JetonlaştırıcıSeçenekleri

## Genel Bakış

T5TokenizerOptions düğümü, çeşitli T5 model türleri için tokenizer ayarlarını yapılandırır. t5xxl, pile_t5xl, t5base, mt5xl ve umt5xxl dahil olmak üzere birden çok T5 model varyantı için minimum dolgu ve minimum uzunluk parametrelerini ayarlar. Düğüm bir CLIP girdisi alır, ayarları bunun bir kopyasına uygular ve değiştirilmiş CLIP'i döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizer seçeneklerinin yapılandırılacağı CLIP modeli | CLIP | Evet | - |
| `min_dolgu` | Tüm T5 model türleri için ayarlanacak minimum dolgu değeri (varsayılan: 0) | INT | Evet | 0 ile 10000 |
| `min_uzunluk` | Tüm T5 model türleri için ayarlanacak minimum uzunluk değeri (varsayılan: 0) | INT | Evet | 0 ile 10000 |

Not: Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir. Ayarlar, desteklenen tüm T5 varyantlarına tek seferde uygulanır: t5xxl, pile_t5xl, t5base, mt5xl ve umt5xxl. `clip` girdisi değişiklikten önce klonlanır, böylece orijinal CLIP değiştirilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm T5 varyantlarına uygulanan güncellenmiş tokenizer seçenekleriyle değiştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/tr.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
