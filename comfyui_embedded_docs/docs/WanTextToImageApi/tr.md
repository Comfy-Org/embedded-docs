> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/tr.md)

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

Wan Metinden Görüntüye düğümü, metin açıklamalarına dayalı olarak görüntüler üretir. Yazılı istemlerden görsel içerik oluşturmak için yapay zeka modelleri kullanır ve hem İngilizce hem de Çince metin girişini destekler. Düğüm, çıktı görüntü boyutunu, kalitesini ve stil tercihlerini ayarlamak için çeşitli kontroller sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-t2i-preview" | Kullanılacak model (varsayılan: "wan2.5-t2i-preview") |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: boş) |
| `negative_prompt` | STRING | Hayır | - | Kaçınılması gerekenleri tanımlayan olumsuz istem (varsayılan: boş) |
| `width` | INT | Hayır | 768-1440 | Piksel cinsinden görüntü genişliği (varsayılan: 1024, adım: 32) |
| `height` | INT | Hayır | 768-1440 | Piksel cinsinden görüntü yüksekliği (varsayılan: 1024, adım: 32) |
| `seed` | INT | Hayır | 0-2147483647 | Üretim için kullanılacak tohum değeri (varsayılan: 0) |
| `prompt_extend` | BOOLEAN | Hayır | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `watermark` | BOOLEAN | Hayır | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Metin istemine dayalı olarak oluşturulan görüntü |

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`
