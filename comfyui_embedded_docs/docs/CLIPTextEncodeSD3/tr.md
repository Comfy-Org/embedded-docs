> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/tr.md)

CLIPTextEncodeSD3 düğümü, Stable Diffusion 3 modelleri için metin girişlerini işleyerek farklı CLIP modelleri kullanarak birden fazla metin istemini kodlar. Üç ayrı metin girişini (clip_g, clip_l ve t5xxl) işler ve boş metin dolgusu yönetimi için seçenekler sunar. Düğüm, farklı metin girişleri arasında uygun token hizalaması sağlar ve SD3 üretim pipeline'ları için uygun koşullandırma verilerini döndürür.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Gerekli | - | - | Metin kodlama için kullanılan CLIP modeli |
| `clip_l` | STRING | Çok Satırlı, Dinamik İstemler | - | - | Yerel CLIP modeli için metin girişi |
| `clip_g` | STRING | Çok Satırlı, Dinamik İstemler | - | - | Global CLIP modeli için metin girişi |
| `t5xxl` | STRING | Çok Satırlı, Dinamik İstemler | - | - | T5-XXL modeli için metin girişi |
| `boş_dolgu` | COMBO | Seçim | - | ["none", "empty_prompt"] | Boş metin girişlerinin nasıl işleneceğini kontrol eder |

**Parametre Kısıtlamaları:**

- `empty_padding` "none" olarak ayarlandığında, `clip_g`, `clip_l` veya `t5xxl` için boş metin girişleri, dolgu yerine boş token listeleriyle sonuçlanır
- Düğüm, uzunluklar farklı olduğunda daha kısa olanı boş token'larla doldurarak `clip_l` ve `clip_g` girişleri arasındaki token uzunluklarını otomatik olarak dengeler
- Tüm metin girişleri dinamik istemleri ve çok satırlı metin girişini destekler

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | SD3 üretim pipeline'larında kullanıma hazır kodlanmış metin koşullandırma verileri |