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

Bu düğüm, ComfyUI'nin giriş dizini içindeki belirtilen bir alt klasörden birden fazla görüntü yükler. Seçilen klasörde yaygın görüntü dosyası türlerini tarar ve bunları bir liste olarak döndürür; bu da onu toplu işleme veya veri kümesi hazırlığı için kullanışlı hale getirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin yükleneceği klasör. Seçenekler, ComfyUI'nin ana giriş dizininde bulunan alt klasörlerdir. | STRING | Evet | *Birden çok seçenek mevcut* |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görüntülerin listesi. Düğüm, seçilen klasörde bulunan tüm geçerli görüntü dosyalarını (PNG, JPG, JPEG, WEBP) yükler. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `0f6e1b3d159f7d7c0c9530350ee057118a2618796f149586bae925253ecc8cf0`
