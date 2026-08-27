# ClipTextEncodeHunyuanDit

`CLIPTextEncodeHunyuanDiT` düğümü, metin açıklamalarını HunyuanDiT modelinin anlayabileceği bir biçime dönüştürür. HunyuanDiT'in çift metin kodlayıcı mimarisi için tasarlanmış gelişmiş bir koşullandırma düğümüdür; iki ayrı metin girdisini farklı tokenizer'lar aracılığıyla işler ve sonuçlarını tek bir koşullandırma çıktısında birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Koşulların oluşturulmasında temel olan, metin tokenizasyonu ve kodlaması için kullanılan bir CLIP model örneği. | CLIP | Evet | - |
| `bert` | BERT tokenizer aracılığıyla kodlanacak metin girdisi. İfadeleri ve anahtar kelimeleri tercih eder. Çok satırlı ve dinamik istemleri destekler. | STRING | Evet | - |
| `mt5xl` | mT5-XL tokenizer aracılığıyla kodlanacak metin girdisi. Çok satırlı ve dinamik istemleri destekler (çok dilli). Tam cümleler ve karmaşık açıklamalar kullanılabilir. | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | BERT ve mT5-XL ile tokenize edilmiş metinleri birleştiren kodlanmış koşullandırma çıktısıdır; üretim görevlerinde daha sonraki işlemler için kullanılır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeHunyuanDit/tr.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
