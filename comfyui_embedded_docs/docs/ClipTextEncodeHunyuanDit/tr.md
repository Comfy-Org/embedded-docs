> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/tr.md)

`CLIPTextEncodeHunyuanDiT` düğümü, metin açıklamalarını HunyuanDiT modelinin anlayabileceği bir biçime dönüştürür. HunyuanDiT'in çift metin kodlayıcı mimarisi için tasarlanmış gelişmiş bir koşullandırma düğümüdür; iki ayrı metin girdisini farklı tokenlaştırıcılar aracılığıyla işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Metin tokenlaştırma ve kodlama için kullanılan bir CLIP model örneği; koşulların oluşturulmasında temel rol oynar. |
| `bert` | STRING | Evet | - | BERT tokenlaştırıcı aracılığıyla kodlanacak metin girdisi. İfadeleri ve anahtar kelimeleri tercih eder. Çok satırlı ve dinamik istemleri destekler. |
| `mt5xl` | STRING | Evet | - | mT5-XL tokenlaştırıcı aracılığıyla kodlanacak metin girdisi. Çok satırlı ve dinamik istemleri (çok dilli) destekler. Tam cümleler ve karmaşık açıklamalar kullanılabilir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Hem BERT hem de mT5-XL tokenlaştırılmış metni birleştiren kodlanmış koşullandırma çıktısı; üretim görevlerinde daha ileri işlemler için kullanılır. |

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
