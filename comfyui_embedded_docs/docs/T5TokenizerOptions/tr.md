# T5JetonlaştırıcıSeçenekleri

The T5TokenizerOptions node allows you to configure tokenizer settings for various T5 model types. It sets minimum padding and minimum length parameters for multiple T5 model variants including t5xxl, pile_t5xl, t5base, mt5xl, and umt5xxl. The node takes a CLIP input and returns a modified CLIP with the specified tokenizer options applied.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizer seçeneklerini yapılandırmak için kullanılacak CLIP modeli | CLIP | Evet | - |
| `min_padding` | Tüm T5 model türleri için ayarlanacak minimum padding değeri (varsayılan: 0) | INT | Hayır | 0 ile 10000 |
| `min_length` | Tüm T5 model türleri için ayarlanacak minimum uzunluk değeri (varsayılan: 0) | INT | Hayır | 0 ile 10000 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Güncellenmiş tokenizer seçenekleri tüm T5 varyantlarına uygulanmış değiştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/tr.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
