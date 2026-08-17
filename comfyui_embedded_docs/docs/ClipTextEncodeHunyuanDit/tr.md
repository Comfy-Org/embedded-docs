# CLIPMetinKodlamaHunyuanDiT

`CLIPTextEncodeHunyuanDiT` düğümü, metin açıklamalarını HunyuanDiT modelinin anlayabileceği bir biçime dönüştürür. HunyuanDiT'in çift metin kodlayıcı mimarisi için tasarlanmış gelişmiş bir koşullandırma düğümüdür; iki ayrı metin girdisini farklı tokenleştiriciler aracılığıyla işler ve bunları tek bir koşullandırma çıktısında birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin tokenleştirme ve kodlama için kullanılan, koşulların üretilmesinde temel olan bir CLIP model örneği. | CLIP | Yes | - |
| `bert` | BERT tokenleştirici ile kodlanacak metin girdisi. İfadeleri ve anahtar kelimeleri tercih eder. Çok satırlı ve dinamik istemleri destekler. | STRING | Yes | - |
| `mt5xl` | mT5-XL tokenleştirici ile kodlanacak metin girdisi. Çok satırlı ve dinamik istemleri (çok dilli) destekler. Tam cümleler ve karmaşık açıklamalar kullanılabilir. | STRING | Yes | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| CONDITIONING | Hem BERT hem de mT5-XL ile tokenleştirilmiş metni birleştiren, üretim görevlerinde daha ileri işlemler için kullanılan kodlanmış koşullandırma çıktısı. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/tr.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
