# CLIPMetinKodlamaSD3

CLIPTextEncodeSD3 düğümü, farklı CLIP modellerini kullanarak birden fazla metin istemini kodlayarak Stable Diffusion 3 modelleri için metin girdilerini işler. Üç ayrı metin girdisini (`clip_g`, `clip_l` ve `t5xxl`) yönetir ve boş metin doldurma işlemleri için seçenekler sunar. Düğüm, farklı metin girdileri arasında uygun token hizalamasını sağlar ve SD3 üretim hatlarına uygun koşullandırma verileri döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Metin kodlaması için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_l` | Yerel CLIP modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `clip_g` | Global CLIP modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `t5xxl` | T5-XXL modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | - |
| `empty_padding` | Boş metin girdilerinin nasıl işleneceğini kontrol eder. "none" olarak ayarlandığında, `clip_g`, `clip_l` veya `t5xxl` için boş metin girdileri doldurma yerine boş token listeleriyle sonuçlanır. Bu bir gelişmiş parametredir (varsayılan: "none"). | COMBO | Evet | `"none"`<br>`"empty_prompt"` |

**Parametre Kısıtlamaları:**

- `empty_padding` "none" olarak ayarlandığında, `clip_g`, `clip_l` veya `t5xxl` için boş metin girdileri doldurma yerine boş token listeleriyle sonuçlanır.
- Düğüm, `clip_l` ve `clip_g` girdileri arasındaki token uzunluklarını, uzunluklar farklı olduğunda kısa olanı boş tokenlerle doldurarak otomatik olarak dengeler.
- Tüm metin girdileri dinamik istemleri ve çok satırlı metin girişini destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | SD3 üretim hatlarında kullanıma hazır, kodlanmış metin koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/tr.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`
