> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

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

Kling Başlangıç-Bitiş Karesinden Video düğümü, sağladığınız başlangıç ve bitiş görselleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye kadar yumuşak bir dönüşüm üretmek için aradaki tüm kareleri oluşturur. Bu düğüm, görselden videoya API'sini çağırır ancak yalnızca `image_tail` istek alanıyla çalışan giriş seçeneklerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Evet | - | Referans Görsel - URL veya Base64 kodlu dize, 10MB'ı geçemez, çözünürlük en az 300*300 piksel olmalıdır, en-boy oranı 1:2,5 ~ 2,5:1 arasında olmalıdır. Base64, data:image ön ekini içermemelidir. |
| `end_frame` | IMAGE | Evet | - | Referans Görsel - Bitiş karesi kontrolü. URL veya Base64 kodlu dize, 10MB'ı geçemez, çözünürlük en az 300*300 piksel olmalıdır. Base64, data:image ön ekini içermemelidir. |
| `prompt` | STRING | Evet | - | Pozitif metin istemi |
| `negative_prompt` | STRING | Evet | - | Negatif metin istemi |
| `cfg_scale` | FLOAT | Hayır | 0.0-1.0 | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) |
| `aspect_ratio` | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1" | Oluşturulan video için en-boy oranı (varsayılan: "16:9") |
| `mode` | COMBO | Hayır | Birden çok seçenek mevcut | Video oluşturma için kullanılacak yapılandırma, şu formatta: mod / süre / model_adı. (varsayılan: mevcut modlardan yedinci seçenek) |

**Görsel Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` sağlanmalıdır ve dosya boyutu 10MB'ı geçemez
- Her iki görsel için minimum çözünürlük: 300×300 piksel
- `start_frame` en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır
- Base64 kodlu görseller "data:image" ön ekini içermemelidir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dizisi |
| `video_id` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süresi |

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
