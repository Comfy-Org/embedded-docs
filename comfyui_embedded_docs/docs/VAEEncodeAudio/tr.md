> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/tr.md)

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

VAEEncodeAudio düğümü, bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak ses verilerini gizli bir temsile dönüştürür. Ses girdisini alır ve sıkıştırılmış gizli örnekler oluşturmak için VAE aracılığıyla işler; bu örnekler daha sonraki ses üretimi veya manipülasyon görevleri için kullanılabilir. Düğüm, kodlamadan önce gerekirse sesi VAE'nin beklenen örnekleme hızına uyacak şekilde otomatik olarak yeniden örnekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | AUDIO | Evet | - | Kodlanacak ses verisi; dalga formu ve örnekleme hızı bilgilerini içerir |
| `vae` | VAE | Evet | - | Sesi gizli uzaya kodlamak için kullanılan Varyasyonel Otomatik Kodlayıcı modeli |

**Not:** Ses girdisi, orijinal örnekleme hızı VAE'nin beklenen değerinden (varsayılan: 44100 Hz) farklıysa, otomatik olarak VAE'nin beklenen örnekleme hızına yeniden örneklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Sıkıştırılmış örnekler içeren, gizli uzaydaki kodlanmış ses temsili |

---
**Source fingerprint (SHA-256):** `db509ab571154c4cedbfc6cae6591bd2b67b2c6e2261766565cdb0205b2c2ecc`
