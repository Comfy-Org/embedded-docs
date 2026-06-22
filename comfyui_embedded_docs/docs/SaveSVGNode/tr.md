# SVGDüğümünüKaydet

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

SVG dosyalarını diske kaydeder. Bu düğüm, girdi olarak SVG verisi alır ve isteğe bağlı meta veri gömme ile bunu çıktı dizininize kaydeder. Düğüm, sayaç sonekleriyle dosya adlandırmayı otomatik olarak yönetir ve iş akışı prompt bilgilerini doğrudan SVG dosyasına gömebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `svg` | Diske kaydedilecek SVG verisi | SVG | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosyanın ön eki. Bu, düğümlerden değerleri dahil etmek için %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgileri içerebilir. (varsayılan: "svg/ComfyUI") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui` | ComfyUI arayüzünde görüntülenmek üzere dosya adı, alt klasör ve tür dahil dosya bilgilerini döndürür | DICT |

**Not:** Bu düğüm, kullanılabilir olduğunda iş akışı meta verilerini (prompt ve ek PNG bilgisi) otomatik olarak SVG dosyasına gömer. Meta veri, SVG'nin meta veri öğesi içinde bir CDATA bölümü olarak eklenir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
