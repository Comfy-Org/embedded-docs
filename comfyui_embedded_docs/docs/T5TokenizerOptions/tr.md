# T5JetonlaştırıcıSeçenekleri

T5TokenizerOptions düğümü, çeşitli T5 model türleri için tokenleştirici ayarlarını yapılandırmanıza olanak tanır. t5xxl, pile_t5xl, t5base, mt5xl ve umt5xxl dahil olmak üzere birden fazla T5 model varyantı için minimum dolgu ve minimum uzunluk parametrelerini ayarlar. Düğüm, bir CLIP girişi alır ve belirtilen tokenleştirici seçeneklerinin uygulandığı değiştirilmiş bir CLIP döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenleştirici seçeneklerini yapılandırmak için CLIP modeli | CLIP | Evet | - |
| `min_dolgu` | Tüm T5 model türleri için ayarlanacak minimum dolgu değeri (varsayılan: 0) | INT | Hayır | 0 ile 10000 |
| `min_uzunluk` | Tüm T5 model türleri için ayarlanacak minimum uzunluk değeri (varsayılan: 0) | INT | Hayır | 0 ile 10000 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm T5 varyantlarına güncellenmiş tokenleştirici seçeneklerinin uygulandığı değiştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/tr.md)

---
**Source fingerprint (SHA-256):** `bc05c714e4006786d0c948ed1de05324257472337397b0aa4ce574d7483929ff`
