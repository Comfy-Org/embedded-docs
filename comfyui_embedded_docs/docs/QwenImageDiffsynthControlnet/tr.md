> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/tr.md)

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

QwenImageDiffsynthControlnet düğümü, bir temel modelin davranışını değiştirmek için bir difüzyon sentezi kontrol ağı yaması uygular. Modelin üretim sürecini ayarlanabilir güçle yönlendirmek için bir görüntü girişi ve isteğe bağlı maske kullanarak, kontrol ağının etkisini bünyesine katan ve daha kontrollü görüntü sentezi sağlayan yamalı bir model oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kontrol ağı ile yamalanacak temel model |
| `model_yaması` | MODEL_PATCH | Evet | - | Temel modele uygulanacak kontrol ağı yama modeli |
| `vae` | VAE | Evet | - | Difüzyon sürecinde kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) |
| `görsel` | IMAGE | Evet | - | Kontrol ağını yönlendirmek için kullanılan giriş görüntüsü (yalnızca RGB kanalları kullanılır) |
| `güç` | FLOAT | Evet | -10.0 ila 10.0 | Kontrol ağı etkisinin gücü (varsayılan: 1.0) |
| `maske` | MASK | Hayır | - | Kontrol ağının uygulanması gereken alanları tanımlayan isteğe bağlı maske (dahili olarak ters çevrilir) |

**Not:** Bir maske sağlandığında, otomatik olarak ters çevrilir (1.0 - mask) ve kontrol ağı işlemesi için beklenen boyutlara uyacak şekilde yeniden şekillendirilir. Düğüm, model yamasının bir ZImage Kontrol türü mü yoksa standart bir DiffSynth kontrol ağı mı olduğuna bağlı olarak farklı dahili işleme yöntemleri kullanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Difüzyon sentezi kontrol ağı yaması uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `61833984d0b92be65fae72a894806572c0588dea74a295e8289d1194dee611bb`
