> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/tr.md)

CLIPTextEncodeSD3 düğümü, birden fazla metin istemini farklı CLIP modelleri kullanarak kodlayarak Stable Diffusion 3 modelleri için metin girdilerini işler. Üç ayrı metin girdisini (`clip_g`, `clip_l` ve `t5xxl`) yönetir ve boş metin dolgusu için seçenekler sunar. Düğüm, farklı metin girdileri arasında uygun token hizalamasını sağlar ve SD3 üretim hatlarına uygun koşullandırma verileri döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Metin kodlama için kullanılan CLIP modeli |
| `clip_l` | STRING | Evet | - | Yerel CLIP modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. |
| `clip_g` | STRING | Evet | - | Global CLIP modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. |
| `t5xxl` | STRING | Evet | - | T5-XXL modeli için metin girdisi. Çok satırlı metin ve dinamik istemleri destekler. |
| `boş_dolgu` | COMBO | Evet | `"none"`<br>`"empty_prompt"` | Boş metin girdilerinin nasıl işleneceğini kontrol eder. "none" olarak ayarlandığında, `clip_g`, `clip_l` veya `t5xxl` için boş metin girdileri dolgu yerine boş token listeleriyle sonuçlanır. Bu gelişmiş bir parametredir (varsayılan: "none"). |

**Parametre Kısıtlamaları:**

- `empty_padding` "none" olarak ayarlandığında, `clip_g`, `clip_l` veya `t5xxl` için boş metin girdileri dolgu yerine boş token listeleriyle sonuçlanır
- Düğüm, `clip_l` ve `clip_g` girdileri arasındaki token uzunluklarını, uzunluklar farklı olduğunda kısa olanı boş tokenlerle doldurarak otomatik olarak dengeler
- Tüm metin girdileri dinamik istemleri ve çok satırlı metin girişini destekler

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | SD3 üretim hatlarında kullanıma hazır, kodlanmış metin koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`
