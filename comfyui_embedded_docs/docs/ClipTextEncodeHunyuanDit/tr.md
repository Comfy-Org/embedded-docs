> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/tr.md)

`CLIPTextEncodeHunyuanDiT` düğümünün temel işlevi, giriş metnini modelin anlayabileceği bir forma dönüştürmektir. Bu, HunyuanDiT modelinin çift metin kodlayıcı mimarisi için özel olarak tasarlanmış gelişmiş bir koşullandırma düğümüdür.
Birincil rolü, bir çevirmen gibi, metin açıklamalarımızı AI modelinin anlayabileceği "makine diline" dönüştürmektir. `bert` ve `mt5xl` girişleri farklı türde prompt girdilerini tercih eder.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `clip` | CLIP | Metin tokenizasyonu ve kodlama için kullanılan, koşulların oluşturulmasında temel öneme sahip bir CLIP model örneği. |
| `bert` | STRING | Kodlama için metin girişi, kelime öbekleri ve anahtar kelimeleri tercih eder, çok satırlı ve dinamik prompt'ları destekler. |
| `mt5xl` | STRING | Kodlama için başka bir metin girişi, çok satırlı ve dinamik prompt'ları (çok dilli) destekler, tam cümleler ve karmaşık açıklamalar kullanabilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Oluşturma görevlerinde ileri işlemler için kullanılan kodlanmış koşullu çıktı. |